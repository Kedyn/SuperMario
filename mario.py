import pygame

from tile import Tile


class Mario:
    def __init__(self, screen, i, j, width, height, images=[]):
        self.tile = Tile(screen, i, j, width, height, '', images)

        self.direction_x = 0

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

    def render(self):
        self.tile.screen.blit(self.tile.image, self.tile.rect)
