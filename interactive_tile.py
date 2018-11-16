class InteractiveTile:
    def __init__(self, tile):
        self.tile = tile

        self.frame = 0
        self.bumping = False
        self.top = False
        self.complete = False
        self.max_height = self.tile.rect.y - 7
        self.origin = self.tile.rect.y

    def __str__(self):
        return 'Interactive tile type: \'' + self.tile.tile_type + \
            '\' Rect: ' + str(self.tile.rect)

    def update(self):
        if not self.complete:
            self.frame += 1
            if self.frame % 10 == 0:
                if self.tile.tile_type is not '9' and \
                        self.tile.tile_type is not 'Z':
                    if self.tile.image is self.tile.images[
                            'mystery_box_bright']:
                        self.tile.image = self.tile.images[
                            'mystery_box_normal']
                    elif self.tile.image is self.tile.images[
                            'mystery_box_normal']:
                        self.tile.image = self.tile.images[
                                'mystery_box_dark']
                    else:
                        self.tile.image = self.tile.images[
                            'mystery_box_bright']

        if self.bumping:
            if self.top:
                self.tile.rect.y += 1
                if self.tile.rect.y >= self.origin:
                    self.tile.rect.y = self.origin
                    self.bumping = False
                    self.top = False
                    if self.tile.tile_type is not '9' and \
                            self.tile.tile_type is not 'Z':
                        self.tile.image = self.tile.images['mystery_box_used']
                        self.complete = True
            else:
                self.tile.rect.y -= 1
                if self.tile.rect.y <= self.max_height:
                    self.top = True

    def bump(self):
        if not self.complete:
            self.bumping = True
