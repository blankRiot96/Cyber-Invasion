from src.sprites import shadow_img


class Shadow:
    def draw(self, screen, x, y) -> None:
        screen.blit(shadow_img, (x + 14, y + 36))
