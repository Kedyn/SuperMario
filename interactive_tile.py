class InteractiveTile:
    def __init__(self, tile):
        self.tile = tile

        self.frame = 0

    def __str__(self):
        return 'Interactive tile type: \'' + self.tile.tile_type + \
            '\' Rect: ' + str(self.tile.rect)

    def update(self):
        self.frame += 1
        if self.frame % 10 == 0:
            if self.tile.tile_type is '?':
                if self.tile.image is self.tile.images['mystery_box_bright']:
                    self.tile.image = self.tile.images['mystery_box_normal']
                elif self.tile.image is self.tile.images['mystery_box_normal']:
                    self.tile.image = self.tile.images['mystery_box_dark']
                else:
                    self.tile.image = self.tile.images['mystery_box_bright']
