from src.sprites import shadow_img


class Shadow:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.last_registered = []


    def update(self, coord: list, jumping: bool) -> tuple:
        if not jumping:
            self.x, self.y = coord
        else:
            self.x, self.y = self.last_registered

        self.last_registered = [self.x, self.y]
        return self.x, self.y


    def draw(self, screen) -> None:
        screen.blit(shadow_img, (self.x + 14, self.y + 36))

