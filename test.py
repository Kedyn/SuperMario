import sys
import pygame

from tilemap import TileMap


pygame.init()

screen = pygame.display.set_mode((1280, 1024))

pygame.display.set_caption("Test")

tile_map = TileMap(screen)

tile_map.load_map("tile_map.json")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    tile_map.render()

    pygame.display.flip()
