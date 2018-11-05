import json
import pygame

from tile import Tile
from mario import Mario


class TileMap:
    def __init__(self, file, screen):
        self.screen = screen

        with open(file) as f:
            self.__info = json.load(f)

        self.tile = pygame.Rect(0, 0, self.__info['tile_width'],
                                self.__info['tile_height'])

        self.camera = pygame.Rect(0, 0, self.screen.get_rect().width,
                                  self.screen.get_rect().height)

        width = self.tile.width
        height = self.tile.height

        self.visible_tiles_x = int(self.tile.width / width)
        self.visible_tiles_y = int(self.tile.height / height)

        self.tiles = []

        self.mario = None

        mario = self.__info['mario']

        for row, data_row in enumerate(self.__info['map']):
            row_contents = []

            for col, data_col in enumerate(data_row):
                if data_col is mario:
                    self.mario = Mario(screen, row, col, width,
                                       height,
                                       self.__info['images'][data_col])
                else:
                    if self.__info['images'][data_col]:
                        row_contents.append(Tile(screen, row, col, width,
                                                 height, data_col,
                                                 self.__info['images']
                                                 [data_col]))
                    else:
                        row_contents.append(Tile(screen, row, col, width,
                                                 height, data_col))

            self.tiles.append(row_contents)

        self.total_tiles_x = len(self.tiles[0])
        self.total_tiles_y = len(self.tiles)

        self.total_width = self.total_tiles_x * width
        self.total_height = self.total_tiles_y * height

        self.__visible_tiles = []

        self.update()

    def update(self):
        self.camera.centerx = self.mario.tile.rect.centerx

        if self.camera.left < 0:
            self.camera.left = 0
        elif self.camera.right > self.total_width:
            self.camera.right = self.total_width

        min_x = int(self.camera.left / self.tile.width)
        max_x = min(int(self.camera.right / self.tile.width),
                    self.total_tiles_x - 1)
        min_y = 0
        max_y = self.total_tiles_y

        self.__visible_tiles = []

        for i in range(min_y, max_y):
            for j in range(min_x, max_x):
                self.__visible_tiles.append(self.tiles[i][j])

        self.mario.set_visible_tiles(self.__visible_tiles)

    def render(self):
        x = self.camera.left
        y = self.camera.top

        self.screen.fill((0, 0, 0))
        for tile in self.__visible_tiles:
            if tile:
                tile.render(x, y)

        self.mario.render(x, y)
