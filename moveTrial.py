import pygame
import time
pygame.init()


screen_width = 500
screen_height = 480

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Movement Trial')
# game_screen.fill(GREEN)

walkRight = [pygame.image.load('images/small_mario/R1.gif'), pygame.image.load('images/small_mario/R2.gif'),
             pygame.image.load('images/small_mario/R3.gif')]
walkLeft = [pygame.image.load('images/small_mario/L1.gif'), pygame.image.load('images/small_mario/L2.gif'),
            pygame.image.load('images/small_mario/L3.gif')]

pacRight = [pygame.image.load('Pacman/r1.png'), pygame.image.load('Pacman/r2.png')]
pacLeft = [pygame.image.load('Pacman/L1.png'), pygame.image.load('Pacman/L2.png')]

pacUp = [pygame.image.load('Pacman/U1.png'), pygame.image.load('Pacman/U2.png')]
pacDown = [pygame.image.load('Pacman/D1.png'), pygame.image.load('Pacman/D2.png')]

pacman = pygame.image.load('Pacman/standby.png')

bg = pygame.image.load('images/bgTest.jpg')

char = pygame.image.load('images/small_mario/R1.gif')

playerImage = pygame.image.load('images/small_mario/R1.gif')
player = playerImage.get_rect()

# Clock to control fps
clock = pygame.time.Clock()

# Draw a rect at (x,y) position and width and height
x = 50
y = 400
vel = 5
width = 64
height = 64
isJump = False
jumpCount = 10  # airtime delay after a jump
left = False
right = False
up = False
down = False
walkCount = 0

# player = pygame.draw.rect(game_screen, RED, (x, y, width, height))


def redraw_window():
    global walkCount
    # game_screen.fill(GREEN)  # The purpose of this line is to only draw one rect per "refresh"
    game_screen.blit(bg, (0, 0))
    # player = pygame.draw.rect(game_screen, RED, (x, y, width, height))  # (x-pos, y-pos, shapeWidth, shapeHeight)

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        game_screen.blit(walkLeft[walkCount % 2], (x, y))
        walkCount += 1
    elif right:
        game_screen.blit(walkRight[walkCount % 2], (x, y))
        walkCount += 1
    elif up:
        game_screen.blit(pacUp[walkCount % 2], (x, y))
        walkCount += 1
    elif down:
        game_screen.blit(pacDown[walkCount % 2], (x, y))
        walkCount += 1
    else:
        game_screen.blit(char, (x, y))

    pygame.display.update()


game_running = True
# Main loop
while game_running:
    clock.tick(25)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:  # player.left > 0
        x -= vel
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
        up = False
        down = False
    elif keys[pygame.K_UP] and y > 0:
        y -= vel
        right = False
        left = False
        up = True
        down = False
    elif keys[pygame.K_DOWN] and y < screen_height:
        y += vel
        right = False
        left = False
        up = False
        down = True
    else:
        right = False
        left = False
        up = False
        down = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_UP] and y > 0:
            y -= vel
            right = False
            left = False
        if keys[pygame.K_DOWN] and y < screen_height:
            y += vel
            right = False
            left = False
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * .5 * neg  # to the power of..2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redraw_window()

pygame.quit()
