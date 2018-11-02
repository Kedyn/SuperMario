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
                                             [data_col]))
                else:
                    row_contents.append(None)

            self.tiles.append(row_contents)

            self.__visible_tiles = []

    def update(self, x, y):
        tile_x = int(x / self.__tile_map['tile_width'])
        tile_y = int(y / self.__tile_map['tile_height'])

        if tile_x + self.tiles_x > len(self.tiles[0]):
            tile_x = len(self.tiles[0]) - self.tiles_x

        if tile_y + self.tiles_y > len(self.tiles):
            tile_y = len(self.tiles) - self.tiles_y

        if tile_x != self.last_first_tile_x or \
                tile_y != self.last_first_tile_y:
            self.__visible_tiles = []
            for i in range(tile_y, tile_y + self.tiles_y):
                for j in range(tile_x, tile_x + self.tiles_x):
                    self.__visible_tiles.append(self.tiles[i][j])

        self.last_first_tile_x = tile_x
        self.last_first_tile_y = tile_y

    def render(self):
        for tile in self.__visible_tiles:
            tile.render()
