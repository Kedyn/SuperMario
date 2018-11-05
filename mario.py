import pygame

from tile import Tile


class Mario:
    def __init__(self, screen, x, y, camera, images=[]):
        self.camera = camera
        print(camera)

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

    def set_max_position(self, total_width, total_height):
        self.total_width = total_width
        self.total_height = total_height

    def keydown(self, key):
        if key == pygame.K_LEFT:
            self.velocity_to_be_reached.x = self.max_velocity.x * -1
        elif key == pygame.K_RIGHT:
            self.velocity_to_be_reached.x = self.max_velocity.x
        else:
            print(len(self.__visible_tiles))

    def keyup(self, key):
        if key == pygame.K_LEFT or \
                key == pygame.K_RIGHT:
            self.velocity_to_be_reached.x = 0

    def update(self):
        dt = pygame.time.get_ticks() - self.ticks
        difference = self.velocity_to_be_reached.x - self.velocity.x

        self.velocity.x = self.velocity_to_be_reached.x

        if difference > dt:
            self.velocity.x = self.velocity.x + dt
        elif difference < -dt:
            self.velocity.x = self.velocity.x - dt

        self.tile.rect.x += self.velocity.x
        self.tile.rect.y += self.velocity.y

        if self.tile.rect.left < self.camera.left:
            self.tile.rect.left = self.camera.left
        elif self.tile.rect.right > self.camera.right:
            self.tile.rect.right = self.camera.right

        if self.velocity.x == 0:
            self.tile.image = self.tile.images[0]
        else:
            if self.tile.image is self.tile.images[2]:
                self.tile.image = self.tile.images[3]
            elif self.tile.image is self.tile.images[3]:
                self.tile.image = self.tile.images[1]
            else:
                self.tile.image = self.tile.images[2]

        self.ticks = pygame.time.get_ticks()

    def render(self, x, y):
        self.tile.render(x, y)
