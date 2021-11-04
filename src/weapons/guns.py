import pygame

from src.bullet import Bullet
from src.generic_types import Position
from src.sprites import blaster_img


class Blaster:
    def __init__(self, bullet_speed, shot_cool_down, max_bullets, reload_speed, _range, screen: pygame.Surface):
        """
        :param bullet_speed: Speed at which bullet must move
        :param shot_cool_down: Cool down between generation of bullets
        :param max_bullets: Maximum capacity
        :param reload_speed: Reload Speed
        """
        self.coord = [0, 0]
        self.bullet_speed = bullet_speed
        self.shot_cool_down = shot_cool_down
        self.max_bullets = max_bullets
        self.reload_speed = reload_speed
        self._range = _range
        self.direction = ""

        self.count = 0

        self.bullets = []
        self.screen = screen

    def create_new_bullet(self, player_pos: Position, mx, my):
        self.bullets.append(bullet := Bullet(*player_pos, self.bullet_speed, mx, my))

        return bullet.direction

    def update(self, player_rect: pygame.Rect, mouse_pos, dt):
        self.count += dt

        self.coord = list(player_rect.center)
        # Creating bullets
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            if self.count >= self.shot_cool_down:
                self.direction = self.create_new_bullet(player_rect.center, *mouse_pos)
                self.count = 0

        # Updating bullets
        for bullet in self.bullets:
            bullet.update(dt)
            bullet.draw(self.screen)

            # Removing bullets
            if bullet.distance >= self._range:
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.blit(blaster_img, self.coord)


