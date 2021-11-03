import pygame
import time
import json

from src.id_generator import return_id

# Setup
pygame.init()

clock = pygame.time.Clock()

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Isometric Level Editor")

pygame.mouse.set_visible(False)

from src.sprites import (
    brick_block_1,
    brick_block_2,
    brick_block_3,
    dirt_block,
    gear_icon,
    gear_icon_size,
    menu_bar_img,
    menu_bar_size,
    green_check_mark_img,
    scale_image
)
from src.world import draw_world
from src.diff_val import x_dif, y_dif
from src.border import return_color
from src.widgets import Button
from src.effects.cursor_effects import Cursor
from src.effects.expanding_circle import ExpandingCircle


# Fonts
comic_sans_ms = pygame.font.SysFont('comicsansms', 24)
ebrima = pygame.font.SysFont('ebrima', 17)

# Texts
safe_mode = comic_sans_ms.render("Safe Mode", True, (255, 255, 255))

# Switching between blocks
switch = {49: brick_block_1, 50: brick_block_2, 51: brick_block_3, 52: dirt_block}

id_switch = {
    49: "brick_block_1",
    50: "brick_block_2",
    51: "brick_block_3",
    52: "dirt_block",
}

# Essentials
block_size = 60
grid = 20
bx, by = 0, 0

path = "src/level_data/level_test.json"

# Levels
with open(path, "r") as f:
    level_test = json.loads(f.read())


level_test["objects"] = []


def return_base():
    level_grid = []
    for e in range(grid + 2):
        for i in range(grid + 1):
            x = (450 + (x_dif * e)) - (x_dif * i)
            y = 0 + (y_dif * i) + (y_dif * e)
            level_grid.append([x, y])
            level_test["objects"].append(
                {return_id("brick_block_1"): [x, y, block_size, block_size]}
            )

    return level_test, level_grid


def closest(lst, k):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - k))]


def sort(blocks) -> dict[str, list[dict[str, list[int]]]]:
    blocks["objects"] = sorted(blocks["objects"], key=lambda v: v[next(iter(v))][0])

    return blocks


def multiples(x_dif, y, start_val):
    multiples_x = [0]
    i = 1
    while multiples_x[-1] <= screen_width:
        multiples_x.append(x_dif * i)
        i += 1

    multiples_y = [start_val]
    i = 1
    while multiples_y[-1] <= screen_height:
        multiples_y.append((y * i) + start_val)
        i += 1

    return multiples_x, multiples_y


def replace_block(lst: list[dict], block, coord: list[int]) -> list[dict]:
    # Index is the current dictionary we are
    # inside of the lst = [{'block-41MR2p4': [480.0, 615.0, 60, 60]}...]
    # So from 1..max num of blocks

    # e is the dictionary itself: {'block-41MR2p4': [480.0, 615.0, 60, 60]}
    for index, e in enumerate(lst):
        # i: 'block-41MR2p4'
        for i in e:
            params = blocks["objects"][index][i]
            if coord == params[:2]:
                lst[index][return_id(block)] = lst[index].pop(i)
                break

    return lst


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = surface.get_rect()

    return rotated_surface, rotated_rect

def save(blocks):
    with open(path, "w") as f:
        json.dump(blocks, f, indent=2)


# Game Variables
on_click_circles = []
scale_cool_down = 0.2
scale_count = 0
open_menu_bar = False
once = True
number_keys = [eval(f"pygame.K_{i}") for i in range(1, len(switch) + 1)]

# Check Box
check_box_size = 30
check_box_rect = pygame.Rect((60 + 180, 70), (check_box_size, check_box_size))
check_mark = pygame.transform.scale(green_check_mark_img, (check_box_size, check_box_size))

# Rectangles
gear_icon_rect = pygame.Rect((20, 20), (gear_icon_size, gear_icon_size))

# Colour
colour = [0, 0, 0]
direction = ""
gear_icon.set_alpha(150)
menu_bar_img.set_alpha(100)
on_click = False

# Buttons
save_btn = Button("  Save", (60, 180), (80, 30), (255, 255, 255), (0, 255, 0))
clear_btn = Button("  Clear", (180, 180), (80, 30), (255, 255, 255), (255, 0, 0))

# Safe
blocks, level_grid = return_base()
x_grid = [coord[0] for coord in level_grid]
y_grid = [coord[1] for coord in level_grid]

# Blocks
preview_block = brick_block_1.copy()
preview_block.set_alpha(150)
cursor2 = Cursor((100, 255, 255), 1)
current_block = "brick_block_1"

# Unsafe
multiples_x, multiples_y_1 = multiples(x_dif, x_dif, start_val=x_dif)
_, multiples_y_2 = multiples(x_dif, x_dif, start_val=y_dif)
registered = [[0, 0]]

start = time.time()
safe = True
run = True
while run:
    clock.tick()
    pygame.display.set_caption(f"Iso Level Editor ({int(clock.get_fps())})")

    # Time for each iteration
    end = time.time()

    dt = end - start
    dt *= 100
    scale_count += dt
    start = time.time()

    # Background Colour
    screen.fill((0, 0, 0))
    screen.blit(gear_icon, gear_icon_rect)

    mx, my = pygame.mouse.get_pos()

    draw_world(screen, blocks)
    if safe:
        bx = closest(x_grid, mx - (block_size / 2))
        by = closest(y_grid, my - (block_size / 4))
    else:
        bx = closest(multiples_x, mx - 30)
        if bx % (2 * x_dif) == 0:
            by = closest(multiples_y_2, my - 30)
        elif bx % x_dif == 0:
            by = closest(multiples_y_1, my - 30)

    # Current Block Preview
    screen.blit(preview_block, (1000, 12))
    current_block_text = ebrima.render(current_block, True, (242, 255, 0))
    screen.blit(current_block_text, (980, 12 + block_size))

    # Drawing Click Effect
    for circle in on_click_circles:
        circle.draw(screen, dt)
        if circle.radius >= circle.max_radius:
            on_click_circles.remove(circle)

    # Brighten on Hover
    if gear_icon_rect.collidepoint(mx, my):
        gear_icon.set_alpha(255)
    else:
        gear_icon.set_alpha(150)

    # Check for mouse input
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        if safe:
            if not open_menu_bar:
                if [bx, by] in level_grid:
                    blocks["objects"] = replace_block(
                        blocks["objects"], current_block, [bx, by]
                    )
        elif not open_menu_bar and not on_click:
            if [bx, by] not in registered:
                new_id = return_id(current_block)
                blocks["objects"].append({new_id: [bx, by, block_size, block_size]})
                # blocks = sort(blocks)

                registered.append([bx, by])

        scale_count = 0

    # Rendering Menu bar
    var = menu_bar_size / 3
    if open_menu_bar:
        screen.blit(menu_bar_img, (100 - var, 200 - var))

    # Open animation
    if scale_count >= scale_cool_down:
        if open_menu_bar:
            if menu_bar_size <= 800:
                menu_bar_size += 8
                menu_bar_img = pygame.transform.scale(
                    menu_bar_img, (menu_bar_size, menu_bar_size)
                )
            # Draw things to be on the menu bar
            else:
                screen.blit(safe_mode, (60, 70))
                pygame.draw.rect(screen, (255, 255, 255), check_box_rect, width=3)
                if safe:
                    screen.blit(check_mark, check_box_rect)
                save_btn.draw(screen, (mx, my))
                clear_btn.draw(screen, (mx, my))

        scale_count = 0
        on_click = False

    # Preview Block Cursor for Terrain
    if not safe:
        screen.blit(preview_block, (bx, by))

    # Dynamic Colouring
    colour, direction = return_color(colour, direction, dt)

    # Setting colours
    # clear_btn.colour = colour
    cursor2.colour = colour

    # Setting Cursor
    cursor2.update(mx, my, screen, dt)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            on_click_circles.append(ExpandingCircle((mx, my), 15, 40, 0.9, (255, 255, 255)))
            if gear_icon_rect.collidepoint(mx, my):
                open_menu_bar = not open_menu_bar
                on_click = True

                # Reset Menu Bar
                menu_bar_size = 500
                menu_bar_img = pygame.image.load("assets/images/menu_bar.png").convert_alpha()
                menu_bar_img = pygame.transform.scale(menu_bar_img, (menu_bar_size, menu_bar_size))
                menu_bar_img.set_alpha(100)
            # Setting safe mode on and off
            elif check_box_rect.collidepoint(mx, my):
                safe = not safe
            # Saving current level
            elif save_btn.hover((mx, my)):
                save(blocks)
            # Clearing current level
            elif clear_btn.hover((mx, my)):
                blocks["objects"] = []
                blocks, level_grid = return_base()
                registered = []

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save(blocks)
            # Any number key
            if event.key in number_keys:
                current_block = id_switch[event.key]
                preview_block = switch[event.key].copy()
                preview_block.set_alpha(150)

    pygame.display.update()

pygame.quit()
