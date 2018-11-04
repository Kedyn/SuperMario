import pygame


class Tile:
    def __init__(self, screen, i, j, width, height, tile_type, images=[]):
        self.screen = screen
        self.tile_type = tile_type

        self.images = []

        for image in images:
            if image:
                pygame_image = pygame.image.load(image)

                self.images.append(pygame.transform.scale(pygame_image,
                                                          (width, height)))

        self.rect = pygame.Rect(j * height, i * width, width, height)

        self.image = None

        if images:
            self.image = self.images[0]

    def render(self, x, y):
        if self.image:
            rect = pygame.Rect(self.rect.x - x, self.rect.y - y,
                               self.rect.width, self.rect.height)
            self.screen.blit(self.image, rect)
