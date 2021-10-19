import pygame

pygame.init()

clock = pygame.time.Clock()

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode(
    (screen_width, screen_height), pygame.SCALED | pygame.RESIZABLE
)
pygame.display.set_caption("Cyber Invasion")

pygame.mouse.set_visible(False)
