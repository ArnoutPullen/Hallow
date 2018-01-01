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
wallx = 50
wally = 300

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invaders')
spaceShipImage = pygame.image.load('spaceship7.png')
spaceshipRect = pygame.Rect(8,6, 71, 79) #rectangle of ship
#wallImage = pygame.image.load('wall.png')
#wallRect = pygame.Rect(0,0,58,17)

while True: # main game loop
    DISPLAYSURF.fill(white)
    DISPLAYSURF.blit(spaceShipImage, (shipx, shipy))
    #DISPLAYSURF.blit(wallImage, (wallx, wally))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_LEFT:
            shipxchange += -5
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            shipxchange += +5
        if event.type == KEYUP and event.key == K_LEFT:
            shipxchange += +5
        elif event.type == KEYUP and event.key == K_RIGHT:
            shipxchange += -5

    shipx += shipxchange

    #bounderies for the spaceship
    if shipx >= display_width - spaceshipwidth:
        shipx -= shipxchange
    if shipx < 0:
        shipx -= shipxchange

    pygame.display.update()
    fpsClock.tick(FPS)
