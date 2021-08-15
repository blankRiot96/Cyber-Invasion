import pygame


class SpriteSheet():
    def __init__(self, image, width, height, bg=None):
        self.sheet = image
        self.extract = []
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.sheet, (0, 0))
        img.set_colorkey(bg)

        self.sheet = img

    def get_images(self, rows, columns, width, height, bg=None):
        images = []
        fixer = 8

        for i in range(rows):
            for e in range(columns):
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(self.sheet, (0, 0), ((e * width), ((i*fixer) * columns), width, height))
                image.set_colorkey(bg)

                self.extract.append(image)
                images.append(image)
                
        return images

    def scaler(self, extract, width, height):
        scaled = []

        for i in extract:
            scaled.append(pygame.transform.scale(i, (width, height)))

        return scaled

    def turn_left(self):
        left_images = []

        for i in self.extract:
            left_images.append(pygame.transform.flip(i, True, False))

        return left_images
