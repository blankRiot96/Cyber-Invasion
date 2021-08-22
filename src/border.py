import pygame, random, time
from pygame.constants import BLEND_RGB_ADD

from src.particle import Particle


def return_color(color: list, direction: str) -> list:
    r = color[0]
    g = color[1]
    b = color[2]

    if direction == "up":
        if r < 255:
            r += 1
        elif g < 255:
            g += 1
        elif b < 255:
            b += 1
        else:
            direction = "down"
    else:
        if r > 0:
            r -= 1
        elif g > 0:
            g -= 1
        elif b > 0:
            b -= 1
        else:
            direction = "up" 

    color = [r, g, b]

    return color, direction 


def circle_surf(radius, color) -> pygame.Surface:
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))

    return surf


def draw_border(screen, particles:list, color: tuple, count) -> None:
    # Creating particles
    if int(count) % 3 == 0:
        particles.append([random.choice([[random.randrange(0, 1100), 600],
                 [random.randrange(0, 1100), 0], [0, random.randrange(0, 600)], [1100, random.randrange(0, 600)]]),
                 [0.4, -0.4], random.randint(6, 8),
                 random.choice([[random.randrange(0, 1100), 600],
                 [random.randrange(0, 1100), 0], [0, random.randrange(0, 600)], [1100, random.randrange(0, 600)]])])

    # Updating particles
    for particle in particles:
        if (particle[3][0] in range(0, 1100)) and (particle[3][1] == 600):
            particle[0][0] += random.randint(-2, 2)
            particle[0][1] += particle[1][1]
        elif (particle[3][0] in range(0, 1100)) and (particle[3][1] == 0):
            particle[0][0] += random.randint(-2, 2)
            particle[0][1] -= particle[1][1]
        elif (particle[3][0] == 0) and (particle[3][1] in range(0, 600)):
            particle[0][0] += particle[1][0]
            particle[0][1] += random.randint(-2, 2)
        elif (particle[3][0] == 1100) and (particle[3][1] in range(0, 600)):
            particle[0][0] -= particle[1][0]
            particle[0][1] += random.randint(-2, 2)
        
        
        particle[2] -= 0.04

        # Rendering Particles
        pygame.draw.circle(screen, color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 2
        screen.blit(circle_surf(radius, (20, 20, 20)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

        # Removing Particles
        if particle[2] <= 0:
            particles.remove(particle)


''' RECTANGLE ATTEMPT TO BE DOCUMENTED
# def glow_surface(size: list, color: list, rect) -> pygame.Surface:
#     try:
#         surf = pygame.Surface((int(size[0]) + 1, int(size[1]) + 1))
#     except:
#         surf = pygame.Surface((1, 1))
#     pygame.draw.rect(surf, tuple(color), rect)
#     surf.set_colorkey((0, 0, 0))

#     return surf


# def draw_border(screen, particles: list, count) -> None:
#     if int(count) % 8 == 0:
#         particles.append(Particle([random.randrange(0, 1100), 600], [255, 255, 255], [5, 5]))
#     for particle in particles:
#         particle.pos[0] += random.randint(-1, 1)
#         particle.pos[1] -= 0.3
#         particle.size[0] -= 0.02
#         particle.size[1] -= 0.02

#         # Remove particles if their size becomes 0
#         if particle.size == [0, 0]:
#             particles.remove(particle)

#         particle.draw(screen) 
#         # Adding the Glow effect
#         glow_rect = pygame.Rect(tuple(particle.pos), ((particle.size[0] + (particle.size[0] / 2),
#                  (particle.size[1] + (particle.size[1] / 2)))))

#         screen.blit(glow_surface(particle.size, [25, 25, 25], glow_rect),
#                     tuple(particle.pos),
#                     special_flags=BLEND_RGB_ADD)

'''


