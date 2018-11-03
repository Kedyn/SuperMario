import pygame

from scene import Scene


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

    def update(self):
        pass

    def render(self):
        self.director.screen.fill(self.background)
