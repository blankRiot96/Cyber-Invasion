import pygame
from pygame.locals import *
from src.spritesheet import SpriteSheet

path = 'src\images\\'

# Player sprites
player_sprite_ss = pygame.image.load(path + 'player-torso-idle-gun-full.png').convert_alpha()
player_sprite = SpriteSheet(player_sprite_ss, 16*10, 19, bg=(0, 0, 0))
player = player_sprite.get_images(1, 10, 16, 19)
player = player_sprite.scaler(player, 60, 60)

# Block sprite
block_size = 60
block_img = pygame.image.load(path + 'block.png').convert_alpha()
block = pygame.transform.scale(block_img, (60, 60))
