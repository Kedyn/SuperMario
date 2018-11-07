import pygame
from pygame.sprite import Sprite

class Power(Sprite):
    def __init__(self, screen, xpos, ypos, type):
        super(Power, self).__init__()
        self.screen = screen
        self.xpos, self.ypos = xpos, ypos
        self.type = type
        if type == "Mushroom":
            self.surface = pygame.image.load('assets/images/consumables/growMushroom.gif')
        elif type == "Flower":
            self.surface = pygame.image.load('assets/images/consumables/flower1.gif')
        elif type == "Star":
            self.surface = pygame.image.load('assets/images/consumables/star1.gif')
        self.rect = self.surface.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.max_height = self.rect.y - 32
        self.rising = False
        self.top = False
        self.falling = False
        self.rise_tick = 0
        self.movement_factor = 1
        self.fall_tick = 0
        self.tick = 0
        self.lastx, self.lasty = self.rect.x, self.rect.y
        self.animate_tick = 0
        self.frame = 0
        self.moving_up = False
        self.y_factor = 1
        self.bounce_tick = 0
        self.y_tick = 0

    def hit_ground(self):
        self.rect.x, self.rect.y = self.lastx, self.lasty
        self.not_falling()


    def is_falling(self):
        if not self.y_factor == 1:
            self.y_factor = 1
        self.falling = True

    def not_falling(self):
        self.falling = False


    def flip_falling(self):
        if not self.falling:
            self.falling = True
            return
        if self.falling:
            self.falling = False
            return

    def blitme(self):
        self.screen.blit(self.surface, self.rect)

    def flip(self):
        self.rect.x, self.rect.y = self.lastx, self.lasty
        self.movement_factor *= -1


    def bounce(self):
        self.not_falling()
        self.rect.x, self.rect.y = self.lastx, self.lasty
        self.y_factor *= -1
        self.moving_up = True
        self.bounce_tick = pygame.time.get_ticks()



    def spawn(self):
        pygame.mixer.music.load('assets/sound/powerup_appears.ogg')
        pygame.mixer.music.play(0)
        self.rising = True


    def update(self):
        self.lastx, self.lasty = self.rect.x, self.rect.y
        if self.falling:
            current = pygame.time.get_ticks()
            if current - self.fall_tick > 8:
                self.fall_tick = current
                self.rect.y += self.y_factor
        if self.rising:
            current = pygame.time.get_ticks()
            if current - self.tick > 20:
                self.tick = current
                self.rect.y -= 1
            if self.rect.y <= self.max_height:
                self.rising = False
                self.top = True
        if self.top:
            if self.type == "Mushroom":
                current = pygame.time.get_ticks()
                if current - self.tick > 8:
                    self.tick = current
                    self.rect.x += self.movement_factor
            if self.type == "Flower":
                this = pygame.time.get_ticks()
                if this - self.animate_tick > 150:
                    self.animate_tick = this
                    self.animate()

            if self.type == "Star" or self.type == "Mushroom":
                this = pygame.time.get_ticks()
                if this - self.animate_tick > 150:
                    self.animate_tick = this
                    self.animate()
                current = pygame.time.get_ticks()
                if current - self.tick > 8:
                    self.tick = current
                    self.rect.x += self.movement_factor
                if self.moving_up:
                    timer = pygame.time.get_ticks()
                    if timer - self.bounce_tick > 500:
                        self.moving_up = False
                        self.is_falling()
                    current = pygame.time.get_ticks()
                    if current - self.y_tick > 8:
                        self.y_tick = current
                        self.rect.y += self.y_factor






    def animate(self):
        if self.type == "Flower":
            if self.frame == 0:
                self.surface = pygame.image.load('assets/images/consumables/flower1.gif')
                self.frame = 1
                return
            if self.frame == 1:
                self.surface = pygame.image.load('assets/images/consumables/flower2.gif')
                self.frame = 2
                return
            if self.frame == 2:
                self.surface = pygame.image.load('assets/images/consumables/flower3.gif')
                self.frame = 0
                return
        if self.type == "Star":
            if self.frame == 0:
                self.surface = pygame.image.load('assets/images/consumables/star1.gif')
                self.frame = 1
                return
            if self.frame == 1:
                self.surface = pygame.image.load('assets/images/consumables/star2.gif')
                self.frame = 0
                return


class Block(Sprite):
    def __init__(self, screen, xpos, ypos, type):
        super(Block, self).__init__()
        self.screen = screen
        self.xpos, self.ypos = xpos, ypos
        self.type = type
        if type == "mystery":
            self.surface = pygame.image.load('assets/images/map_assets/dynamic/mystery_box/mystery_box_bright.png')
        elif type == "brick":
            self.surface = pygame.image.load('assets/images/map_assets/dynamic/bricks/orange_bricks.png')
        elif type == "stair":
            self.surface = pygame.image.load('assets/images/map_assets/metal_tile/metalTile.gif')
        self.rect = self.surface.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.animate_tick = 0
        self.frame = 0
        self.bump = False
        self.top = False
        self.move_tick = 0
        self.max_height = self.rect.y - 16
        self.origin = self.rect.y
        self.complete = False



    def get_brick_status(self):
        return self.complete


    def update(self):
        if self.bump:
            if self.top:
                this = pygame.time.get_ticks()
                if this - self.move_tick > 8:
                    self.move_tick = this
                    self.rect.y += 1
                if self.rect.y >= self.origin:
                    self.rect.y = self.origin
                    self.bump = False
                    self.top = False
                    self.complete = True

            if not self.top:
                this = pygame.time.get_ticks()
                if this - self.move_tick > 8:
                    self.move_tick = this
                    self.rect.y -= 1
                if self.rect.y <= self.max_height:
                    self.top = True
        this = pygame.time.get_ticks()
        if this - self.animate_tick > 150:
            self.animate_tick = this
            self.animate()


    def hit(self):
        pygame.mixer.music.load('assets/sound/bump.ogg')
        pygame.mixer.music.play(0)
        self.bump = True

    def destroy(self):
        print("wip")
    def animate(self):
        if self.type == "mystery" and self.complete:
            self.surface = pygame.image.load('assets/images/map_assets/dynamic/mystery_box/mystery_box_used.png')
            return
        if self.type == "mystery":
            if self.frame == 0:
                self.surface = pygame.image.load('assets/images/map_assets/dynamic/mystery_box/mystery_box_bright.png')
                self.frame = 1
                return
            if self.frame == 1:
                self.surface = pygame.image.load('assets/images/map_assets/dynamic/mystery_box/mystery_box_dark.png')
                self.frame = 2
                return
            if self.frame == 2:
                self.surface = pygame.image.load('assets/images/map_assets/dynamic/mystery_box/mystery_box_normal.png')
                self.frame = 0
                return

    def blitme(self):
        self.screen.blit(self.surface, self.rect)