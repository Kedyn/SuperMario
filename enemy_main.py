import pygame
from Enemy import Enemy
import sys


def run_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Goomba")
    goomba = Enemy(screen, 50, 50, "Goomba")
    screenrect = screen.get_rect()
    koopa = Enemy(screen, 100, 100, "Koopa")

    while True:
        screen.fill((255, 255, 255))
        goomba.update()
        goomba.blitme()
        koopa.update()
        koopa.blitme()
        pygame.display.flip()
        if goomba.rect.left < screenrect.left:
            goomba.rect.x, goomba.rect.y = goomba.lastx, goomba.lasty
            goomba.flip()
        elif goomba.rect.right > screenrect.right:
            goomba.rect.x, goomba.rect.y = goomba.lastx, goomba.lasty
            goomba.flip()


        if koopa.rect.left < screenrect.left:
            koopa.rect.x, koopa.rect.y = koopa.lastx, koopa.lasty
            koopa.flip()
        elif koopa.rect.right > screenrect.right:
            koopa.rect.x, koopa.rect.y = koopa.lastx, koopa.lasty
            koopa.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not koopa.alive:
                        koopa.hit_shell()
                    print("DIE!")
                    goomba.death()
                    koopa.death()



















run_game()