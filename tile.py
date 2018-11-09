import pygame


class Tile:
    def __init__(self, screen, i, j, tile_type, width, height, images=[]):
        self.screen = screen
        self.tile_type = tile_type

        self.interactive_id = -1

        self.images = {}

        for image in images:
            if image:
                path = image.split('/')
                full_name = path[-1].split('.')
                self.images[full_name[0]] = pygame.image.load(image)

        x = j * width
        y = i * height

        self.image = None

        if images:
            self.image = next(iter(self.images.values()))

            rect = self.image.get_rect()

            width = rect.width
            height = rect.height

        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        if self.image:
            rect = self.image.get_rect()

            width = rect.width
            height = rect.height

            self.rect(self.rect.x, self.rect.y, width, height)

    def render(self, x, y):
        if self.image:
            rect = pygame.Rect(self.rect.x - x, self.rect.y - y,
                               self.rect.width, self.rect.height)

            self.screen.blit(self.image, rect)
