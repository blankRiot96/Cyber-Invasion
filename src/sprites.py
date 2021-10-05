import pygame
from pygame.locals import *
from src.sprite_sheet import SpriteSheet

path = 'assets/images/'

'''Player Sprites'''
player_scale = 1.5

# Sprite sheets
player_run_img = pygame.image.load(path + 'player_run.png').convert_alpha()
player_run_sprite_sheet = SpriteSheet(player_run_img, 256, 256)
player_run = player_run_sprite_sheet.get_images(8, 8, 32, 32, fixer=4)
player_run = player_run_sprite_sheet.resize(player_run, 32 * player_scale, 32 * player_scale)

player_idle_img = pygame.image.load(path + 'player_idle.png').convert_alpha()
player_idle_sprite_sheet = SpriteSheet(player_idle_img, 64, 256)
player_idle = player_idle_sprite_sheet.get_images(8, 2, 32, 32, fixer=16)
player_idle = player_idle_sprite_sheet.resize(player_idle, 32 * player_scale, 32 * player_scale)

player_jump_img = pygame.image.load(path + 'player-jump_40x40.png').convert_alpha()
player_jump_sprite_sheet = SpriteSheet(player_jump_img, 280, 320)
player_jump = player_jump_sprite_sheet.get_images(8, 7, 40, 40, fixer=5.7)
player_jump = player_jump_sprite_sheet.resize(player_jump, 40 * player_scale, 40 * player_scale)

'''
Player movements:
ur = Up + Right
dr = Down + Right
ul = Up + Left
dl = Down + Left
'''
# Forward/Backward
player_run_forward = player_run[0:8]
player_run_backward = player_run[32:32 + 8]

# Right movements
player_run_ur = player_run[8:8 + 8]
player_run_right = player_run[16:16 + 8]
player_run_dr = player_run[24: 24 + 8]

# Left movements
player_run_dl = player_run[40:48]
player_run_left = player_run[48:48 + 8]
player_run_ul = player_run[56:64]

# Player idle
player_idle_forward = player_idle[0:2]
player_idle_ur = player_idle[2:4]
player_idle_right = player_idle[4:6]
player_idle_dr = player_idle[6:8]
player_idle_backward = player_idle[8:10]
player_idle_dl = player_idle[10:12]
player_idle_left = player_idle[12:14]
player_idle_ul = player_idle[14:16]

player_idling = {
    "backward": player_idle_backward,
    "up + right": player_idle_ur,
    "right": player_idle_right,
    "down + right": player_idle_dr,
    "forward": player_idle_forward,
    "down + left": player_idle_dr,
    "left": player_idle_left,
    "up + left": player_idle_ul
}

# Player jump
player_jumping = {
    "forward": player_jump[0:7],
    "up + right": player_jump[7:14],
    "right": player_jump[14:21],
    "down + right": player_jump[21:28],
    "backward": player_jump[28:35],
    "down + left": player_jump[35:42],
    "left": player_jump[42: 49],
    "up + left": player_jump[49:56]
}

# Block sprite
block_size = 60
block_img = pygame.image.load(path + 'block1.png').convert_alpha()
block = pygame.transform.scale(block_img, (block_size, block_size))

# Shadow
shadow_size = 20
shadow_img = pygame.image.load(path + 'shadow.png').convert_alpha()
shadow_img = player_run_sprite_sheet.resize([shadow_img], shadow_size, shadow_size)[0]
