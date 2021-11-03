import pygame


class ExpandingCircle:
    def __init__(self, pos: tuple[int, int], init_radius, max_radius, increment: float, colour: tuple[int, int, int]):
        self.pos = pos
        self.radius = init_radius
        self.max_radius = max_radius
        self.increment = increment
        self.colour = colour
        self.width = 10

        self.cool_down = 7
        self.count = 0

    def draw(self, screen, dt):
        self.count += dt
        if self.radius <= self.max_radius:
            self.radius += self.increment * dt

            if self.count >= self.cool_down:
                self.width -= 1

            # Make sure that width is valid value for circle
            if self.width <= 0:
                self.width = 1

            pygame.draw.circle(screen, self.colour, self.pos, self.radius, width=self.width)
