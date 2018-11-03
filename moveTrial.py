"""This acts as the main
Things that are new: moveTrial.py, settings.py, sprites.py"""
import pygame as pg
from settings import *
from sprites import *


class Game:
    def __init__(self):
        """Initialize game window, etc"""
        pg.init()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True

    def new(self):
        """Start a new game"""
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        p1 = Platform(0, screen_height - 40, screen_width, 20)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(screen_width/2 - 50, screen_height * 3/4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.run()

    def run(self):
        """Game loop"""
        self.playing = True

        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        """Game loop update"""
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y = lowest.rect.top + .5  # the .5 is to make sure it is colliding w/ the floor
                    self.player.vel.y = 0
                    self.player.jumping = False

    def events(self):
        """Game loop events"""

        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self):
        """Game loop draw"""
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        """game splash/start screen"""
        pass

    def show_go_screen(self):
        """game over/continue"""
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()
pg.quit()
