from tile import Tile


class InteractiveTile:
    def __init__(self, screen, row, col, tile_type, images=[]):
        self.tile = Tile(screen, row, col, tile_type, images)

    def update(self):
        if self.tile.tile_type is '?':
            if self.tile.image is self.tile.images['mystery_box_bright']:
                self.tile.image = self.tile.images['mystery_box_normal']
            elif self.tile.image is self.tile.images['mystery_box_normal']:
                self.tile.image = self.tile.images['mystery_box_dark']
            else:
                self.tile.image = self.tile.images['mystery_box_bright']

    def render(self, x, y):
        self.tile.render(x, y)
