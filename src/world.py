import pygame
import json
from src.sprites import brick_block_1, brick_block_2, brick_block_3, dirt_block
from src.diff_val import x_dif, y_dif

# Essentials
grid = 20
by = 0
reference = {
    "brick_block_1": brick_block_1,
    "brick_block_2": brick_block_2,
    "brick_block_3": brick_block_3,
    "dirt_block": dirt_block
}


def load_world(level):
    blocks = {}
    if level == "playground":
        with open("src/level_data/level_test.json", "r") as f:
            blocks = json.loads(f.read())

    return blocks


def draw_world(screen, blocks):
    # Index is the current dictionary we are
    # inside of the list [{'block-41MR2p4': [480.0, 615.0, 60, 60]}...]
    # So from 1..max num of blocks

    # e is the dictionary itself: {'block-41MR2p4': [480.0, 615.0, 60, 60]}
    for index, e in enumerate(blocks["objects"]):
        # i: 'block-41MR2p4'
        for i in e:
            block = i[: i.find("-")]

            params = blocks["objects"][index][i]
            rect = pygame.Rect(*params)  # x, y, block_size, block_size
            
            screen.blit(reference[block], rect)


# Draw fun
up = True
selected = True


def draw_fun(screen):
    global by, up, selected
    if up:
        if by < 15:
            by += 0.1
        else:
            up = False
    else:
        if by > 0:
            by -= 0.1
        else:
            up = True

    for e in range(grid + 2):
        for i in range(grid + 1):
            # Very simple On/Off switch
            selected = not selected

            # Blit
            if selected:
                screen.blit(
                    brick_block_1,
                    (
                        (450 + (x_dif * e)) - (x_dif * i),
                        by + (0 + (y_dif * i) + (y_dif * e)),
                    ),
                )
            else:
                screen.blit(
                    brick_block_1,
                    ((450 + (x_dif * e)) - (x_dif * i), 0 + (y_dif * i) + (y_dif * e)),
                )
