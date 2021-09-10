import pygame
from pygame.locals import *
import sys

from json import load
import time

'''Main Display and setup'''
pygame.init()

clock = pygame.time.Clock()

screen_width = 1100
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption('Cyber Invasion')


'''Importing necessary componenets from SRC'''
# Background
from src.backgrounds import background_1

# World
from src.world import load_world, draw_world, draw_fun

# Border
from src.border import draw_border, return_color

# Player
from src.player import Player


def check_spritesheets(images, size):
    for i in range(len(images)):
        screen.blit(images[i], (i*size, 200))

'''Pre loading game elements'''
blocks = load_world('playground')
player = Player([200, 200])

'''Variables for the Game'''
# Define colours
bg = (0, 0, 0)

# Game Variables
index = 0
start = time.time()

count = 100  # Count var

x_dif = 450 - 350
y_dif = 25
grid = 10

# Border variables
particles = []
color = [0, 0, 0]
direction = "up"


'''Main Loop'''
run = True
while run:
    clock.tick()

    # Time for each iteration
    end = time.time()

    dt = end - start
    dt *= 100
    count += dt
    if count >= 100000:
        count = 100

    start = time.time()

    # Rendering
    # Draw background
    screen.fill(bg)
    draw_world(screen, blocks)
    blocks = player.update(blocks, dt)
    player.draw(screen)

    # check_spritesheets(player_run_right, 32)

    color, direction = return_color(color, direction, dt)
    draw_border(screen, particles, tuple(color), dt)

    # FPS
    

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

sys.exit()
