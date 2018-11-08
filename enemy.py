import pygame

from tile import Tile


class Enemy:
    def __init__(self, screen, x, y, enemy_type, width, height, images=[]):
        self.tile = Tile(screen, 0, 0, '', width, height, images)

        self.enemy_type = enemy_type

        self.tile.rect.x = x
        self.tile.rect.y = y

        self.__visible_tiles = []

        self.frame = 0
        self.active = False

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def set_max_position(self, total_width, total_height):
        self.total_width = total_width
        self.total_height = total_height

    def update(self):
        if self.active:
            self.frame += 1
            self.tile.rect.x += -1

            if self.frame % 30 == 0:
                if self.enemy_type == "goomba":
                    if self.tile.image is self.tile.images["goomba_two"]:
                        self.tile.image = self.tile.images["goomba_one"]
                    else:
                        self.tile.image = self.tile.images["goomba_two"]

    def render(self, x, y):
        self.tile.render(x, y)
