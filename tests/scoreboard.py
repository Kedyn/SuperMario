import pygame

class Score:
    def __init__(self, screen, screenwidth, screenheight):
        pygame.font.init()
        self.myfont = pygame.font.SysFont(None, 30)


        self.screen = screen
        self.width = screenwidth
        self.height = screenheight
        self.score = 0
        self.coins = 0
        self.lives = 3
        self.time = 400
        self.top_buffer = 20


        self.scorestr = "{:,}".format(self.score)
        self.coinstr = "{:,}".format(self.coins)
        self.livestr = "{:,}".format(self.lives)
        self.timestr = "{:,}".format(self.time)

        self.score_surface = self.myfont.render(self.scorestr, False, (0, 0, 0))
        self.coins_surface = self.myfont.render(self.coinstr, False, (0, 0, 0))
        self.lives_surface = self.myfont.render(self.livestr, False, (0, 0, 0))
        self.time_surface = self.myfont.render( self.timestr, False, (0, 0, 0))
        self.tick = 0




    def update(self):
        current = pygame.time.get_ticks()
        if current - self.tick > 500:
            self.tick = current
            self.time -= 1

        self.scorestr = "{:,}".format(self.score)
        self.coinstr = "{:,}".format(self.coins)
        self.livestr = "{:,}".format(self.lives)
        self.timestr = "{:,}".format(self.time)

        self.score_surface = self.myfont.render(self.scorestr, False, (0, 0, 0))
        self.coins_surface = self.myfont.render(self.coinstr, False, (0, 0, 0))
        self.lives_surface = self.myfont.render(self.livestr, False, (0, 0, 0))
        self.time_surface = self.myfont.render( self.timestr, False, (0, 0, 0))
        self.blitme()



        # if you want to use this module.

    def blitme(self):
        self.screen.blit(self.score_surface, (100, self.top_buffer))
        self.screen.blit(self.coins_surface, (200, self.top_buffer))
        self.screen.blit(self.lives_surface, (300, self.top_buffer))
        self.screen.blit(self.time_surface, (400, self.top_buffer))



    def add_score(self, value):
        self.score += value


    def add_coins(self, value):
        self.coins += value

    def sub_live(self):
        self.lives_surface -= 1