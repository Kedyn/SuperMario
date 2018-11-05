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

    def is_falling(self):
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
                self.rect.y += 1
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
                    print(self.animate_tick)
                    self.animate_tick = this
                    self.animate()

            if self.type == "Star":
                print("wip")

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

