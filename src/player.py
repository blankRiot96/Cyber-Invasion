import pygame
from src.sprites import (
    player_run_forward,
    player_run_backward,
    player_run_right,
    player_run_left,
    player_run_dr,
    player_run_dl,
    player_run_ur,
    player_run_ul,

    player_idling
)


class Player:
    def __init__(self, coord: list) -> None:
        self.coord = coord
        self.direction = ""

        # Variable for idling in last position
        self.last_direction = "forward"

        # Index Variable
        self.index = 0


    def update(self, blocks, dt) -> dict:
        key = pygame.key.get_pressed()
        pressed = [key[pygame.K_RIGHT], key[pygame.K_LEFT], key[pygame.K_UP], key[pygame.K_DOWN]]

        if pressed == [True, False, False, False]:
            self.direction = "right"
            self.last_direction = "right"
            self.update_index(0.1*dt)
        elif pressed == [False, True, False, False]:
            self.direction = "left"
            self.last_direction = "left"
            self.update_index(0.1*dt)
        elif pressed == [False, False, True, False]:
            self.direction = "forward"
            self.last_direction = "forward"
            self.update_index(0.1*dt)
        elif pressed == [False, False, False, True]:
            self.direction = "backward"
            self.last_direction = "backward"
            self.update_index(0.1*dt)
        else:
            self.direction = ""


        for block in blocks['objects']:
            for name in block:
                if self.direction == "right":
                    block[name][0] -= 0.5
                elif self.direction == "left":
                    block[name][0] += 0.5
                elif self.direction == "forward":
                    block[name][1] -= 0.5
                elif self.direction == "backward":
                    block[name][1] += 0.5

        return blocks


    def update_index(self, speed):
        self.index += speed
    

    def catch_index(self, movement):
        try:
            movement[int(self.index)]
        except:
            self.index = 0


    def idle(self, screen):
        idle_d = player_idling[self.last_direction]
        try:
            idle_d[int(self.index)]
        except:
            self.index = 0
        screen.blit(idle_d[int(self.index)], tuple(self.coord))


    def right(self, screen):
        self.catch_index(player_run_right)
        screen.blit(player_run_right[int(self.index)], tuple(self.coord))


    def left(self, screen):
        self.catch_index(player_run_left)
        screen.blit(player_run_left[int(self.index)], tuple(self.coord))


    def forward(self, screen):
        self.catch_index(player_run_forward)
        screen.blit(player_run_forward[int(self.index)], tuple(self.coord))

    def draw(self, screen) -> None:
        if self.direction == "right":
            self.right(screen)
        elif self.direction == "left":
            self.left(screen)
        elif self.direction == "":
            self.idle(screen)
    
