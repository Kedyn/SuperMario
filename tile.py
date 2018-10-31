import pygame


class Tile:
    def __init__(self, screen, i, j, width, height, tile_type, images=None):
        self.screen = screen
        self.tile_type = tile_type

        self.images = []
        '''
        for image in images:
            pygame_image = pygame.image.load(image)

            self.images.append(pygame.transform.scale(pygame_image,
                                                      (width, height)))
        '''
        self.rect = pygame.Rect(j * height, i * width, width, height)

        self.image = None

        if images:
            self.image = images[0]

    def render(self):
        if self.image:
            self.screen.fill((0, 100, 200), self.rect)
            # self.screen.blit(self.image, self.rect)
