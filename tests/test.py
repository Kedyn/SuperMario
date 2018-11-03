import sys
import pygame

from tilemap import TileMap


pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Test")

tile_map = TileMap(screen)

# tile_map.load_map("tile_map.json")
tile_map.load_map("level1.json")

tile_map.update(0, 0)

x = 0
y = 0
direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
            elif event.key == pygame.K_UP:
                direction = 2
            elif event.key == pygame.K_RIGHT:
                direction = 3
            elif event.key == pygame.K_DOWN:
                direction = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = 0
            elif event.key == pygame.K_UP:
                direction = 0
            elif event.key == pygame.K_RIGHT:
                direction = 0
            elif event.key == pygame.K_DOWN:
                direction = 0
    if direction is 1:
        x -= 1
    elif direction is 2:
        y -= 1
    elif direction is 3:
        x += 1
    elif direction is 4:
        y += 1

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    tile_map.update(x, y)
    tile_map.render(x, y)

    pygame.display.flip()
