
import sys, pygame
import random
from pygame.locals import *
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaders')
background = 40, 40, 40  # Background RGB color.
white = (255,255,255)

class Player:
    def __init__(self):
        self.image = pygame.image.load('spaceship3.png').convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.leftSpeed = [-5, 0]
        self.rightSpeed = [5, 0]
        self.goingLeft = False #going left is always False except when pressing down left key
        self.goingRight = False #going right is always False except when pressing down right key

    def Update(self):
        if self.goingLeft:
            self.rect = self.rect.move(self.leftSpeed) #rect update with leftspeed
        elif self.goingRight:
            self.rect = self.rect.move(self.rightSpeed) #rect update with rightspeed
        screen.blit(self.image, self.rect)

class PlayerBullet:
    def __init__(self):
        self.image = pygame.image.load('bullet.png').convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.speed = [0, -4] #vertically going 7 px up

    def Update(self):
        self.rect = self.rect.move(self.speed) #rect update with speed(-7)
        screen.blit(self.image, self.rect)

        if self.rect.y < 0:
            playerBulletList.remove(self)  #remove bullet from playerBulletList when going above the screen
            objectList.remove(self) #remove bullet from objectlist when going above the screen

class Wall:
    def __init__(self):
        self.image = pygame.image.load('wall2.png')
        self.rect = self.image.get_rect()

    def Update(self):
        screen.blit(self.image, self.rect)

class EnemyBullet:
    def __init__(self):
        self.image = pygame.image.load('bulletenemy.png')
        self.rect = self.image.get_rect()
        self.speed = [0, 10] #bullet is going down with 30px

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

class EnemyRightBullet:
    def __init__(self):
        self.image = pygame.image.load('bulletenemy.png')
        self.rect = self.image.get_rect()
        self.speed = [0, 20]

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('enemy6.png')
        self.rect = self.image.get_rect()
        self.speed = [4,0] #enemy is going horizontally with 4px, vertically 0px

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

class EnemyRight:
    def __init__(self):
        self.image = pygame.image.load('enemy6.png')
        self.rect = self.rect.move([700,400])
        self.rect = self.image.get_rect()
        self.speed = [-4, 0]
        objectList.insert(True, EnemyRight)

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)


spawnenemy = USEREVENT + 1 #spawn enemy
enemyshoot = USEREVENT + 2 #spawn enemy bullet
pygame.time.set_timer(spawnenemy, 2000) #spawn enemy after 2 sec
pygame.time.set_timer(enemyshoot, 3126) #spawn enemy bullet after 3 sec

#lists
objectList = list()
playerBulletList = list()
enemyBulletList = list()
enemyRightBulletList = list()
wallList = list()
enemyList = list()
enemyRightList = list()
playerList = list()

player = Player()
player.rect = player.rect.move([100,500]) #starting position player
objectList.insert(True, player)

#walls
wall_1 = Wall()
wall_1.rect = wall_1.rect.move([100,400])
wallList.insert(True, wall_1)
objectList.insert(True, wall_1)

wall_2 = Wall()
wall_2.rect = wall_2.rect.move([300,400])
wallList.insert(True, wall_2)
objectList.insert(True, wall_2)

wall_3 = Wall()
wall_3.rect = wall_3.rect.move([500,400])
wallList.insert(True, wall_3)
objectList.insert(True, wall_3)

wall_4 = Wall()
wall_4.rect = wall_4.rect.move([700,400])
wallList.insert(True, wall_4)
objectList.insert(True, wall_4)

while True:
    pygame.time.Clock().tick(60) #60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT: #if goingLeft = True then spaceship will go left
                player.goingLeft = True
            elif event.key == K_RIGHT: #if goingRight = True then spaceship will go right
                player.goingRight = True

        elif event.type == KEYUP:
            if event.key == K_LEFT: #if goingLeft = False then goingLeft will be deactivated
                player.goingLeft = False
            elif event.key == K_RIGHT: #if goingRight = False then goingRight will be deactivated
                player.goingRight = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                playerBullet = PlayerBullet() #class will be called
                playerBullet.rect = playerBullet.rect.move(player.rect.x + 25, player.rect.y) #position of the bullet is player position + 25px to the right
                playerBulletList.insert(True, playerBullet) #playerBullet will be added in playerBulletList
                objectList.insert(True, playerBullet) #playerBullet will be added in objectList

        elif event.type == spawnenemy:
            enemy = Enemy() #class will be called
            enemy.rect = enemy.rect.move([-25,50]) #starting position of the enemy
            enemyList.insert(True, enemy) #enemy will be added in enemyList
            objectList.insert(True, enemy) #enemy will be added in objectList

        elif event.type == enemyshoot:
            enemyBullet = EnemyBullet() #class will be called
            enemyBullet.rect = enemyBullet.rect.move(enemy.rect.x + 25, enemy.rect.y) #position of the bullet is enemy position + 25px to the right
            enemyBulletList.insert(True, enemyBullet) #enemybullet will be added in enemyBulletList
            objectList.insert(True, enemyBullet) #enemybullet will be added in objectList

        # elif event.type == spawnenemy:
        #     enemy2 = EnemyRight()
        #     enemy2.rect = enemy.rect.move([100,100])
        #     enemyRightList.insert(True, enemy2)
        #     objectList.insert(True, enemy2)
        # 
        # elif event.type == enemyshoot:
        #     enemyBullet2 = EnemyRightBullet()
        #     enemyBullet2.rect = enemyBullet2.rect.move(enemy.rect.x + 25, enemy.rect.y)
        #     enemyRightBulletList.insert(True, enemyBullet2)
        #     objectList.insert(True, enemyBullet2)


    for bullet in playerBulletList:
        for enemy in enemyList:

            if bullet.rect.colliderect(enemy): #if player bullet hits enemy, remove bullet and enemy
                enemyList.remove(enemy)
                objectList.remove(enemy)

                playerBulletList.remove(bullet)
                objectList.remove(bullet)

    for bullet in playerBulletList:
        for wall_1 in wallList:

            if bullet.rect.colliderect(wall_1): #if player bullet hits wall, remove bullet
                playerBulletList.remove(bullet)
                objectList.remove(bullet)

    # for enemyBullet in enemyBulletList:
    #     for player in playerList:
    #
    #         if bullet.rect.colliderect(player):
    #             playerList.remove(player)
    #             objectList.remove(player)

    screen.fill(background)

    for object in objectList:
        object.Update()

    pygame.display.flip()
