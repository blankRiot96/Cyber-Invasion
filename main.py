import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption('Game')


# Sprites
from src.sprites import player

# World
from src.world import draw_world

# Define colours
bg = (0, 0, 0)

run = True
while run:
    clock.tick(fps)

    # Draw background
    screen.fill(bg)
    draw_world(screen)
    for i in range(len(player)):
        screen.blit(player[i], (70*i, 50))
    

    # for i in range(grid+1):
    #     screen.blit(block, (450 - (x_dif*i), 0 + (y_dif*i)))

    ## Procedural Pattern
    # Row 1
    # screen.blit(block, (450, 0))
    # screen.blit(block, (450 - x_dif, 37))
    # # Row 2
    # screen.blit(block, (450 + x_dif, 37))
    # screen.blit(block, (450, 37 + y_dif))
    # screen.blit(block, (450 - x_dif, 37 + (y_dif*2)))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
