import pygame

from tile import Tile


class Enemy:
    def __init__(self, screen, x, y, enemy_type, images=[]):
        self.tile = Tile(screen, 0, 0, '', images)

        self.enemy_type = enemy_type

        self.tile.rect.x = x
        self.tile.rect.y = y

        self.__visible_tiles = []

        self.ticks = pygame.time.get_ticks()

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def set_max_position(self, total_width, total_height):
        self.total_width = total_width
        self.total_height = total_height

    def update(self):
        # test
        pass

    def render(self, x, y):
        self.tile.render(x, y)
