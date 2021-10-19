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

        self.dx = 0
        self.dy = 0

    def update(self, dt):
        # Finding by how much to update player x and y to reach target
        self.dx = math.cos(self.angle) * self.speed * dt
        self.dy = math.sin(self.angle) * self.speed * dt

        # Update player pos by dx and dy
        self.x += self.dx
        self.y += self.dy

        # Update rectangle
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))


