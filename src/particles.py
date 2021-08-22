#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

# [loc, velocity, timer]
particles = []

# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (50, 20, 120), pygame.Rect(100, 100, 200, 80))

    mx, my = pygame.mouse.get_pos()
    particles.append([[250, 250], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.15
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 2
        screen.blit(circle_surf(radius, (20, 20, 20)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

        if particle[2] <= 0:
            particles.remove(particle)

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
