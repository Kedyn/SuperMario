import pygame

from tile import Tile


class Mario:
    def __init__(self, screen, i, j, width, height, images=[]):
        self.tile = Tile(screen, i, j, width, height, '', images)

        self.direction_x = 0

        self.__visible_tiles = []

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def keydown(self, key):
        if key == pygame.K_LEFT:
            self.direction_x = -1
        elif key == pygame.K_RIGHT:
            self.direction_x = 1

    def keyup(self, key):
        if key == pygame.K_LEFT or \
                key == pygame.K_RIGHT:
            self.direction_x = 0

    def update(self):
        self.tile.rect.x += self.direction_x

    def render(self, x, y):
        rect = pygame.Rect(self.tile.rect.x - x, self.tile.rect.y - y,
                           self.tile.rect.width, self.tile.rect.height)

        self.tile.screen.blit(self.tile.image, rect)
