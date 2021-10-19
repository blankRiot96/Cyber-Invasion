import pygame
import json

from src.id_generator import return_id

# Setup
pygame.init()

clock = pygame.time.Clock()

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Isometric Level Editor")

from src.sprites import brick_block_1, brick_block_2, brick_block_3, dirt_block
from src.world import draw_world
from src.diff_val import x_dif, y_dif

# Switching between blocks
switch = {
    1: brick_block_1,
    2: brick_block_2,
    3: brick_block_3,
    4: dirt_block
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
    for e in range(grid + 2):
        for i in range(grid + 1):
            x = (450 + (x_dif * e)) - (x_dif * i)
            y = 0 + (y_dif * i) + (y_dif * e)
            level_test["objects"].append(
                {return_id("brick_block_1"): [x, y, block_size, block_size]}
            )

    return level_test


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


# with open(path, 'w') as f:
#     json.dump(return_base(), f, indent=2)


blocks = return_base()
preview_block = brick_block_1.copy()
preview_block.set_alpha(150)

multiples_x, multiples_y_1 = multiples(x_dif, x_dif, start_val=x_dif)
_, multiples_y_2 = multiples(x_dif, x_dif, start_val=y_dif)
registered = [[0, 0]]

run = True
while run:
    clock.tick()
    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    draw_world(screen, blocks)

    bx = closest(multiples_x, mx - 30)
    if bx % (2 * x_dif) == 0:
        by = closest(multiples_y_2, my - 30)
    elif bx % x_dif == 0:
        by = closest(multiples_y_1, my - 30)

    screen.blit(preview_block, (bx, by))

    # Check for mouse input
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        if [bx, by] not in registered:
            new_id = return_id("brick_block_1")

            blocks["objects"].append({new_id: [bx, by, block_size, block_size]})
            # blocks = sort(blocks)

        registered.append([bx, by])

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                with open(path, "w") as f:
                    json.dump(return_base(), f, indent=2)
            # if event.key == pygame.K_

    pygame.display.update()

pygame.quit()
