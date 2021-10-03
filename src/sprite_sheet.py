import pygame
from typing import List


class SpriteSheet:
    def __init__(self, image: pygame.Surface, width: float, height: float, bg: tuple[int, int, int] = (0, 0, 0)):
        self.bg = bg
        self.extract = []
        self.sheet = image

        # Width of each sprite NOT sprite sheet
        self.width, self.height = 0, 0

        if bg:
            img = pygame.Surface((width, height)).convert_alpha()
            img.blit(self.sheet, (0, 0))
            img.set_colorkey(bg)

            self.sheet = img

    def get_images(self, rows: int, columns: int, width: float, height: float, fixer: int):
        self.width = width
        self.height = height

        images = []

        for i in range(rows):
            for e in range(columns):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(self.sheet, (0, 0), pygame.Rect((e * width), ((i * fixer) * columns), width, height))
                image.set_colorkey(self.bg)

                self.extract.append(image)
                images.append(image)

        return images

    def resize(self, extract: List[pygame.Surface], width: float, height: float):
        scaled = []
        width = int(width)
        height = int(height)

        for i in extract:
            img = pygame.transform.scale(i, (width, height))
            img.set_colorkey(self.bg)

            scaled.append(img)

        return scaled

    def turn_left(self):
        left_images = []

        for i in self.extract:
            img = pygame.Surface((self.width, self.height)).convert_alpha()
            img.blit(i, (0, 0))
            img.set_colorkey(self.bg)

            left_images.append(pygame.transform.flip(img, True, False))

        return left_images
