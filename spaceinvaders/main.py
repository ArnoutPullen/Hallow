#https://www.youtube.com/watch?v=Ve-BvoCVN40

import pygame, sys
from pygame.locals import *

screenWidth = 800
screenHeight = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

shipWidth = 78
shipX = (screenWidth * 0.45)
shipY = (screenHeight * 0.8)
shipMoveX = 0
shipX += shipMoveX

#colors
black=(0,0,0)
blue=(0,0, 255)
green=(0,128,0)
red=(255,0,0)
white=(255,255,255)
yellow=(255,255,0)

backgroundImage =  pygame.image.load("background.png")
spaceShipImage =  pygame.image.load("spaceship7.png")
wallImage =  pygame.image.load("wall.png")
enemyImage =  pygame.image.load("enemy.png")
bulletImage =  pygame.image.load("bullet.png")

numberEnemies = 5
enemies = []


def app_quit():
    pygame.quit()
    sys.exit("System exit.")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship7.png").convert()
        self.image.set_colorkey(white)#make white transparant
        self.rect = self.image.get_rect()
        self.rect.center = 300, 500

    def update(self):
        self.shipX = 0
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.shipX = -2
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            self.shipX = 2
        self.rect.x += self.shipX

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = 100, 300

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = 150, 100

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = 400,500

    def update(self):
        self.bulletX = 0
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.bulletX = -2
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            self.bulletX = 2
        self.rect.x += self.bulletX
        self.bulletY = 0
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.bulletY = -2
        elif event.type == KEYUP and event.key == K_SPACE:
            self.bulletY = -2
        self.rect.y += self.bulletY


allSprites = pygame.sprite.Group()

player = Player()
wall = Wall()
enemy = Enemy()
bullet = Bullet()
allSprites.add(player,wall,enemy,bullet)

running = True
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            running = False
            app_quit()

    if shipX >= screenWidth - shipWidth:
        shipX -= 0
    if shipX < 0:
        shipX -= 0

    allSprites.update()

    screen.fill(black)
    allSprites.draw(screen)
    pygame.display.flip()

pygame.quit()
