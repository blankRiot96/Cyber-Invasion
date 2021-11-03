import pygame
from src.generic_types import Position, Size, Colour


# Fonts
comic_sans_ms = pygame.font.SysFont('comicsansms', 24)


class Button:
    def __init__(self, text: str, pos: Position, size: Size, text_colour: Colour, colour: Colour | list[int, int, int]):
        self.text = text
        self.font = pygame.font.SysFont('comicsansms', size[1] - 10)
        self.title = self.font.render(self.text, True, text_colour)

        self.pos = pos
        self.size = size
        self.colour = tuple(colour)
        self.rect = pygame.Rect(pos, size)

        self.opacity = 155

    def hover(self, mouse_pos: Position) -> bool:
        return self.rect.collidepoint(*mouse_pos)

    def draw(self, screen, mouse_pos: Position) -> None:
        if self.hover(mouse_pos):
            self.opacity = 255
        else:
            self.opacity = 155

        pygame.draw.rect(screen, (*self.colour, self.opacity), self.rect, border_radius=3)
        screen.blit(self.title, self.pos)
