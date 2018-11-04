import json

from tile import Tile
from mario import Mario


class TileMap:
    def __init__(self, file, screen):
        self.screen = screen
        self.last_first_tile_x = -1
        self.last_first_tile_y = -1

        with open(file) as f:
            self.__tile_map = json.load(f)

        self.map = self.__tile_map['map']

        width = self.__tile_map['tile_width']
        height = self.__tile_map['tile_height']

        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height

        self.tiles_x = int(self.width / width)
        self.tiles_y = int(self.height / height)

        self.tiles = []

        self.mario = None

        mario = self.__tile_map['mario']

        for row, data_row in enumerate(self.map):
            row_contents = []

            for col, data_col in enumerate(data_row):
                if data_col is mario:
                    self.mario = Mario(self.screen, row, col, width,
                                       height,
                                       self.__tile_map['images'][data_col])
                else:
                    if self.__tile_map['images'][data_col]:
                        row_contents.append(Tile(self.screen, row, col, width,
                                                 height, data_col,
                                                 self.__tile_map['images']
                                                 [data_col]))
                    else:
                        row_contents.append(Tile(self.screen, row, col, width,
                                                 height, data_col))

            self.tiles.append(row_contents)

            self.__visible_tiles = []

        self.update()

    def update(self):
        width = self.__tile_map['tile_width']
        height = self.__tile_map['tile_height']

        total_tiles_x = len(self.tiles[0])
        total_tiles_y = len(self.tiles)

        total_width = total_tiles_x * width
        total_height = total_tiles_y * height

        x = self.mario.tile.rect.x + self.mario.tile.rect.width - \
            (self.width / 2)
        y = self.mario.tile.rect.y + self.mario.tile.rect.height - \
            (self.height / 2)

        if x < 0:
            x = 0
        elif x > total_width - (self.width / 2):
            x = total_width - self.width

        if y < 0:
            y = 0
        elif y > total_height - (self.height / 2):
            y = total_height - self.height

        tile_x = int(x / width)
        tile_y = int(y / height)

        if tile_x + self.tiles_x > total_tiles_x:
            tile_x = total_tiles_x - self.tiles_x

        if tile_x < 0:
            tile_x = 0

        if tile_y + self.tiles_y > total_tiles_y:
            tile_y = total_tiles_y - self.tiles_y

        if tile_y < 0:
            tile_y = 0

        if tile_x != self.last_first_tile_x or \
                tile_y != self.last_first_tile_y:
            max_y = tile_y + self.tiles_y
            max_x = tile_x + self.tiles_x

            if max_y > total_tiles_y:
                max_y = total_tiles_y

            if max_x > total_tiles_x:
                max_x = total_tiles_x

            self.__visible_tiles = []
            for i in range(tile_y, max_y):
                for j in range(tile_x, max_x):
                    self.__visible_tiles.append(self.tiles[i][j])

            self.mario.set_visible_tiles(self.__visible_tiles)

        self.last_first_tile_x = tile_x
        self.last_first_tile_y = tile_y

    def render(self):
        # x = self.mario.tile.rect.centerx
        # y = self.mario.tile.rect.y
        first_tile = self.__visible_tiles[0]

        # if x > first_tile.rect.x:
        x = first_tile.rect.x
        # if y > first_tile.rect.y:
        y = first_tile.rect.y

        self.screen.fill((0, 0, 0))
        for tile in self.__visible_tiles:
            if tile:
                tile.render(x, y)
