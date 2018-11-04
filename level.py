from tilemap import TileMap


class Level:
    def __init__(self, file, screen):
        self.__tile_map = TileMap(file, screen)

        self.done = False

    def keydown(self, key):
        self.__tile_map.mario.keydown(key)

    def keyup(self, key):
        self.__tile_map.mario.keyup(key)

    def update(self):
        self.__tile_map.mario.update()

        self.__tile_map.update()

    def render(self):
        self.__tile_map.render()

        self.__tile_map.mario.render()
