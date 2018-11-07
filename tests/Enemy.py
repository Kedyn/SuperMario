import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, xpos, ypos, enemy_type):
        super(Enemy, self).__init__()
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render("100", False, (0, 0, 0))
        self.screen = screen
        self.xpos, self.ypos = xpos, ypos
        self.enemy_type = enemy_type

        if enemy_type == "Goomba":
            self.surface = pygame.image.load('../assets/images/enemies/goomba/goomba1.gif')
        elif enemy_type == "Koopa":
            self.surface = pygame.image.load('../assets/images/enemies/koopa/koopa1left.gif')

        self.rect = self.surface.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.direction = -1
        self.frame = 0
        self.ticks = 0
        self.animate_tick = 0
        self.text_tick = 0
        self.lastx = 0
        self.lasty = 0
        self.alive = True
        self.shell_active = False
        self.shell_sound = False
        self.text_y = self.rect.y
        self.text_first = True

    def collide(self):
        self.rect.x, self.rect.y = self.lastx, self.lasty
        self.flip()

    def update(self):
        self.lastx, self.lasty = self.rect.x, self.rect.y
        if self.enemy_type == "Koopa" and not self.alive and self.shell_active:
            self.shell_hit()
        if self.alive:
            current = pygame.time.get_ticks()
            if current - self.ticks > 8:
                self.ticks = current
                self.rect.x += self.direction
                self.animate()
        elif not self.alive:
            if self.text_first:
                self.text_tick = pygame.time.get_ticks()
                self.text_first = False
            this = pygame.time.get_ticks()
            if this - self.text_tick < 500:
                self.screen.blit(self.text, (self.rect.x, self.text_y))
                self.text_y -= 0.25


    def flip(self):
        self.direction *= -1

    def animate_goomba(self):
        current = pygame.time.get_ticks()
        if current - self.animate_tick > 300:
            self.animate_tick = current
            if self.frame == 0:
                self.surface = pygame.image.load('../assets/images/enemies/goomba/goomba1.gif')
                self.frame += 1
                return
            if self.frame == 1:
                self.surface = pygame.image.load('../assets/images/enemies/goomba/goomba2.gif')
                self.frame = 0
                return

    def animate_koopa(self):
        current = pygame.time.get_ticks()
        if current - self.animate_tick > 300:
            self.animate_tick = current
            if self.frame == 0:
                self.surface = pygame.image.load('../assets/images/enemies/koopa/koopa1left.gif')
                self.frame += 1
                return
            if self.frame == 1:
                self.surface = pygame.image.load('../assets/images/enemies/koopa/koopa2left.gif')
                self.frame = 0
                return

    def animate(self):
        if self.enemy_type == "Goomba":
            self.animate_goomba()
        elif self.enemy_type == "Koopa":
            self.animate_koopa()

    def blitme(self):
        if self.direction == 1:
            self.screen.blit(pygame.transform.flip(self.surface, True, False), self.rect)
        else:
            self.screen.blit(self.surface, self.rect)

    def death(self):
        if self.alive:
            pygame.mixer.music.load('../assets/sound/stomp.ogg')
            pygame.mixer.music.play(0)

        self.alive = False

        if self.enemy_type == "Goomba":
            self.surface = self.surface = pygame.image.load('../assets/images/enemies/goomba/goombaDead.gif')
        elif self.enemy_type == "Koopa":
            self.surface = self.surface = pygame.image.load('../assets/images/enemies/koopa/shell.gif')

    def shell_hit(self):
        if not self.shell_sound:
            pygame.mixer.music.load('../assets/sound/kick.ogg')
            pygame.mixer.music.play(0)
            self.shell_sound = True
        current = pygame.time.get_ticks()
        if current - self.ticks > 1:
            self.ticks = current
            self.rect.x += self.direction

    def hit_shell(self):
        if self.enemy_type == "Koopa":
            self.shell_active = True
