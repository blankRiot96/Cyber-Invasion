import pygame
from pygame.locals import *
from src.spritesheet import SpriteSheet

path = 'src/images/'

# Player sprites
player_run_img = pygame.image.load(path + 'player_run.png').convert_alpha()
player_run_spritesheet = SpriteSheet(player_run_img, 256, 256, bg=(0, 0, 0))
player_run = player_run_spritesheet.get_images(8, 8, 32, 32, fixer=4)
player_run = player_run_spritesheet.scaler(player_run, 32*1.5, 32*1.5)

player_idle_img = pygame.image.load(path + 'player_idle.png').convert_alpha()
player_idle_spritesheet = SpriteSheet(player_idle_img, 64, 256, bg=(0, 0, 0))
player_idle = player_idle_spritesheet.get_images(8, 2, 32, 32, fixer=16)
player_idle = player_idle_spritesheet.scaler(player_idle, 32*1.5, 32*1.5)

'''
Player movements:
ur = Up + Right
dr = Down + Right
ul = Up + Left
dl = Down + Left
'''
# Forward/Backward
player_run_forward = player_run[0:8 ]
player_run_backward = player_run[32:32+8 ]

# Right movements
player_run_ur = player_run[8 :8+8 ]
player_run_right = player_run[16 :16+8 ]
player_run_dr = player_run[24 : 24+8 ]

# Left movements
player_run_dl = player_run[40 :48 ]
player_run_left = player_run[48 :48+8 ]
player_run_ul = player_run[56 :64 ]

player_movements = [
    player_run_forward,
    player_run_backward,
    player_run_right,
    player_run_left,
    player_run_dr,
    player_run_dl,
    player_run_ur,
    player_run_ul
]

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
    "uo + right": player_idle_ul
}

# Block sprite
block_size = 60
block_img = pygame.image.load(path + 'block1.png').convert_alpha()
block = pygame.transform.scale(block_img, (60, 60))
