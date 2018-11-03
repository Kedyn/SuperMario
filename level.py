from tilemap import TileMap


class Level:
    def __init__(self, file, screen):
        self.__tile_map = TileMap(file, screen)

        self.done = False

    def update(self):
        self.__tile_map.update(0, 0)

    def render(self):
        self.__tile_map.render(0, 0)
