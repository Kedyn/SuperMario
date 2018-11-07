import pygame

from tile import Tile

vec = pygame.math.Vector2


class Mario:
    def __init__(self, screen, x, y, camera, collding_tiles, images=[]):
        self.camera = camera
        self.colliding_tiles = collding_tiles

        self.tile = Tile(screen, 0, 0, '', images)  # this is mario

        self.direction_x = 0

        self.velocity = vec(0, 0)  # velocity of mario

        self.velocity_to_be_reached = vec(0, 0)

        self.max_velocity = vec(1, 1)

        self.ticks = pygame.time.get_ticks()

        #  stuff i added
        self.mario_gravity = 0.001
        self.mario_acceleration = 0.6
        self.mario_friction = -0.08
        self.mario_jump_height = 18
        self.keys = []
        self.acc = vec(0, 0)  # mario acceleration
        self.pos = vec(x, y - 10)

        self.tile.rect.x = self.pos.x
        self.tile.rect.y = self.pos.y

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def keydown(self, key):
        self.keys.append(key)

    def keyup(self, key):
        self.keys.remove(key)

    def update(self):

        dt = pygame.time.get_ticks() - self.ticks
        difference = self.velocity_to_be_reached.x - self.velocity.x
        prev_velocity_x = self.velocity.x

        # stuff i added
        for key in self.keys:
            if key == pygame.K_LEFT:
                self.acc.x = -self.mario_acceleration
            if key == pygame.K_RIGHT:
                self.acc.x = self.mario_acceleration

        self.acc = vec(0, self.mario_gravity)

        # apply friction
        self.acc.x += self.velocity.x * self.mario_friction

        # my version of handling movement
        self.velocity += self.acc
        if abs(self.velocity.x) < 0.5:
            self.velocity.x = 0
        self.pos += self.velocity + 0.5 * self.acc

        self.tile.rect.x = self.pos.x
        self.tile.rect.y = self.pos.y

        """collision for y coordinate"""
        # if self.velocity.y > 0:
        #     hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        #     if hits:
        #         lowest = hits[0]
        #         for hit in hits:
        #             if hit.rect.bottom > lowest.rect.bottom:
        #                 lowest = hit
        #         if self.player.pos.y < lowest.rect.bottom:
        #             self.player.pos.y = lowest.rect.top + .5  # the .5 is to make sure it is colliding w/ the floor
        #             self.player.vel.y = 0
        #             self.player.jumping = False

        # if difference > dt:
        #     self.velocity.x = self.velocity.x + dt
        # elif difference < -dt:
        #     self.velocity.x = self.velocity.x - dt


        if self.tile.rect.left < self.camera.left:
            self.tile.rect.left = self.camera.left
            self.velocity.x = 0
            self.velocity_to_be_reached.x = 0
        elif self.tile.rect.right > self.camera.right:
            self.tile.rect.right = self.camera.right
            self.velocity.x = 0
            self.velocity_to_be_reached.x = 0

        # handles collision
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
        #if self.velocity.y > 0:
        for tile in self.__visible_tiles:
            if tile.tile_type in self.colliding_tiles:
                if self.tile.rect.colliderect(tile.rect):
                    if self.tile.rect.top >= tile.rect.top:
                        print('collide')
                        self.velocity.y = 0
                        self.tile.rect.bottom = tile.rect.top


        # image/animation handling
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
