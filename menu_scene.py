import pygame

from scene import Scene
from level import Level
from text import Text


class MenuScene(Scene):
    def __init__(self, director, background=(92, 150, 252)):
        super().__init__(director)

        self.background = background
        self.screen = director.screen

        text_rect = pygame.Rect(0, 20, 300, 140)
        text_rect.centerx = director.screen.get_rect().centerx

        menu_rect = pygame.Rect(0, 0, 100, 30)

        menu_rect.center = director.screen.get_rect().center
        menu_rect.y = 288

        self.play = Text(menu_rect, 30, director.regular_text_color,
                         director.screen, "PLAY GAME")

        menu_rect.right = self.play.rect.right
        menu_rect.y += 32

        self.high_score = Text(menu_rect, 30, director.regular_text_color,
                               director.screen, "HIGH SCORES")

        self.mouse_on = None

        self.game_logo = pygame.image.load(
            "assets/images/menu_assets/logo.png"
            )
        self.game_logo = pygame.transform.scale(self.game_logo, (384, 192))

        self.level = Level('assets/levels/level1.json', director.screen)

        self.cursor_image = pygame.image.load(
            "assets/images/consumables/mushroom.png")
        self.cursor_image = pygame.transform.scale(self.cursor_image,
                                                   (25, self.play.rect.height))

        self.on_play = False
        self.on_highscore = False

        self.theme_song = pygame.mixer.music.load("assets/sound/mario_theme_song.ogg")

    def reset(self):
        # play music
        pygame.mixer.music.play(-1)


    def mousebuttondown(self, button, point):
        self.mouse_on = None

        if self.play.rect.collidepoint(point):
            self.director.set_scene("game")
            pygame.mixer.music.pause()
        elif self.high_score.rect.collidepoint(point):
            self.director.set_scene("scores")

    def update(self):
        point = pygame.mouse.get_pos()

        if self.mouse_on is not None:
            self.mouse_on.color = self.director.regular_text_color
            self.mouse_on.prep_img()
            self.mouse_on = None

        if self.play.rect.collidepoint(point):
            self.mouse_on = self.play
            self.on_play = True
            self.on_highscore = False
        elif self.high_score.rect.collidepoint(point):
            self.mouse_on = self.high_score
            self.on_play = False
            self.on_highscore = True

    def render(self):
        self.director.screen.fill(self.background)

        # self.logo.render()

        if self.mouse_on is not None:
            self.mouse_on.color = self.director.special_text_color
            self.mouse_on.prep_img()

        self.level.render()

        self.play.render()
        self.high_score.render()

        self.screen.blit(self.game_logo, (64, 64))

        if self.on_play:
            self.screen.blit(self.cursor_image, (165, self.play.rect.y))  # play cursor
        elif self.on_highscore:
            self.screen.blit(self.cursor_image, (165, self.high_score.rect.y))  # high score cursor
