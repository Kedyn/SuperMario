import pygame


class Tile:
    def __init__(self, screen, i, j, tile_type, images=[]):
        self.screen = screen
        self.tile_type = tile_type

        self.images = {}

        for image in images:
            if image:
                path = image.split('/')
                full_name = path[-1].split('.')
                self.images[full_name[0]] = pygame.image.load(image)

        width = 0
        height = 0

        self.image = None

        if images:
            self.image = next(iter(self.images.values()))

            rect = self.image.get_rect()

            width = rect.width
            height = rect.height

        self.rect = pygame.Rect(j * width, i * height, width, height)

    def render(self, x, y):
        if self.image:
            rect = pygame.Rect(self.rect.x - x, self.rect.y - y,
                               self.rect.width, self.rect.height)

            self.screen.blit(self.image, rect)
