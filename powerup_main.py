import pygame
from powerup import Power
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Powerup")
    mush = Power(screen, 50, 50, "Mushroom")
    screenrect = screen.get_rect()
    flower = Power(screen, 100, 100, "Flower")

    while True:
        screen.fill((255, 255, 255))
        flower.update()
        flower.blitme()
        mush.update()
        mush.blitme()
        pygame.display.flip()
        if mush.rect.right >= screenrect.right or mush.rect.left <= screenrect.left:
            mush.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mush.spawn()
                    flower.spawn()
                if event.key == pygame.K_UP:
                    mush.flip_falling()


















run_game()