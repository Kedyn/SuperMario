import pygame

from tile import Tile

vec = pygame.math.Vector2


class Character:
    def __init__(self, screen, x, y, colliding_tiles_types,
                 interacting_tiles, width, height, population, images=[]):
        self.colliding_tiles_types = colliding_tiles_types
        self.interacting_tiles = interacting_tiles
        self.population = population

        self.tile = Tile(screen, 0, 0, '', width, height, images)

        self.velocity = vec(0, 0)

        self.gravity = .8
        self.acceleration = 0.6
        self.friction = -0.08

        self.acc = vec(0, self.gravity)
        self.pos = vec(x, y)
        self.falling = False
        self.tile.rect.x = self.pos.x
        self.tile.rect.y = self.pos.y

        self.ground_rect = pygame.Rect(self.tile.rect.x, self.tile.rect.y,
                                       width, height)
        self.ground_rect.top = self.tile.rect.bottom

        self.colliding_bottom = False
        self.colliding_top = False
        self.colliding_left = False
        self.colliding_right = False

        self.collided_with_other_character = False

        self.current_colliding_tiles = []
        self.current_colliding_population = []

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def check_colliding_tiles(self, tiles):
        self.current_colliding_tiles = []
        for tile in self.colliding_tiles_types:
            if tile is not self.tile:
                if tile.tile_type in self.colliding_tiles_types:
                    if self.tile.rect.bottom != tile.rect.top:
                        if self.tile.rect.colliderect(tile.rect):
                            if tile.rect.x > self.tile.rect.x:
                                self.colliding_right = True
                                self.current_colliding_tiles.append(tile)
                            elif tile.rect.x < self.tile.rect.x:
                                self.colliding_left = True
                                self.current_colliding_tiles.append(tile)
                            elif self.tile.rect.top > tile.rect.top:
                                self.colliding_top = True
                                self.current_colliding_tiles.append(tile)
                            elif self.ground_rect.top == tile.rect.top:
                                self.colliding_bottom = True
                                self.current_colliding_tiles.append(tile)

    def check_collisions(self):
        self.check_colliding_tiles(self.__visible_tiles)
        self.check_colliding_tiles(self.interacting_tiles)

        self.current_colliding_population = []
        for character in self.population:
            if character is not self:
                if character.tile.rect.colliderect(self.tile.rect):
                    self.collided_with_other_character = True
                    self.current_colliding_population.append(character)

    def update(self):
        #apply friction when walking
        self.acc.x += self.velocity.x * self.friction

        self.velocity += self.acc
        self.pos += self.velocity + 0.5 * self.acc
        self.tile.rect.x = self.pos.x
        self.tile.rect.y = self.pos.y

    def render(self, x, y):
        self.tile.render(x, y)
