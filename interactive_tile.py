class InteractiveTile:
    def __init__(self, tile):
        self.tile = tile

    def update(self):
        if self.tile.tile_type is '?':
            if self.tile.image is self.tile.images['mystery_box_bright']:
                self.tile.image = self.tile.images['mystery_box_normal']
            elif self.tile.image is self.tile.images['mystery_box_normal']:
                self.tile.image = self.tile.images['mystery_box_dark']
            else:
                self.tile.image = self.tile.images['mystery_box_bright']
