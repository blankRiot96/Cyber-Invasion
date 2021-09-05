import pygame
import json

# Draw world variables
# x_dif = 450 - 385
# y_dif = 37
x_dif = 450 - 424
y_dif = 15
grid = 20
by = 0
up = True
selected = True

# Blocks
from src.sprites import block


def load_world(level):
    blocks = {}
    if level == 'playground':
        with open('src/LevelData/level_test.json', 'r') as f:
            blocks = json.loads(f.read())  
    

    return blocks


def draw_world(screen, blocks):
    for index, e in enumerate(blocks['objects']):
        for i in e:
            obj = i[:i.find('-')]

            params = blocks['objects'][index][i]
            rect = pygame.Rect(*params)
            if obj == 'block':
                screen.blit(block, rect)


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
    

    for e in range(grid+2):
        for i in range(grid+1):
            # Very simple On/Off switch
            selected = not selected
            
            # Blit
            if selected:
                screen.blit(block, ((450 + (x_dif*e)) - (x_dif*i), by + (0 + (y_dif*i) + (y_dif*e))))
            else:
                screen.blit(block, ((450 + (x_dif*e)) - (x_dif*i), 0 + (y_dif*i) + (y_dif*e)))



