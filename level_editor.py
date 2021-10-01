import pygame
import json

from src.id_generator import return_id

# Essentials
block_size = 60
x_dif = 450 - 424
y_dif = 15
grid = 20

# Levels
with open('src/level_data/level_test.json', 'r') as f:
    level_test = json.loads(f.read())

level_test['objects'] = []


def return_base():
    for e in range(grid + 2):
        for i in range(grid + 1):
            level_test["objects"].append({return_id('block'): [(450 + (x_dif * e)) - (x_dif * i),
                                                               0 + (y_dif * i) + (y_dif * e), block_size, block_size]})

    return level_test


with open('src/level_data/level_test.json', 'w') as f:
    json.dump(return_base(), f, indent=2)

print(len(level_test['objects']))
