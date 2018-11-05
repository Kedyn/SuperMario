import pygame

from tile import Tile


class Mario:
    def __init__(self, screen, x, y, camera, collding_tiles, images=[]):
        self.camera = camera
        self.colliding_tiles = collding_tiles

        self.tile = Tile(screen, 0, 0, '', images)

        self.tile.rect.x = x
        self.tile.rect.y = y

        self.direction_x = 0

        self.velocity = pygame.Vector2(0, 0)

        self.velocity_to_be_reached = pygame.Vector2(0, 0)

        self.max_velocity = pygame.Vector2(1, 1)

        self.ticks = pygame.time.get_ticks()

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def keydown(self, key):
        if key == pygame.K_LEFT:
            self.velocity_to_be_reached.x = self.max_velocity.x * -1
        elif key == pygame.K_RIGHT:
            self.velocity_to_be_reached.x = self.max_velocity.x

    def keyup(self, key):
        if key == pygame.K_LEFT or \
                key == pygame.K_RIGHT:
            self.velocity_to_be_reached.x = 0

    def update(self):
        dt = pygame.time.get_ticks() - self.ticks
        difference = self.velocity_to_be_reached.x - self.velocity.x
        prev_velocity_x = self.velocity.x

        self.velocity.x = self.velocity_to_be_reached.x

        if difference > dt:
            self.velocity.x = self.velocity.x + dt
        elif difference < -dt:
            self.velocity.x = self.velocity.x - dt

        self.tile.rect.x += self.velocity.x
        self.tile.rect.y += self.velocity.y

        if self.tile.rect.left < self.camera.left:
            self.tile.rect.left = self.camera.left
            self.velocity.x = 0
            self.velocity_to_be_reached.x = 0
        elif self.tile.rect.right > self.camera.right:
            self.tile.rect.right = self.camera.right
            self.velocity.x = 0
            self.velocity_to_be_reached.x = 0

        if self.velocity.x != 0:
            for tile in self.__visible_tiles:
                if tile.tile_type in self.colliding_tiles:
                    if self.tile.rect.bottom != tile.rect.top:
                        if self.tile.rect.colliderect(tile.rect):
                            if self.velocity.x > 0 and \
                                    tile.rect.x > self.tile.rect.x:
                                self.tile.rect.right = tile.rect.left
                                self.velocity.x = 0
                                self.velocity_to_be_reached.x = 0
                            elif self.velocity.x < 0 and \
                                    tile.rect.x < self.tile.rect.x:
                                self.tile.rect.left = tile.rect.right
                                self.velocity.x = 0
                                self.velocity_to_be_reached.x = 0

        if self.velocity.x == 0:
            if self.tile.image != self.tile.images["standing_right"] and \
                    self.tile.image != self.tile.images["standing_left"]:
                if prev_velocity_x > 0:
                    self.tile.image = self.tile.images["standing_right"]
                else:
                    self.tile.image = self.tile.images["standing_left"]
        else:
            if self.velocity.x > 0:
                if self.tile.image is self.tile.images["moving_two_right"]:
                    self.tile.image = self.tile.images["moving_three_right"]
                elif self.tile.image is self.tile.images["moving_three_right"]:
                    self.tile.image = self.tile.images["moving_one_right"]
                else:
                    self.tile.image = self.tile.images["moving_two_right"]
            else:
                if self.tile.image is self.tile.images["moving_two_left"]:
                    self.tile.image = self.tile.images["moving_three_left"]
                elif self.tile.image is self.tile.images["moving_three_left"]:
                    self.tile.image = self.tile.images["moving_one_left"]
                else:
                    self.tile.image = self.tile.images["moving_two_left"]

        self.ticks = pygame.time.get_ticks()

    def render(self, x, y):
        self.tile.render(x, y)
