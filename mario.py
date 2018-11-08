import pygame

from tile import Tile

vec = pygame.math.Vector2

'''
Use interacting tiles and enemies for collision like visible tiles.
'''


class Mario:
    def __init__(self, screen, x, y, camera, colliding_tiles, width, height,
                 enemies, images=[]):
        self.camera = camera
        self.colliding_tiles = colliding_tiles
        # self.interacting_tiles = interacting_tiles
        self.enemies = enemies

        self.tile = Tile(screen, 0, 0, '', width, height, images)  # this is mario

        self.velocity = vec(0, 0)  # velocity of mario

        self.velocity_to_be_reached = vec(0, 0)

        self.ticks = pygame.time.get_ticks()

        #  stuff i added
        self.mario_gravity = 0.3
        self.mario_acceleration = 0.6
        self.mario_friction = -0.08
        self.mario_jump_height = 9.3
        self.keys = []
        self.acc = vec(0, self.mario_gravity)  # mario acceleration
        self.pos = vec(x, y)
        self.jumping = False
        self.falling = False
        self.jump_count = 0
        self.tile.rect.x = self.pos.x
        self.tile.rect.y = self.pos.y

        self.he_dead = False

    def set_visible_tiles(self, visible_tiles):
        self.__visible_tiles = visible_tiles

    def keydown(self, key):
        self.keys.append(key)

        # stuff i added
        self.jumping = False
        if key == pygame.K_SPACE:
            print('jump = ' + str(self.jump_count))
            if self.jump_count <= 10:
                self.jump()

    def keyup(self, key):
        self.jumping = True
        self.keys.remove(key)
        if key == pygame.K_SPACE:
            self.jump_cut()

    def jump_cut(self):
        if self.jumping:
            if self.velocity.y < -1:
                self.velocity.y = -1

    def jump(self):
        self.velocity.y = -self.mario_jump_height

    def check_horizontal_tiles(self, tiles):
        if self.velocity.x != 0:
            for tile in tiles:
                if tile.tile_type in self.colliding_tiles:
                    if self.tile.rect.bottom != tile.rect.top:
                        if self.tile.rect.colliderect(tile.rect):
                            if self.velocity.x > 0 and \
                                    tile.rect.x > self.tile.rect.x:
                                self.tile.rect.right = tile.rect.left
                                self.velocity.x = 0
                                self.pos.x = tile.rect.left - \
                                    self.tile.rect.width
                                break
                            elif self.velocity.x < 0 and \
                                    tile.rect.x < self.tile.rect.x:
                                self.tile.rect.left = tile.rect.right
                                self.velocity.x = 0
                                self.pos.x = tile.rect.right
                                break

    def check_falling(self, tiles):  # falling collision

        for tile in tiles:
            if tile.tile_type in self.colliding_tiles:
                if self.tile.rect.colliderect(tile.rect):
                    if self.tile.rect.top > tile.rect.top:
                        print('bottom collide')
                        self.tile.rect.top = tile.rect.bottom
                        self.velocity.y *= -1
                        self.jump_cut()
                        break
                    if self.tile.rect.bottom >= tile.rect.top:
                        self.velocity.y = 0
                        self.pos.y = tile.rect.top - self.tile.rect.height
                        self.tile.rect.bottom = tile.rect.top
                        self.falling = True
                        break

        # for enemy in self.enemies:
        #    if enemy.tile.rect.colliderect(self.tile.rect):
        #        print('enemy collide')

    def update(self):
        prev_velocity_x = self.velocity.x

        self.acc.x = 0
        self.falling = False

        print('position is --->' + str(self.velocity))
        # stuff i added
        for key in self.keys:
            if key == pygame.K_LEFT:
                self.acc.x = -self.mario_acceleration
            if key == pygame.K_RIGHT:
                self.acc.x = self.mario_acceleration

        # apply friction
        self.acc.x += self.velocity.x * self.mario_friction

        # my version of handling movement
        self.velocity += self.acc
        if abs(self.velocity.x) < 0.55:
            self.velocity.x = 0
        self.pos += self.velocity + 0.5 * self.acc

        self.tile.rect.x = self.pos.x

        self.check_horizontal_tiles(self.__visible_tiles)

        self.tile.rect.y = self.pos.y

        self.check_falling(self.__visible_tiles)
        print('is he falling? ---> ' + str(self.falling))
        # create enemy collision here

        # camera stuff
        if self.tile.rect.left < self.camera.left:
            self.tile.rect.left = self.camera.left
            self.velocity.x = 0
        elif self.tile.rect.right > self.camera.right:
            self.tile.rect.right = self.camera.right
            self.velocity.x = 0
        elif self.tile.rect.bottom > self.camera.bottom:
            self.he_dead = True
            print(str(self.he_dead))



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

    def render(self, x, y):
        self.tile.render(x, y)
