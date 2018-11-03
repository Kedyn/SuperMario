from scene import Scene
from level import Level


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        self.level1 = Level('assets/levels/level1.json', director.screen)

    def update(self):
        self.level1.update()

        if self.level1.done:
            # should move to next level or return to the menu screen
            pass

    def render(self):
        self.director.screen.fill(self.background)

        self.level1.render()
