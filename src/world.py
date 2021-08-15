import pygame

# Draw world variables
x_dif = 450 - 385
y_dif = 37
grid = 5

# Blocks
from src.sprites import block

def draw_world(screen):
    for e in range(grid+2):
        for i in range(grid+1):
            screen.blit(block, ((450 + (x_dif*e)) - (x_dif*i), 0 + (y_dif*i) + (y_dif*e)))

