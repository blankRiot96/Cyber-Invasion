import pygame
import sys
import time

"""Importing necessary components from SRC"""
from src.display import *
from src.sprites import cursor
from src.world import load_world, draw_world
from src.border import draw_border, return_color
from src.player import Player
from src.enemies.bee_bot import BeeBot


def main():
    """Pre loading game elements"""
    blocks = load_world("playground")
    player = Player([550, 300], screen)
    bees = []

    """Variables for the Game"""
    # Define colours
    bg = (0, 0, 0)

    # Game Variables
    bullet_direction = "forward"
    bee_generation_cool_down = 200
    start = time.time()

    # Count variables
    fire_rate = 0
    bee_rate = 0

    # Border variables
    particles = []
    color = [0, 0, 0]
    direction = "up"

    run = True
    # Main Loop
    while run:
        clock.tick()
        pygame.display.set_caption(f"Cyber Invasion ({int(clock.get_fps())})")

        # Time for each iteration
        end = time.time()

        dt = end - start
        dt *= 100

        # Update count variables
        fire_rate += dt
        bee_rate += dt

        start = time.time()

        # Rendering
        # Draw background
        screen.fill(bg)
        draw_world(screen, blocks)

        # Updating blocks and drawing player
        blocks = player.update(blocks, dt)
        mx, my = pygame.mouse.get_pos()
        # Check for mouse input
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            if fire_rate >= 40:
                bullet_direction = player.create_new_bullet(mx, my)
                fire_rate = 0
        player.shoot()

        # Generating Bees
        if bee_rate >= bee_generation_cool_down:
            bees.append(BeeBot(1, player.coord))
            bee_rate = 0

        # Drawimg bee bots and checking if shot by bullet
        for bee in bees:
            bee.update(dt)
            bee.draw(screen)

            #  Checking for collision between bullet and bee bot
            for bullet in player.bullets:
                if bullet.rect.colliderect(bee.rect):
                    bees.remove(bee)

        # Drawing Player
        if len(player.bullets) >= 1:
            player.direction, player.last_direction = bullet_direction, bullet_direction
        player.draw()

        # Setting colour and drawing border
        color, direction = return_color(color, direction, dt)
        draw_border(screen, particles, tuple(color), dt)

        # Draw Cursor
        screen.blit(cursor, (mx, my))

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump = True

        pygame.display.update()

    sys.exit()


if __name__ == "__main__":
    main()
