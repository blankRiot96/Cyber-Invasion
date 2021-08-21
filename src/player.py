import pygame


class Player:
    def __init__(self, coord: list) -> None:
        self.coord: list = coord

    def update(self) -> None:
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            print('Moving Right')


