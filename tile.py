import pygame


class Tile:
    def __init__(self, screen, i, j, width, height, tile_type, images=None):
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

    def render(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
