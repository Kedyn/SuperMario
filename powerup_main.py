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
    brick1 = Block(screen, 100, 100, "mystery")
    brick2 = Block(screen, 200, 200, "mystery")
    flag = False
    flag2 = False
    flag3 = False

    while True:
        screen.fill((255, 255, 255))
        brick.update()
        brick1.update()
        brick2.update()
        if brick.get_brick_status() and not flag:
            mush.spawn()
            flag = True
        if brick1.get_brick_status() and not flag2:
            flower.spawn()
            flag2 = True
        if brick2.get_brick_status() and not flag3:
            star.spawn()
            flag3 = True
        if flag2:
            flower.blitme()
        if flag3:
            star.blitme()

        star.update()
        flower.update()
        mush.update()
        if flag:
            mush.blitme()
        brick.blitme()
        brick1.blitme()
        brick2.blitme()
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
                    brick1.hit()
                    brick2.hit()


















run_game()