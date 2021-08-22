import pygame
from pygame.locals import *

import time

pygame.init()

clock = pygame.time.Clock()

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption('Game')


# Sprites
from src.sprites import player, block

# World
from src.world import draw_world, draw_fun

# Border
from src.border import draw_border, return_color



# Define colours
bg = (25, 25, 25)

# Game Variables
index = 0
start = time.time()

count = 100  # Count var

x_dif = 450 - 350
y_dif = 25
grid = 10

# Border variables
particles = []
color = [0, 0, 0]
direction = "up"


run = True
while run:
    clock.tick()

    # Time for each iteration
    end = time.time()

    dt = end - start
    dt *= 60
    count += dt
    if count >= 100000:
        count = 100

    start = time.time()

    # Rendering
    # Draw background
    screen.fill(bg)
    draw_world(screen)
    print(color)
    color, direction = return_color(color, direction)
    print(color)
    draw_border(screen, particles, tuple(color), count)
    
    index += dt/8

    try:
        player[int(index)]
    except IndexError:
        index = 0
    
    screen.blit(player[int(index)], (70, 50))


    

    # for i in range(grid+1):
    #     screen.blit(block, (450 - (x_dif*i), 0 + (y_dif*i)))

    # Procedural Pattern
    # Row 1
    # screen.blit(block, (450, 0))
    # screen.blit(block, (424, 15))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
