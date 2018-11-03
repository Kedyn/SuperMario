""" Sprite classes """
from settings import *
import pygame as pg
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = pg.image.load('images/small_mario/smallMarioStandRight.gif')
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width/2, screen_height/2)
        self.pos = vec(screen_width/2, screen_height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.walking_right = [pg.image.load('images/small_mario/R1.gif'), pg.image.load('images/small_mario/R2.gif'),
                              pg.image.load('images/small_mario/R3.gif')]

        self.walking_left = [pg.image.load('images/small_mario/L1.gif'), pg.image.load('images/small_mario/L2.gif'),
                             pg.image.load('images/small_mario/L3.gif')]

        self.jump_right = pg.image.load('images/small_mario/smallMarioJumpRight.gif')

        self.jump_left = pg.image.load('images/small_mario/smallMarioJumpLeft.gif')

        self.standing_right = [pg.image.load('images/small_mario/smallMarioStandRight.gif')]

        self.standing_left = [pg.image.load('images/small_mario/smallMarioStandLeft.gif')]

        self.right_reverse = [pg.image.load('images/small_mario/smallMarioRightReverse.gif')]

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -1:
                self.vel.y = -1

    def jump(self):
        # Jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits and not self.jumping:  # this removes double jump
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAVITY)  # Gravity is the y
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
                self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        # wrap around the sides of the screen
        if self.pos.x > screen_width + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = screen_width + self.rect.width / 2

        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        # show walk animation
        if self.walking:
            if now - self.last_update > 75:  # speed of animation
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_right)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walking_right[self.current_frame]
                else:
                    self.image = self.walking_left[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
            print('walking')

        # idle animation
        if not self.jumping and not self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_right)
                self.image = self.standing_right[self.current_frame]


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y