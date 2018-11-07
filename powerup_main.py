import pygame
from powerup import Power
import sys
from powerup import Block


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Powerup")
    mush = Power(screen, 50, 50, "Mushroom")
    screenrect = screen.get_rect()
    flower = Power(screen, 100, 100, "Flower")
    star = Power(screen, 200, 200, "Star")
    brick = Block(screen, 50, 50, "mystery")
    stair = Block(screen, 75, 75, "stair")
    flag = False

    while True:
        screen.fill((255, 255, 255))
        brick.update()
        if brick.get_brick_status() and not flag:
            mush.spawn()
            flag = True
        star.update()
        star.blitme()
        stair.blitme()
        flower.update()
        flower.blitme()
        mush.update()
        if flag:
            mush.blitme()
        brick.blitme()
        pygame.display.flip()
        if mush.rect.right >= screenrect.right or mush.rect.left <= screenrect.left:
            mush.flip()
        if mush.rect.bottom >= screenrect.bottom:
            mush.hit_ground()
        if star.rect.right >= screenrect.right or star.rect.left <= screenrect.left:
            star.flip()
        if star.rect.bottom >= screenrect.bottom:
            star.bounce()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mush.spawn()
                if event.key == pygame.K_UP:
                    mush.flip_falling()
                    star.is_falling()
                if event.key == pygame.K_DOWN:
                    brick.hit()


















run_game()