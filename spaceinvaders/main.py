
import sys, pygame
import random
from pygame.locals import *
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaders')
background = 40, 40, 40  # background color
white = (255,255,255)
black = (0,0,0)
pointsSpaceInvaders = 0
pygame.mixer.init()

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
        shootsound.play()

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
        self.image = pygame.image.load('bulletenemy.png').convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speed = [0, 10] #bullet is going down with 10px

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

class Enemy2Bullet:
    def __init__(self):
        self.image = pygame.image.load('bulletenemy.png').convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speed = [0, 20]

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

class Enemy3Bullet:
    def __init__(self):
        self.image = pygame.image.load('bulletenemy.png').convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speed = [0, 10] #bullet is going down with 10px

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

class Enemy2:
    def __init__(self):
        self.image = pygame.image.load('enemy1.png')
        self.rect = self.image.get_rect()
        self.speed = [-4, 0]

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

class Enemy3:
    def __init__(self):
        self.image = pygame.image.load('enemy2.png')
        self.rect = self.image.get_rect()
        self.speed = [6, 0]

    def Update(self):
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

shootsound = pygame.mixer.Sound('lasershoot.wav') #plays this sound when shooting
explosionsound = pygame.mixer.Sound('explosion.wav') #plays this sound when hitting enemy
pygame.mixer.music.load('musicbackground.wav')
pygame.mixer.music.set_volume(0.4)

spawnenemy = USEREVENT + 1 #spawn enemy
enemyshoot = USEREVENT + 2 #spawn enemy bullet
spawnenemy2 = USEREVENT + 3 #spawn enemy right
enemyshoot2 = USEREVENT + 4 #spawn enemy right bullet
spawnenemy3 = USEREVENT + 5 #spawn enemy right
enemyshoot3 = USEREVENT + 6 #spawn enemy right bullet
pygame.time.set_timer(spawnenemy, 2000) #spawn enemy after 2 sec
pygame.time.set_timer(enemyshoot, 3100) #spawn enemy bullet after 3,1 sec
pygame.time.set_timer(spawnenemy2, 2500) #spawn enemy right after 2,5 sec
pygame.time.set_timer(enemyshoot2, 3600) #spawn enemy bullet right after 3,6 sec
pygame.time.set_timer(spawnenemy3, 4000) #spawn enemy right after 4 sec
pygame.time.set_timer(enemyshoot3, 4600) #spawn enemy bullet right after 4,6 sec

#lists
objectList = list()
playerBulletList = list()
enemyBulletList = list()
enemy2BulletList = list()
enemy3BulletList = list()
wallList = list()
enemyList = list()
enemy2List = list()
enemy3List = list()
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

# pygame.mixer.music.play(loops=-1) #loop it
while True:
    pygame.time.Clock().tick(60) #60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            print(pointsSpaceInvaders)
            sys.exit()

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

        elif event.type == spawnenemy2:
            enemy2 = Enemy2()
            enemy2.rect = enemy2.rect.move([900,150])
            enemy2List.insert(True, enemy2)
            objectList.insert(True, enemy2)

        elif event.type == enemyshoot2:
            enemyBullet2 = Enemy2Bullet()
            enemyBullet2.rect = enemyBullet2.rect.move(enemy2.rect.x + 25, enemy2.rect.y)
            enemy2BulletList.insert(True, enemyBullet2)
            objectList.insert(True, enemyBullet2)

        elif event.type == spawnenemy3:
            enemy3 = Enemy3() #class will be called
            enemy3.rect = enemy3.rect.move([-25,250]) #starting position of the enemy
            enemy3List.insert(True, enemy3) #enemy will be added in enemyList
            objectList.insert(True, enemy3) #enemy will be added in objectList

        elif event.type == enemyshoot3:
            enemyBullet3 = Enemy3Bullet()
            enemyBullet3.rect = enemyBullet3.rect.move(enemy3.rect.x + 25, enemy3.rect.y)
            enemy3BulletList.insert(True, enemyBullet3)
            objectList.insert(True, enemyBullet3)

    for bullet in playerBulletList:
        for enemy in enemyList:

            if bullet.rect.colliderect(enemy): #if player bullet hits enemy, remove bullet and enemy
                enemyList.remove(enemy)
                objectList.remove(enemy)
                pointsSpaceInvaders += 1000 #add 1000 points
                explosionsound.play() #play sound

                playerBulletList.remove(bullet)
                objectList.remove(bullet)

    for bullet in playerBulletList:
        for enemy2 in enemy2List:

            if bullet.rect.colliderect(enemy2): #if player bullet hits enemy, remove bullet and enemy
                enemy2List.remove(enemy2)
                objectList.remove(enemy2)
                pointsSpaceInvaders += 1000
                explosionsound.play()

                playerBulletList.remove(bullet)
                objectList.remove(bullet)

    for bullet in playerBulletList:
        for enemy3 in enemy3List:

            if bullet.rect.colliderect(enemy3): #if player bullet hits enemy, remove bullet and enemy
                enemy3List.remove(enemy3)
                objectList.remove(enemy3)
                pointsSpaceInvaders += 1000
                explosionsound.play()

                playerBulletList.remove(bullet)
                objectList.remove(bullet)

    for bullet in playerBulletList:
        for wall_1 in wallList:

            if bullet.rect.colliderect(wall_1): #if player bullet hits wall, remove bullet
                playerBulletList.remove(bullet)
                objectList.remove(bullet)

    for enemyBullet in enemyBulletList:
        for wall_1 in wallList:

            if enemyBullet.rect.colliderect(wall_1): #if enemy bullet hits wall, remove bullet
                enemyBulletList.remove(enemyBullet)
                objectList.remove(enemyBullet)

    for enemy2Bullet in enemy2BulletList:
            for wall_1 in wallList:

                if enemy2Bullet.rect.colliderect(wall_1): #if enemy bullet hits wall, remove bullet
                    enemy2BulletList.remove(enemy2Bullet)
                    objectList.remove(enemy2Bullet)

    for enemy3Bullet in enemy3BulletList:
            for wall_1 in wallList:

                if enemy3Bullet.rect.colliderect(wall_1): #if enemy bullet hits wall, remove bullet
                    enemy3BulletList.remove(enemy3Bullet)
                    objectList.remove(enemy3Bullet)

    for enemyBullet in enemyBulletList:
        if enemyBullet.rect.colliderect(player):
            print(pointsSpaceInvaders)
            sys.exit()

    for enemy2Bullet in enemy2BulletList:
        if enemy2Bullet.rect.colliderect(player):
            print(pointsSpaceInvaders)
            sys.exit()

    for enemy3Bullet in enemy3BulletList:
        if enemy3Bullet.rect.colliderect(player):
            print(pointsSpaceInvaders)
            sys.exit()

    screen.fill(background)

    for object in objectList:
        object.Update()

    pygame.display.flip()
