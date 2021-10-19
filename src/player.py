import pygame
import math
from src.display import screen_width, screen_height
from src.sprites import (
    player_run_forward,
    player_run_backward,
    player_run_right,
    player_run_left,
    player_run_dr,
    player_run_dl,
    player_run_ur,
    player_run_ul,

    player_jumping,
    player_idling,
    player_scale
)
from src.shadow import Shadow
from src.bullet import Bullet

shadow = Shadow()


class Player:
    def __init__(self, coord: list, screen) -> None:
        # Screen to blit on
        self.screen = screen

        # World attributes
        self.x = 0
        self.y = 0

        # Player attributes
        self.coord = coord
        self.rect = pygame.Rect(*self.coord, 32 * player_scale, 32 * player_scale)

        self.shadow_coord = list(coord)
        self.direction = ""
        self.speed = 1.2

        # Handling shooting variables
        self.bullets = []

        # Jump variables
        self.jump = False
        self.gravity = 2.2
        self.cool_down = 115
        self.dy = 0

        # Variable to determine which stage of jumping the Player is in
        self.stage = 0

        # Jump variable to determine if finished going up
        self.finished = False

        # Delta time variable for frame rate independence
        self.dt = 0

        # Variable for idling in last position
        self.last_direction = "forward"

        # Index Variable
        self.index = 0

    def update(self, blocks, dt) -> dict[str, list[dict[str, list[int]]]]:
        self.dt = dt
        key = pygame.key.get_pressed()
        pressed1 = [key[pygame.K_RIGHT], key[pygame.K_LEFT], key[pygame.K_UP], key[pygame.K_DOWN]]
        pressed2 = [key[pygame.K_d], key[pygame.K_a], key[pygame.K_w], key[pygame.K_s]]

        self.x = 0
        self.y = 0

        # Key inputs: Getting what key is being pressed by user
        if [True, False, False, False] in [pressed1, pressed2]:
            self.direction = "right"
            self.last_direction = "right"
        elif [False, True, False, False] in [pressed1, pressed2]:
            self.direction = "left"
            self.last_direction = "left"
        elif [False, False, True, False] in [pressed1, pressed2]:
            self.direction = "forward"
            self.last_direction = "forward"
        elif [False, False, False, True] in [pressed1, pressed2]:
            self.direction = "backward"
            self.last_direction = "backward"
        elif [True, False, False, True] in [pressed1, pressed2]:
            self.direction = "down + right"
            self.last_direction = "down + right"
        elif [True, False, True, False] in [pressed1, pressed2]:
            self.direction = "up + right"
            self.last_direction = "up + right"
        elif [False, True, False, True] in [pressed1, pressed2]:
            self.direction = "down + left"
            self.last_direction = "down + left"
        elif [False, True, True, False] in [pressed1, pressed2]:
            self.direction = "up + left"
            self.last_direction = "up + left"
        else:
            self.direction = ""

        # Determining direction for player movement
        movement_direction = [self.direction]
        if self.direction == "down + right":
            movement_direction = ["backward", "right"]
        elif self.direction == "up + right":
            movement_direction = ["forward", "right"]
        elif self.direction == "down + left":
            movement_direction = ["backward", "left"]
        elif self.direction == "up + left":
            movement_direction = ["forward", "left"]

        # Updating players position
        if "right" in movement_direction:
            self.x -= self.speed
        if "left" in movement_direction:
            self.x += self.speed
        if "forward" in movement_direction:
            self.y += self.speed
        if "backward" in movement_direction:
            self.y -= self.speed

        # Diagonal movement: Multiplying by certain value to cause perfect diagonal
        # Diagonal movement maintains same speed as other directions.
        if self.x != 0 and self.y != 0:
            self.x *= math.sqrt(2) / 2
            self.y *= math.sqrt(2) / 2

        # Jump and shadow control
        if self.jump:
            self.y = self.player_jump(self.y)
        else:
            self.shadow_coord = list(self.coord)
            self.stage = 0

        # Updating map,
        # Causing moving background effect
        for block in blocks['objects']:
            for name in block:
                block[name][0] += self.x * dt
                block[name][1] += self.y * dt

        return blocks

    def create_new_bullet(self, mx, my) -> str:
        x, y = self.rect.center
        self.bullets.append(bullet := Bullet(x, y, 7, mx, my))

        return bullet.direction

    def shoot(self) -> None:
        for circle in self.bullets:
            circle.update(self.dt)
            circle.draw(self.screen)

            conditions = [circle.x > screen_width, circle.x < 0, circle.y > screen_height, circle.y < 0]
            if conditions[0] or conditions[1] or conditions[2] or conditions[3]:
                self.bullets.remove(circle)

    def player_jump(self, y):
        if not self.finished:
            y = self.jump_up(y)
        else:
            y = self.jump_down(y)

        return y

    def jump_up(self, y):
        if self.dy < self.cool_down:
            self.dy += self.gravity
            y += self.gravity
            self.shadow_coord[1] += self.gravity * self.dt

            self.gravity -= 0.01
        else:
            self.finished = True
            self.dy = 0

        return y

    def jump_down(self, y):
        if self.dy > -self.cool_down:
            self.dy -= self.gravity
            y -= self.gravity
            self.shadow_coord[1] -= self.gravity * self.dt

            self.gravity += 0.01
        else:
            self.finished = False
            self.jump = False
            self.dy = 0

        return y

    def update_index(self, speed: float = 1):
        if not self.jump:
            self.index += speed * self.dt
        else:
            self.index += 1

    def catch_index(self, movement):
        try:
            movement[int(self.index)]
        except IndexError:
            self.index = 0

    def jump_staging(self):
        if self.stage <= 1:  # Leap
            if self.dy <= 20:
                if self.dy == 1:
                    self.update_index()
            elif self.dy <= 50:
                if self.dy == 19:
                    self.update_index()
            else:
                self.stage = 2  # Max Height going up
        elif self.stage == 2:
            if self.dy <= self.cool_down:
                if self.dy == 199:
                    self.update_index()
            else:
                self.stage = 3  # Max height dropping down
        elif self.stage == 3:
            if 200 <= self.dy < 30:
                if self.dy == self.cool_down - 1:
                    self.update_index()
            else:
                self.stage = 4  # Landing
        elif self.stage == 4:
            if 30 <= self.dy < 20:
                if self.dy == 29:
                    self.update_index()
            elif 20 <= self.dy < 10:
                if self.dy == 19:
                    self.update_index()
            elif 10 <= self.dy:
                if self.dy == 9:
                    self.update_index()

    def draw_jump(self):
        try:
            jump_d = player_jumping[self.direction]
        except KeyError:
            jump_d = player_jumping[self.last_direction]

        self.jump_staging()
        self.catch_index(jump_d)

        self.screen.blit(jump_d[self.stage], tuple(self.coord))

    def idle(self):
        self.update_index(0.06)
        idle_d = player_idling[self.last_direction]
        self.catch_index(idle_d)

        self.screen.blit(idle_d[int(self.index)], tuple(self.coord))

    def right(self):
        self.update_index(0.1)
        self.catch_index(player_run_right)
        self.screen.blit(player_run_right[int(self.index)], tuple(self.coord))

    def left(self):
        self.update_index(0.1)
        self.catch_index(player_run_left)
        self.screen.blit(player_run_left[int(self.index)], tuple(self.coord))

    def forward(self):
        self.update_index(0.1)
        self.catch_index(player_run_forward)
        self.screen.blit(player_run_forward[int(self.index)], tuple(self.coord))

    def backward(self):
        self.update_index(0.1)
        self.catch_index(player_run_backward)
        self.screen.blit(player_run_backward[int(self.index)], tuple(self.coord))

    def dr(self):
        self.update_index(0.1)
        self.catch_index(player_run_dr)
        self.screen.blit(player_run_dr[int(self.index)], tuple(self.coord))

    def ur(self):
        self.update_index(0.1)
        self.catch_index(player_run_ur)
        self.screen.blit(player_run_ur[int(self.index)], tuple(self.coord))

    def dl(self):
        self.update_index(0.1)
        self.catch_index(player_run_dl)
        self.screen.blit(player_run_dl[int(self.index)], tuple(self.coord))

    def ul(self):
        self.update_index(0.1)
        self.catch_index(player_run_ul)
        self.screen.blit(player_run_ul[int(self.index)], tuple(self.coord))

    def draw(self) -> None:
        shadow.draw(self.screen, *self.shadow_coord)

        if not self.jump:
            match self.direction:
                case "right":
                    self.right()
                case "left":
                    self.left()
                case "forward":
                    self.forward()
                case "backward":
                    self.backward()
                case "down + right":
                    self.dr()
                case "up + right":
                    self.ur()
                case "down + left":
                    self.dl()
                case "up + left":
                    self.ul()
                case "":
                    self.idle()
        else:
            self.draw_jump()

        # match_cases = {
        #     "right": self.right,
        #     "left": self.left,
        #     "forward": self.forward,
        #     "backward": self.backward,
        #     "down + right": self.dr,
        #     "up + right": self.ur,
        #     "down + left": self.dl,
        #     "up + left": self.ul,
        #     "": self.idle
        # }
        #
        # if not self.jump:
        #     match_cases[self.direction]()
        # else:
        #     self.draw_jump()
