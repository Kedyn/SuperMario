import json

from tile import Tile


class TileMap:
    def __init__(self, screen):
        self.screen = screen
        self.last_first_tile_x = -1
        self.last_first_tile_y = -1

    def load_map(self, file):
        with open(file) as f:
            self.__tile_map = json.load(f)

        self.map = self.__tile_map['map']

        width = self.__tile_map['tile_width']
        height = self.__tile_map['tile_height']

        self.tiles_x = int(self.screen.get_rect().right / width) + 2
        self.tiles_y = int(self.screen.get_rect().bottom / height) + 2

        self.tiles = []

        for row, data_row in enumerate(self.map):
            row_contents = []

            for col, data_col in enumerate(data_row):
                if self.__tile_map['images'][data_col] is not "":
                    row_contents.append(Tile(self.screen, row, col, width,
                                             height, data_col,
                                             self.__tile_map['images']
                                             [data_col], ))
                else:
                    row_contents.append(None)

            self.tiles.append(row_contents)

            self.__visible_tiles = []

    def update(self, x, y):
        tile_x = int(x / self.__tile_map['tile_width']) - 1
        tile_y = int(y / self.__tile_map['tile_height']) - 1

        if tile_x + self.tiles_x > len(self.tiles[0]):
            tile_x = len(self.tiles[0]) - self.tiles_x - 1

        if tile_x < 0:
            tile_x = 0

        if tile_y + self.tiles_y > len(self.tiles):
            tile_y = len(self.tiles) - self.tiles_y - 1

        if tile_y < 0:
            tile_y = 0

        if tile_x != self.last_first_tile_x or \
                tile_y != self.last_first_tile_y:
            max_y = tile_y + self.tiles_y
            max_x = tile_x + self.tiles_x

            if max_y > len(self.tiles):
                max_y = len(self.tiles)

            if max_x > len(self.tiles[0]):
                max_x = len(self.tiles[0])

            self.__visible_tiles = []
            for i in range(tile_y, max_y):
                for j in range(tile_x, max_x):
                    self.__visible_tiles.append(self.tiles[i][j])

        self.last_first_tile_x = tile_x
        self.last_first_tile_y = tile_y

    def render(self, x, y):
        first_tile = self.__visible_tiles[0]

        if x > first_tile.rect.x:
            x = first_tile.rect.x
        if y > first_tile.rect.y:
            y = first_tile.rect.y

        self.screen.fill((0, 0, 0))
        for tile in self.__visible_tiles:
            tile.render(x, y)
