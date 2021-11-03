import pygame
import math
import random
from src.display import screen_width, screen_height
from src.sprites import bee_bot_moving, bee_bot_size


class BeeBot:
    def __init__(self, speed, player_pos: list[int, int]):
        self.x = random.randrange(0, screen_width)
        self.y = random.randint(0, screen_height)

        self.speed = speed
        self.target_x, self.target_y = player_pos

        self.rect = pygame.Rect(self.x, self.y, bee_bot_size, bee_bot_size)
        self.image = bee_bot_moving['left']

        # Getting the angle in radians
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)

        # Finding by how much to update player x and y to reach target
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed

    def update(self, dt):
        # Update bee bot pos by dx and dy
        self.x += self.dx * dt
        self.y += self.dy * dt

        # Update rectangle
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


