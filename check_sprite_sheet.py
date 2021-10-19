import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Sheet Preview')

'''Sprite Sheet'''
from src.sprites import bee_bot
sprite_sheet = bee_bot
attributes = {
    "size": 40,
    "sprite sheet": sprite_sheet,
    "rows": 8,
    "columns": 1
}


# Define colours
bg = (0, 0, 0)
white = (255, 255, 255)


def draw_grid(size, rows):
    for line in range(rows):
        pygame.draw.line(screen, white, (0, line * size), (screen.get_width(), line * size))
        pygame.draw.line(screen, white, (line * size, 0), (line * size, screen.get_height()))


def check_sprite_sheet(size: float, sprites: list[pygame.Surface], rows: int, columns: int, space: float = 20) -> None:
    size += space
    index = 0

    width = int(size * columns)
    height = int(size * rows)
    pygame.display.set_mode((width, height))

    draw_grid(size, rows)
    for row in range(rows):
        for column in range(columns):
            screen.blit(sprites[index], (column * size, row * size))
            index += 1


run = True
while run:

    clock.tick(fps)

    # Draw background
    screen.fill(bg)
    check_sprite_sheet(*list(attributes.values()))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
