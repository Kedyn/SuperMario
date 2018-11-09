import pygame

from tile import Tile


class Enemy:
    def __init__(self, screen, x, y, enemy_type, colliding_tiles, width, height, images=[]):
        self.tile = Tile(screen, 0, 0, '', width, height, images)

        self.enemy_type = enemy_type

        self.tile.rect.x = x
        self.tile.rect.y = y
        self.colliding_tiles = colliding_tiles
        self.__visible_tiles = []

        self.frame = 0
        self.active = False
        self.alive = True
        self.movement_factor = -1
        self.ground_rect = pygame.Rect(self.tile.rect.x, self.tile.rect.y,
                                       width, height)
        self.ground_rect.top = self.tile.rect.bottom


    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def set_max_position(self, total_width, total_height):
        self.total_width = total_width
        self.total_height = total_height

    def update(self):
        if self.active:
            on_ground = False

            for tile in self.__visible_tiles:
                if tile.tile_type in self.colliding_tiles and self.alive:
                    if self.tile.rect.bottom != tile.rect.top:
                        if self.tile.rect.colliderect(tile.rect):
                            if self.movement_factor < 0:
                                self.tile.rect.left = tile.rect.right
                            elif self.movement_factor > 0:
                                self.tile.rect.right = tile.rect.left

                            self.flip()

                    if self.ground_rect.top == tile.rect.top:
                        if self.ground_rect.colliderect(tile.rect):
                            on_ground = True
            if self.alive:
                self.frame += 1
                self.tile.rect.x += self.movement_factor

            if not on_ground and self.alive:
                self.tile.rect.y += 1

            self.ground_rect.top = self.tile.rect.bottom
            self.ground_rect.x = self.tile.rect.x

            if self.frame % 30 == 0 and self.alive:
                if self.enemy_type == "goomba":
                    if self.tile.image is self.tile.images["goomba_two"]:
                        self.tile.image = self.tile.images["goomba_one"]
                    else:
                        self.tile.image = self.tile.images["goomba_two"]

    def render(self, x, y):
        if self.active:
            self.tile.render(x, y)

    def flip(self):
        self.movement_factor *= -1

    def death(self):
        if self.alive:

            if self.enemy_type == "goomba":
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sound/stomp.ogg'))
                self.tile.image = pygame.image.load('assets/images/enemies/goomba/goombaDead.gif')
                self.tile.rect.y += 20
            if self.enemy_type == "koopa":
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sound/kick.ogg'))
                self.tile.image = pygame.image.load('assets/images/enemies/koopa/shell.gif')
                self.tile.rect.y += 20
                self.enemy_type = "shell"
            self.alive = False


