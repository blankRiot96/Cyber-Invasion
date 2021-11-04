import pygame
from pygame.locals import *
from src.sprite_sheet import SpriteSheet


def scale_image(img: pygame.Surface, width: int, height: int) -> pygame.Surface:
    surf = pygame.Surface((width, height))
    scaled_img = pygame.transform.scale(img, (width, height))
    surf.blit(scaled_img, (0, 0))
    surf.set_colorkey((0, 0, 0))

    return surf


path = "assets/images/"

"""Player Sprites"""
player_scale = 1.5

# Sprite sheets
player_run_img = pygame.image.load(path + "player/player_run.png").convert_alpha()
player_run_sprite_sheet = SpriteSheet(player_run_img, 256, 256)
player_run = player_run_sprite_sheet.get_images(8, 8, 32, 32, fixer=4)
player_run = player_run_sprite_sheet.resize(
    player_run, 32 * player_scale, 32 * player_scale
)

player_idle_img = pygame.image.load(path + "player/player_idle.png").convert_alpha()
player_idle_sprite_sheet = SpriteSheet(player_idle_img, 64, 256)
player_idle = player_idle_sprite_sheet.get_images(8, 2, 32, 32, fixer=16)
player_idle = player_idle_sprite_sheet.resize(
    player_idle, 32 * player_scale, 32 * player_scale
)

player_jump_img = pygame.image.load(path + "player/player-jump_40x40.png").convert_alpha()
player_jump_sprite_sheet = SpriteSheet(player_jump_img, 280, 320)
player_jump = player_jump_sprite_sheet.get_images(8, 7, 40, 40, fixer=5.7)
player_jump = player_jump_sprite_sheet.resize(
    player_jump, 40 * player_scale, 40 * player_scale
)

"""
Player movements:
ur = Up + Right
dr = Down + Right
ul = Up + Left
dl = Down + Left
"""
# Forward/Backward
player_run_forward = player_run[0:8]
player_run_backward = player_run[32: 32 + 8]

# Right movements
player_run_ur = player_run[8: 8 + 8]
player_run_right = player_run[16: 16 + 8]
player_run_dr = player_run[24: 24 + 8]

# Left movements
player_run_dl = player_run[40:48]
player_run_left = player_run[48: 48 + 8]
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
    "up + left": player_idle_ul,
}

# Player jump
player_jumping = {
    "forward": player_jump[0:7],
    "up + right": player_jump[7:14],
    "right": player_jump[14:21],
    "down + right": player_jump[21:28],
    "backward": player_jump[28:35],
    "down + left": player_jump[35:42],
    "left": player_jump[42:49],
    "up + left": player_jump[49:56],
}

# Bee Bot
bee_bot_size = 40

bee_bot_img = pygame.image.load(path + "beebot-move_30x30.png").convert_alpha()
bee_bot_sprite_sheet = SpriteSheet(bee_bot_img, 30, 240)
bee_bot_move = bee_bot_sprite_sheet.get_images(8, 1, 30, 30, fixer=29)
bee_bot_move = bee_bot_sprite_sheet.resize(bee_bot_move, bee_bot_size, bee_bot_size)

bee_bot_moving = {
    "forward": bee_bot_move[0],
    "up + right": bee_bot_move[1],
    "right": bee_bot_move[2],
    "down + right": bee_bot_move[3],
    "backward": bee_bot_move[4],
    "down + left": bee_bot_move[5],
    "left": bee_bot_move[6],
    "up + left": bee_bot_move[7],
}

'''Block Sprites'''
block_size = 60

# Ground brick_block_1
brick_block_1_img = pygame.image.load(path + "blocks/brick_block_1.png").convert_alpha()
brick_block_1 = scale_image(brick_block_1_img, block_size, block_size)

brick_block_2_img = pygame.image.load(path + "blocks/brick_block_2.png").convert_alpha()
brick_block_2 = scale_image(brick_block_2_img, block_size, block_size)

brick_block_3_img = pygame.image.load(path + "blocks/brick_block_3.png").convert_alpha()
brick_block_3 = scale_image(brick_block_3_img, block_size, block_size)

# Dirt Block
dirt_block_img = pygame.image.load(path + "blocks/dirt_block.png").convert_alpha()
dirt_block = scale_image(dirt_block_img, block_size, block_size)

# Shadow
shadow_size = 20
shadow_img = pygame.image.load(path + "shadow.png").convert_alpha()
shadow_img = scale_image(shadow_img, shadow_size, shadow_size)


'''Weapons'''
blaster_size = (93*0.3, 66*0.3)
blaster_img = pygame.image.load(path + "guns/side/blasterB.png").convert_alpha()
blaster_img = pygame.transform.scale(blaster_img, blaster_size)

'''Others'''
# Bullet
bullet_size = 5
bullet_img = pygame.image.load(path + "bullet.png").convert_alpha()

# Cursor
cursor_size = 16
cursor_img = pygame.image.load(path + "cursor.png").convert_alpha()
cursor = scale_image(cursor_img, cursor_size, cursor_size)

# Menu Bar
menu_bar_size = 500
menu_bar_img = pygame.image.load(path + "menu_bar.png").convert_alpha()
menu_bar_img = pygame.transform.scale(menu_bar_img, (menu_bar_size, menu_bar_size))

'''Icons'''
# Gear icon
gear_icon_size = 30
gear_icon_img = pygame.image.load(path + "icons/gear-icon.png").convert_alpha()
gear_icon = scale_image(gear_icon_img, gear_icon_size, gear_icon_size)

# Checkmarks
green_check_mark_img = pygame.image.load(path + "icons/green-checkmark.png").convert_alpha()


