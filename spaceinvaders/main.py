import pygame, sys
from pygame.locals import *
import random

screenWidth = 800
screenHeight = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

shipWidth = 78

#colors
black=(0,0,0)
blue=(0,0, 255)
green=(0,128,0)
red=(255,0,0)
white=(255,255,255)
yellow=(255,255,0)

backgroundImage = pygame.image.load("background.png")
spaceShipImage = pygame.image.load("spaceship7.png")
wallImage = pygame.image.load("wall.png")
enemyImage = pygame.image.load("enemy.png")
bulletPlayerImage = pygame.image.load("bullet.png")

def app_quit():
    pygame.quit()
    sys.exit("System exit.")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship7.png").convert()
        self.image.set_colorkey(white)#make white transparant
        self.rect = self.image.get_rect()
        self.rect.centerx = screenWidth / 2
        self.rect.bottom = screenHeight - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.speedx = -2
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            self.speedx = 2
        self.rect.x += self.speedx
        if self.rect.right > screenWidth:
            self.rect.right = screenWidth
        if self.rect.left < 0:
            self.rect.left = 0

    def shootPlayer(self):
        bulletPlayer = BulletPlayer(self.rect.centerx, self.rect.top)
        allSprites.add(bulletPlayer)
        bulletsPlayer.add(bulletPlayer)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randrange(0, 200)
        self.speedx = random.randrange(1,2)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > screenWidth:
            self.rect.x = 0
            self.rect.y = random.randrange(0, 250)
            self.speedx = random.randrange(1,3)
        if self.rect.x > screenWidth:
            self.kill()

    # def shootEnemy(self):
    #     bulletEnemy = BulletEnemy(self.rect.centerx, self.rect.top)
    #     allSprites.add(bulletEnemy)
    #     bulletsEnemy.add(bulletEnemy)

class BulletPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
#
# class BulletEnemey(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("bulletenemy.png").convert()
#         self.image.set_colorkey(white)
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y
#         self.rect.centerx = x
#         self.speedy = 3
#
#     def update(self):
#         self.rect.y += self.speedy
#         if self.rect.bottom > screenHeight:
#             self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = 100, 300

allSprites = pygame.sprite.Group()
enemy = pygame.sprite.Group()
bulletsPlayer = pygame.sprite.Group()
# bulletsEnemy = pygame.sprite.Group()
player = Player()
wall = Wall()
allSprites.add(player,wall,enemy,bulletsPlayer)

for i in range(1):
    e = Enemy()
    allSprites.add(e)
    enemy.add(e)

running = True
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            running = False
            app_quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shootPlayer()


    allSprites.update()
    screen.fill(black)
    allSprites.draw(screen)
    pygame.display.flip()

pygame.quit()
