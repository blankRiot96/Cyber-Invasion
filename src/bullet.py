import pygame
import math

from src.sprites import bullet_img, bullet_size


def get_direction(degrees: int) -> str:
    """World is upside down."""
    direction = ""

    # Upward side of protractor
    if degrees in range(20, -20, -1):
        direction = "right"
    elif degrees in range(-20, -70, -1):
        direction = "up + right"
    elif degrees in range(-70, -110, -1):
        direction = "forward"
    elif degrees in range(-110, -150, -1):
        direction = "up + left"

    # Downward side of protractor
    elif degrees in range(20, 70):
        direction = "down + right"
    elif degrees in range(70, 110):
        direction = "backward"
    elif degrees in range(110, 150):
        direction = "down + left"
    elif degrees in range(180, -180, -1):
        direction = "left"

    return direction


class Bullet:
    def __init__(self, start_x, start_y, speed: float, target_x, target_y) -> None:
        self.image = bullet_img
        self.x = start_x
        self.y = start_y
        self.rect = pygame.Rect(self.x, self.y, bullet_size, bullet_size)
        self.speed = speed
        self.target_x = target_x
        self.target_y = target_y

        # Getting the angle in radians
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.degrees = self.angle * 57.2958

        # Using degrees to determine player direction
        self.direction = get_direction(int(self.degrees))

        # Change in x and y
        self.dx = 0
        self.dy = 0

        # Calculating how much the bullet has moved
        self.distance = 0

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

        # Increasing amount moved
        self.distance += math.sqrt((self.dx**2) + (self.dy**2))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
