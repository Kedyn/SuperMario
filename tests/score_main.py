import pygame
import sys
from scoreboard import Score


def run_game():
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Powerup")
    score = Score(screen, width, height)
    while True:
        screen.fill((255, 255, 255))

        score.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score.add_score(100)
                if event.key == pygame.K_UP:
                    score.add_coins(1)


run_game()