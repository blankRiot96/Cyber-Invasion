import pygame
import random

bg_count = 0
lines = []
def background_1(screen, color, dt):
    global bg_count
    bg_count += dt

    # Cooldown to create new line
    if bg_count >= 10:
        print('DEBUG: new line')
        x, y = random.randint(0, 1100), random.randint(0, 250)
        lines.append([x, y])
        bg_count = 0

    for line in lines:
        x = line[0]
        y = line[1]

        # Updating pos
        line[1] += 2 * dt

        # Rendering
        pygame.draw.line(screen, color, tuple(line), (x, y+30))

        if y > 600:
            print('DEBUG: remove line')
            lines.remove(line)
