import pygame
from pygame.locals import *
from src.spritesheet import SpriteSheet

path = 'src/images/'

# Player sprites
player_sprite_ss = pygame.image.load(path + 'spritesheet.png').convert_alpha()
player_sprite = SpriteSheet(player_sprite_ss, 32, 32)
player = player_sprite.get_images(2, 2, 16, 16)
player = player_sprite.scaler(player, 60, 60)

# Block sprite
block_img = pygame.image.load(path + 'block.png').convert_alpha()
block = pygame.transform.scale(block_img, (150, 150))
