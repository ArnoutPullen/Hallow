# Standard initialisation stuff.
import sys, pygame
import random
from pygame.locals import *
pygame.init()

# Set game window.
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Witchflight')
background = 35, 35, 80     # Background RGB color.

# Score Variables.
global obstaclesDestroyed
obstaclesDestroyed = 0

global applesCollected
applesCollected = 0

global potionsCollected
potionsCollected = 0

# Spawn control variables.
global appleSpawned
appleSpawned = False

global pumpkinSpawned
pumpkinSpawned = False

global potionSpawned
potionSpawned = False

global cloudSpawned
cloudSpawned = False

class fireball:
    def __init__(self):
        self.image1 = pygame.image.load('images/fireball1.png')
        self.image2 = pygame.image.load('images/fireball2.png')
        self.rect = self.image1.get_rect()
        self.speed = [28, 0]
        self.flippedImage = False

    def update(self):

        # Move the fireball to the right.
        self.rect = self.rect.move(self.speed)

        # Constantly switch between image 1 and 2.
        if (self.flippedImage == True):
            screen.blit(self.image1, self.rect)
            self.flippedImage = False
        else:
            screen.blit(self.image2, self.rect)
            self.flippedImage = True

        # If the fireball is off the screen, remove it.
        if self.rect.x > 800:
            fireballList.remove(self)
            objectList.remove(self)

class witch:
    def __init__(self):

        # Image variables.
        self.image = pygame.image.load('images/witch.png')
        self.rect = self.image.get_rect()

        # Control variables.
        self.upSpeed = [0, -20]
        self.downSpeed = [0, 20]
        self.spacebarPressed = False

        # Damage handling variables.
        self.damageAnimation = False
        self.hitpoints = 4
        self.loopedAnimation = 0
        self.frameCounter = 0

    def shootFireball(self, source):

        # Create a fireball.
        activeFireball = fireball()
        activeFireball.rect.x = source.rect.x + 65
        activeFireball.rect.y = source.rect.y + 15

        # Add the created fireball to relevant lists.
        objectList.insert(True, activeFireball)
        fireballList.insert(True, activeFireball)

    def update(self):
        if event.type == KEYDOWN:

            # Moving up and down.
            if event.key == K_UP and self.rect.top > 18:
                self.rect = self.rect.move(self.upSpeed)
            if event.key == K_DOWN and self.rect.bottom < (height - 18):
                self.rect = self.rect.move(self.downSpeed)

            # Shooting a fireball.
            if event.key == K_SPACE and self.spacebarPressed == False:
                self.shootFireball(self)
                self.spacebarPressed = True
        if event.type == KEYUP:
            if event.key == K_SPACE and self.spacebarPressed == True:
                self.spacebarPressed = False

        # Showing the witch.
        if self.damageAnimation == True:

            # The first 5 frames after taking damage, do not show the witch.
            if self.frameCounter <= 5:
                self.frameCounter += 1

            # The next 5 frames, show the witch.
            elif self.frameCounter <= 10:
                screen.blit(self.image, self.rect)
                self.frameCounter += 1

            # The animation is done, which we add to the loopedAnimation.
            elif self.frameCounter > 10:
                self.frameCounter = 0
                self.loopedAnimation += 1

            # If the animation has looped a number of times, stop it.
            if self.loopedAnimation == 5:
                self.damageAnimation = False
                self.loopedAnimation = 0
        else:
            screen.blit(self.image, self.rect)

class apple:
    def __init__(self):
        self.image = pygame.image.load('images/apple.png')
        self.rect = self.image.get_rect()
        self.speed = [-10, 0]

    def update(self):

        # Move and show the apple.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the apple is off the screen, remove it.
        if self.rect.x < -50:
            appleList.remove(self)
            objectList.remove(self)

class potion:
    def __init__(self):
        self.image = pygame.image.load('images/potion.png')
        self.rect = self.image.get_rect()
        self.speed = [-10, 0]

    def update(self):

        # Move and show the potion.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the potion is off the screen, remove it.
        if self.rect.x < -50:
            potionList.remove(self)
            objectList.remove(self)

class cloud:
    def __init__(self):
        self.image = pygame.image.load('images/cloud.png')
        self.rect = self.image.get_rect()
        self.speed = [-10, 0]

    def update(self):

        # Move and show the cloud.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the cloud is off the screen, remove it.
        if self.rect.x < -50:
            obstacleList.remove(self)
            objectList.remove(self)

class pumpkin:
    def __init__(self):
        self.image = pygame.image.load('images/pumpkin.png')
        self.rect = self.image.get_rect()
        self.speed = [-20, 0]

    def update(self):

        # Move and show the pumpkin.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the pumpkin is off the screen, remove it.
        if self.rect.x < -50:
            obstacleList.remove(self)
            objectList.remove(self)

# Singular objects.
player = witch()

# Object lists.
objectList = list()
fireballList = list()
obstacleList = list()
potionList = list()
appleList = list()

objectList.insert(True, player)

# Set custom events.
SPAWNAPPLE = USEREVENT + 1
SPAWNPUMPKIN = USEREVENT + 2
pygame.time.set_timer(SPAWNAPPLE, 2500)
pygame.time.set_timer(SPAWNPUMPKIN, 1500)

while True: # Main game loop.

    # Run the game at 60 frames per second.
    pygame.time.Clock().tick(30)

    # Event catcher. If statements allow us to decide what happens per event within this for loop.
    # ( Events such as quitting the game, pressing a key, moving the mouse, etc. )
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Periodically spawn an apple.
    if event.type == SPAWNAPPLE and appleSpawned == False:

        appleCollectable = apple()
        randomInt = random.randint(25, 495)
        appleCollectable.rect.x += 800
        appleCollectable.rect.y += randomInt

        appleList.insert(True, appleCollectable)
        objectList.insert(True, appleCollectable)

        appleSpawned = True

    elif event.type != SPAWNAPPLE and appleSpawned == True:
        appleSpawned = False

    # Periodically spawn a pumpkin.
    if event.type == SPAWNPUMPKIN and pumpkinSpawned == False:

        pumpkinObstacle = pumpkin()
        randomInt = random.randint(25, 495)
        pumpkinObstacle.rect.x += 800
        pumpkinObstacle.rect.y += randomInt

        obstacleList.insert(True, pumpkinObstacle)
        objectList.insert(True, pumpkinObstacle)

        pumpkinSpawned = True

    elif event.type != SPAWNPUMPKIN and pumpkinSpawned == True:
        pumpkinSpawned = False

    # (TEMP) Spawn pumpkins from the right side of the map by pressing Q.
    if event.type == KEYDOWN:
        if event.key == K_q:

            pumpkinObstacle = pumpkin()
            randomInt = random.randint(25, 495)
            pumpkinObstacle.rect.x += 800
            pumpkinObstacle.rect.y += randomInt

            obstacleList.insert(True, pumpkinObstacle)
            objectList.insert(True, pumpkinObstacle)

    # (TEMP) spawn apples from the right side of the map by pressing W.
    if event.type == KEYDOWN:
        if event.key == K_w:

            appleCollectable = apple()
            randomInt = random.randint(25, 495)
            appleCollectable.rect.x += 800
            appleCollectable.rect.y += randomInt

            appleList.insert(True, appleCollectable)
            objectList.insert(True, appleCollectable)

    # (TEMP) Collision handling.
    for object in objectList:

        # Collecting an apple.
        for appleToCollect in appleList:
            if appleToCollect.rect.colliderect(player):

                appleList.remove(appleToCollect)
                objectList.remove(appleToCollect)

                applesCollected += 1
                print ("Apples collected: " + str(applesCollected))

        for obstacle in obstacleList:

            # Player taking damage.
            if obstacle.rect.colliderect(player) and player.damageAnimation == False:
                player.hitpoints -= 1
                player.damageAnimation = True
            if player.hitpoints == 0:
                sys.exit()

            # Shooting down a pumpkin.
            for shotFireball in fireballList:
                if shotFireball.rect.colliderect(obstacle):

                    fireballList.remove(shotFireball)
                    objectList.remove(shotFireball)
                    obstacleList.remove(obstacle)
                    objectList.remove(obstacle)

                    obstaclesDestroyed += 1
                    print("Obstacles destroyed: " + str(obstaclesDestroyed))

    # Erase last frame.
    screen.fill(background)

    # Draw images on the screen.
    for object in objectList:
        object.update()

    # Make everything drawn to the screen visible.
    pygame.display.flip()
