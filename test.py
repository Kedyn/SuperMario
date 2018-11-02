import sys
import pygame

from tilemap import TileMap


pygame.init()

screen = pygame.display.set_mode((1280, 480))

pygame.display.set_caption("Test")

tile_map = TileMap(screen)

tile_map.load_map("tile_map.json")
# tile_map.load_map("level1.json")

tile_map.update(0, 0)

x = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                x += 32
    tile_map.update(x, 0)
    tile_map.render()

    pygame.display.flip()
