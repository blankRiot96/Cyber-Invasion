import pygame
import math
from src.sprites import (
    player_run_forward,
    player_run_backward,
    player_run_right,
    player_run_left,
    player_run_dr,
    player_run_dl,
    player_run_ur,
    player_run_ul,

    player_idling,
)
from src.diff_val import *
from src.shadow import Shadow

shadow = Shadow(200, 200)


class Player:
    def __init__(self, coord: list) -> None:
        self.x = 0
        self.y = 0
        self.coord = coord
        self.direction = ""
        self.speed = 1.2
        self.jump = False
        self.dy = 0

        # Variable for idling in last position
        self.last_direction = "forward"

        # Index Variable
        self.index = 0


    def update(self, blocks, dt) -> dict:
        key = pygame.key.get_pressed()
        pressed1 = [key[pygame.K_RIGHT], key[pygame.K_LEFT], key[pygame.K_UP], key[pygame.K_DOWN]]        
        pressed2 = [key[pygame.K_d], key[pygame.K_a], key[pygame.K_w], key[pygame.K_s]]

        self.x = 0
        self.y = 0

        if [True, False, False, False] in [pressed1, pressed2]:
            self.direction = "right"
            self.last_direction = "right"
            self.update_index(0.1*dt)
        elif [False, True, False, False] in [pressed1, pressed2]:
            self.direction = "left"
            self.last_direction = "left"
            self.update_index(0.1*dt)
        elif [False, False, True, False] in [pressed1, pressed2]:
            self.direction = "forward"
            self.last_direction = "forward"
            self.update_index(0.1*dt)
        elif [False, False, False, True] in [pressed1, pressed2]:
            self.direction = "backward"
            self.last_direction = "backward"
            self.update_index(0.1*dt)
        elif [True, False, False, True] in [pressed1, pressed2]:
            self.direction = "down + right"
            self.last_direction = "down + right"
            self.update_index(0.1*dt)
        elif [True, False, True, False] in [pressed1, pressed2]:
            self.direction = "up + right"
            self.last_direction = "up + right"
            self.update_index(0.1*dt)
        elif [False, True, False, True] in [pressed1, pressed2]:
            self.direction = "down + left"
            self.last_direction = "down + left"
            self.update_index(0.1*dt)
        elif [False, True, True, False] in [pressed1, pressed2]:
            self.direction = "up + left"
            self.last_direction = "up + left"
            self.update_index(0.1*dt)
        else:
            self.direction = ""
            self.update_index(0.06*dt)

        movement_direction = [self.direction]
        if self.direction == "down + right":
            movement_direction = ["backward", "right"]
        elif self.direction == "up + right":
            movement_direction = ["forward", "right"]
        elif self.direction == "down + left":
            movement_direction = ["backward", "left"]
        elif self.direction == "up + left":
            movement_direction = ["forward", "left"]


        if "right" in movement_direction:
            self.x -= self.speed 
        if "left" in movement_direction:
            self.x += self.speed 
        if "forward" in movement_direction:
            self.y += self.speed 
        if "backward" in movement_direction:
            self.y -= self.speed 

        if self.x != 0 and self.y != 0:
            self.x *= math.sqrt(2)/2
            self.y *= math.sqrt(2)/2


        if self.jump:
            self.y = self.player_jump(self.y)
        
        for block in blocks['objects']:
            for name in block:
                block[name][0] += self.x * dt
                block[name][1] += self.y * dt
            
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


    def player_jump(self, y):
        down = ["down + left", "down + right", "backward"]
        cooldown = 200
        speed = 2
        condition = self.direction in down

        if condition:
            y = self.jump_down(y, speed, cooldown)
        else:
            y = self.jump_up(y, speed, cooldown)

        return y

    def jump_down(self, y, speed, cooldown):
        if self.dy > -(cooldown):
            self.dy -= speed
            y -= speed
        else:
            y = self.jump_up(y, speed, cooldown)
            self.jump = False
            self.dy = 0

        return y

    def jump_up(self, y, speed, cooldown):
        if self.dy < cooldown:
            self.dy += speed
            y += speed
        else:
            self.jump_down(y, speed, cooldown)
            self.jump = False
            self.dy = 0

        return y


    def right(self, screen):
        self.catch_index(player_run_right)
        screen.blit(player_run_right[int(self.index)], tuple(self.coord))


    def left(self, screen):
        self.catch_index(player_run_left)
        screen.blit(player_run_left[int(self.index)], tuple(self.coord))


    def forward(self, screen):
        self.catch_index(player_run_forward)
        screen.blit(player_run_forward[int(self.index)], tuple(self.coord))

    def backward(self, screen):
        self.catch_index(player_run_backward)
        screen.blit(player_run_backward[int(self.index)], tuple(self.coord))

    def dr(self, screen):
        self.catch_index(player_run_dr)
        screen.blit(player_run_dr[int(self.index)], tuple(self.coord))

    def ur(self, screen):
        self.catch_index(player_run_ur)
        screen.blit(player_run_ur[int(self.index)], tuple(self.coord))

    def dl(self, screen):
        self.catch_index(player_run_dl)
        screen.blit(player_run_dl[int(self.index)], tuple(self.coord))

    def ul(self, screen):
        self.catch_index(player_run_ul)
        screen.blit(player_run_ul[int(self.index)], tuple(self.coord))


    def draw(self, screen) -> None:
        shadow.update(self.coord, self.jump)
        shadow.draw(screen)

        if self.direction == "right":
            self.right(screen)
        elif self.direction == "left":
            self.left(screen)
        elif self.direction == "forward":
            self.forward(screen)
        elif self.direction == "backward":
            self.backward(screen)
        elif self.direction == "down + right":
            self.dr(screen)
        elif self.direction == "up + right":
            self.ur(screen)
        elif self.direction == "down + left":
            self.dl(screen)
        elif self.direction == "up + left":
            self.ul(screen)
        elif self.direction == "":
            self.idle(screen)
        
