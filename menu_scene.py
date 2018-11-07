import pygame

from scene import Scene
from text import Text


class MenuScene(Scene):
    def __init__(self, director, background=(92, 150, 252)):
        super().__init__(director)

        self.background = background
        self.screen = director.screen

        text_rect = pygame.Rect(0, 20, 300, 140)
        text_rect.centerx = director.screen.get_rect().centerx

        #self.logo = Text(text_rect, 140, director.regular_text_color,
        #                 director.screen, "SUPER MARIO")

        menu_rect = pygame.Rect(0, 0, 100, 30)

        menu_rect.center = director.screen.get_rect().center
        menu_rect.y = director.screen.get_rect().bottom - 150

        self.play = Text(menu_rect, 50, director.regular_text_color,
                         director.screen, "PLAY GAME")

        menu_rect.y += 60

        self.high_score = Text(menu_rect, 50, director.regular_text_color,
                               director.screen, "HIGH SCORES")

        self.mouse_on = None

        self.game_logo = pygame.image.load(
            "assets/images/menu_assets/logo.png"
            )
        self.game_logo = pygame.transform.scale(self.game_logo, (400, 300))

    def mousebuttondown(self, button, point):
        self.mouse_on = None

        if self.play.rect.collidepoint(point):
            self.director.set_scene("game")
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
        elif self.high_score.rect.collidepoint(point):
            self.mouse_on = self.high_score

    def render(self):
        self.director.screen.fill(self.background)

        # self.logo.render()

        if self.mouse_on is not None:
            self.mouse_on.color = self.director.special_text_color
            self.mouse_on.prep_img()

        self.play.render()
        self.high_score.render()

        self.screen.blit(self.game_logo, (40, 10))

