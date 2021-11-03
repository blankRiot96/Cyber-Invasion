import pygame
import sys
import time
from pygame.locals import *

from src.effects.cursor_effects import Cursor

pygame.init()
pygame.display.set_caption('Trial Window')
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

#pygame.mouse.set_visible(False)
from src.sprites import gear_icon


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = surface.get_rect()

    return rotated_surface, rotated_rect


# Objects
cursor2 = Cursor((100, 255, 255), 1)

start = time.time()
while True:
    clock.tick()
    # pygame.display.set_caption(f"Iso Level Editor ({int(clock.get_fps())})")

    # Time for each iteration
    end = time.time()

    dt = end - start
    dt *= 100

    start = time.time()

    # Render
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()
    # cursor2.update(mx, my, screen, dt)
    # cursor(screen, mx, my, 1, 1)
    gear_icon = pygame.transform.rotozoom(gear_icon, 1, 1)
    screen.blit(gear_icon, (0, 0))  # gear_icon_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

