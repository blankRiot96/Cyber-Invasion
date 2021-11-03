import pygame
from pygame.constants import BLEND_RGB_ADD
import random


def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


# [loc, velocity, timer]
particles = []
count = 0


def cursor(screen, mx, my, gen_cooldown, dt):
    global particles, count
    count += dt

    if count >= gen_cooldown:
        particles.append([[mx, my], [random.randint(0, 10) / 10 - 1, -3], random.randint(5, 10)])
        count = 0

    for particle in particles:
        particle[0][0] += particle[1][0] * dt
        particle[0][1] += particle[1][1] * dt

        particle[2] -= 0.3
        if particle[2] <= 0:
            particles.remove(particle)
            continue

        # particle[1][1] += 0.15
        pygame.draw.circle(screen, (100, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 2
        screen.blit(circle_surf(radius, (20, 20, 20)), (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                    special_flags=BLEND_RGB_ADD)
