import pygame, sys
from pygame.locals import *
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

#display specs
display_width = 800
display_height = 600

#colors
black=(0,0,0)
blue=(0,0, 255)
green=(0,128,0)
red=(255,0,0)
white=(255,255,255)
yellow=(255,255,0)

#center of image
shipx = (display_width * 0.45)
shipy = (display_height * 0.8)


#movement ship is 0
shipxchange = 0

#width of spaceship
spaceshipwidth = 78

#location of the wall
wallx = 0
wally = 0

enemyx = 0
enemyy = 0

bulletx = (shipx)
bullety = (shipy)
bulletychange = 0

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invaders')
spaceShipImage = pygame.image.load('spaceship7.png')
spaceshipRect = pygame.Rect(8,6, 71, 79)
wallImage1 = pygame.image.load('wall.png')
wallRect = pygame.Rect(0,0,58,17)
enemyImage = pygame.image.load('enemy.png')
enemyRect = pygame.Rect(0,0,30,30)

bulletShootImage = pygame.image.load('bullet.png')
bulletShootRect = pygame.Rect(0,0,15,15)

pygame.Surface.set_clip

while True: # main game loop
    DISPLAYSURF.fill(white)
    DISPLAYSURF.blit(spaceShipImage, (shipx, shipy))
    DISPLAYSURF.blit(wallImage1, (100, 400))
    DISPLAYSURF.blit(wallImage1, (300, 400))
    DISPLAYSURF.blit(wallImage1, (500, 400))
    DISPLAYSURF.blit(wallImage1, (700, 400))
    DISPLAYSURF.blit(enemyImage, (100, 100))


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_LEFT:
            shipxchange += -5
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            shipxchange += 5
        if event.type == KEYUP and event.key == K_LEFT:
            shipxchange += 5
        elif event.type == KEYUP and event.key == K_RIGHT:
            shipxchange += -5

    shipx += shipxchange
    shipxMoment = shipx + shipxchange

    #bounderies for the spaceship
    if shipx >= display_width - spaceshipwidth:
        shipx -= shipxchange
    if shipx < 0:
        shipx -= shipxchange

    #shooting bullets
    if event.type == KEYDOWN and event.key == K_SPACE:
        bulletychange += -1
        DISPLAYSURF.blit(bulletShootImage,(shipxMoment, bullety))
    elif event.type == KEYUP and event.key == K_SPACE:
        bulletychange += -1
        DISPLAYSURF.blit(bulletShootImage,(shipxMoment, bullety))

    bullety += bulletychange

    pygame.display.update()
    fpsClock.tick(FPS)
