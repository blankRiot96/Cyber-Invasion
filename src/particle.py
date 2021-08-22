import pygame

class Particle:
    def __init__(self, pos: list, color:list, size: list) -> None:
        self.pos = pos
        self.size = size
        self.color = color

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, tuple(self.color), pygame.Rect(tuple(self.pos), tuple(self.size)))


