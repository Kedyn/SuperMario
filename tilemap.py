import json

from tile import Tile


class TileMap:
    def __init__(self, screen):
        self.screen = screen

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

    def render(self):
        for tiles in self.tiles:
            for tile in tiles:
                tile.render()
