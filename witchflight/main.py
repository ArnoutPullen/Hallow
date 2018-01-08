# Standard initialisation stuff.
import sys, pygame
import random
from pygame.locals import *
pygame.init()

# Set game window.
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Witchflight')
background = 40, 40, 80  # Background RGB color.

# Initialise static images.
moon            = pygame.image.load('images/moon.png')
gameover        = pygame.image.load('images/gameover.png')
retrybutton     = pygame.image.load('images/retrybutton.png')
moonRect        = moon.get_rect()
gameoverRect    = gameover.get_rect()
retrybuttonRect = retrybutton.get_rect()
moonRect        = moonRect.move(540, 70)
gameoverRect    = gameoverRect.move(162, 60)
retrybuttonRect = retrybuttonRect.move(345, 380)

# Initialise audio files.
sAppleCollect   = pygame.mixer.Sound('audio/apple_collect.wav')
sPotionCollect  = pygame.mixer.Sound('audio/potion_collect.wav')
sShootFireball  = pygame.mixer.Sound('audio/shoot_fireball.wav')
sTakeDamage     = pygame.mixer.Sound('audio/take_damage.wav')
sBossDamage     = pygame.mixer.Sound('audio/boss_damage.wav')
sBossDeath      = pygame.mixer.Sound('audio/boss_death.wav')
sBossFireball   = pygame.mixer.Sound('audio/boss_fireball.wav')
sGameOver       = pygame.mixer.Sound('audio/gameover.wav')
sBgm            = pygame.mixer.Sound('audio/bgm.wav')
sAppleCollect   .set_volume(0.2)
sPotionCollect  .set_volume(0.2)
sShootFireball  .set_volume(0.2)
sTakeDamage     .set_volume(0.1)
sBossDamage     .set_volume(0.5)
sBossDeath      .set_volume(0.5)
sBossFireball   .set_volume(0.1)
sGameOver       .set_volume(1.0)
sBgm            .set_volume(1.0)

sBgm.play() # Start the background music.

'''
Classes.
Game objects created from these classes will be added to their respective list.
All game objects will also be added to generic object list.

Each class has an update() method that contains the class' movement logic.
We call the update function for each game object in the object list.
This allows us to cleanly update all game objects each frame.
'''
class UpgradeImage:
    def __init__(self):
        self.image = pygame.image.load('images/fireball_up.png')
        self.rect = self.image.get_rect()
        self.frameCounter = 0

    def Update(self):
        if self.frameCounter != 20:
            self.rect.x = witch.rect.x
            self.rect.y = witch.rect.y - 22
            screen.blit(self.image, self.rect)
            self.frameCounter += 1
        else:
            objectList.remove(self)

class Fireball:
    def __init__(self):
        self.image1 = pygame.image.load('images/fireball1.png')
        self.image2 = pygame.image.load('images/fireball2.png')
        self.rect = self.image1.get_rect()
        self.speed = [10, 0]
        self.frameCounter = 0

    def Update(self):

        # Move the object.
        self.rect = self.rect.move(self.speed)

        # Show image1 for three frames.
        if self.frameCounter <= 2:
            screen.blit(self.image1, self.rect)
            self.frameCounter += 1

        # Show image2 for three frames and reset the animation.
        elif self.frameCounter <= 4:
            screen.blit(self.image2, self.rect)
            self.frameCounter += 1
        elif self.frameCounter > 4:
            screen.blit(self.image2, self.rect)
            self.frameCounter = 0

        # If the object is off the screen, remove it.
        if self.rect.x > 800:
            fireballList.remove(self)
            objectList.remove(self)

class BossFireball:
    def __init__(self):
        self.image1 = pygame.image.load('images/boss_fireball1.png')
        self.image2 = pygame.image.load('images/boss_fireball2.png')
        self.rect = self.image1.get_rect()
        self.speed = [-10, 0]
        self.frameCounter = 0

    def Update(self):

            # Move the object.
            self.rect = self.rect.move(self.speed)

            # Show image1 for three frames.
            if self.frameCounter <= 2:
                screen.blit(self.image1, self.rect)
                self.frameCounter += 1

            # Show image2 for three frames and reset the animation.
            elif self.frameCounter <= 4:
                screen.blit(self.image2, self.rect)
                self.frameCounter += 1
            elif self.frameCounter > 4:
                screen.blit(self.image2, self.rect)
                self.frameCounter = 0

            # If the object is off the screen, remove it.
            if self.rect.x < -100:
                bossAttackList.remove(self)
                objectList.remove(self)

class Apple:
    def __init__(self):
        self.image = pygame.image.load('images/apple.png')
        self.rect = self.image.get_rect()
        self.speed = [-8, 0]
        self.locationSpawned = 0

    def Update(self):

        # Move and show the object.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the object is off the screen, remove it.
        if self.rect.x < -100:
            appleList.remove(self)
            objectList.remove(self)

class Potion:
    def __init__(self):
        self.image = pygame.image.load('images/potion.png')
        self.rect = self.image.get_rect()
        self.speed = [-8, 0]
        self.locationSpawned = 0

    def Update(self):

        # Move and show the object.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the object is off the screen, remove it.
        if self.rect.x < -100:
            potionList.remove(self)
            objectList.remove(self)

class Pumpkin():
    def __init__(self):
        self.image = pygame.image.load('images/pumpkin.png')
        self.rect = self.image.get_rect()
        self.speed = [-13, 0]
        self.locationSpawned = 0

    def Update(self):

        # Move and show the object.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the object is off the screen, remove it.
        if self.rect.x < -100:
            pumpkinList.remove(self)
            objectList.remove(self)

class Cloud:
    def __init__(self):
        self.image = pygame.image.load('images/cloud.png')
        self.rect = self.image.get_rect()
        self.speed = [-6, 0]
        self.locationSpawned = 0

    def Update(self):

        # Move and show the object.
        self.rect = self.rect.move(self.speed)
        screen.blit(self.image, self.rect)

        # If the object is off the screen, remove it.
        if self.rect.x < -150:
            cloudList.remove(self)
            objectList.remove(self)

class EyePumpkin:  # Boss
    def __init__(self):

        # Image variables.
        self.image1 = pygame.image.load('images/eye_pumpkin.png')
        self.image2 = pygame.image.load('images/closed_eye_pumpkin.png')
        self.rect = self.image1.get_rect()

        # Movement variables.
        self.upSpeed = [0, -6]
        self.downSpeed = [0, 6]
        self.goingUp = True
        self.goingDown = False
        # -----
        self.spawned = False
        self.spawnSpeed = [-2, 0]

        # Damage handling variables.
        self.hitpoints = 10
        self.damageAnimation = False
        self.loopedAnimation = 0
        self.frameCounter = 0

        # Attack handling variables.
        self.eyeClosed = False
        self.eyeFrameCounter = 0

    def Update(self):

        if self.eyeClosed and self.eyeFrameCounter <= 11:
            self.eyeFrameCounter += 1
        elif self.eyeClosed and self.eyeFrameCounter > 11:
            self.eyeClosed = False
            self.eyeFrameCounter = 0

        if self.spawned == False:
            self.rect = self.rect.move(self.spawnSpeed)
            if self.rect.x == 500:
                self.spawned = True

        elif self.goingUp:
            if self.rect.top > -25:
                self.rect = self.rect.move(self.upSpeed)
            else:
                self.goingUp = False
                self.goingDown = True

        elif self.goingDown:
            if self.rect.bottom < (height + 105):
                self.rect = self.rect.move(self.downSpeed)
            else:
                self.goingDown = False
                self.goingUp = True

class Witch:
    def __init__(self):

        # Image variables.
        self.image = pygame.image.load('images/witch.png')
        self.rect = self.image.get_rect()

        # Control variables.
        self.flyingUp = False
        self.flyingDown = False
        self.fireballReady = False
        self.upSpeed = -6
        self.downSpeed = 6

        # Damage handling variables.
        self.damageAnimation = False
        self.hitpoints = 4
        self.loopedAnimation = 0
        self.frameCounter = 0

    def Update(self):

        # Move the object.
        if self.rect.top > 20 and self.flyingUp == True:
            self.rect = self.rect.move([0, self.upSpeed])
        if self.rect.bottom < (height - 30) and self.flyingDown == True:
            self.rect = self.rect.move([0, self.downSpeed])

        # Showing the object.
        if self.damageAnimation == True:

            # The first 5 frames after taking damage, do not show the object.
            if self.frameCounter <= 5:
                self.frameCounter += 1

            # The next 5 frames, show the object.
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

'''
Game object lists.
These lists will keep track of all of our game objects.
Segregating them per class allows us to easily use their contents to create effective game logic.
'''
objectList      = list()
fireballList    = list()
bossAttackList  = list()
cloudList       = list()
pumpkinList     = list()
potionList      = list()
appleList       = list()

'''
Custom events.
We use custom events to create timed intervals for certain pieces of game logic to execute.
The timed intervals execute based on the given milliseconds.
'''
SPAWNAPPLE          = USEREVENT + 1
SPAWNPOTION         = USEREVENT + 2
SPAWNCLOUD1         = USEREVENT + 3
SPAWNCLOUD2         = USEREVENT + 4
SPAWNPUMPKIN        = USEREVENT + 5
BOSSATTACK          = USEREVENT + 6
pygame.time.set_timer(SPAWNAPPLE,   2850)
pygame.time.set_timer(SPAWNPOTION,  4400)
pygame.time.set_timer(SPAWNCLOUD1,  2372)
pygame.time.set_timer(SPAWNCLOUD2,  6000)
pygame.time.set_timer(SPAWNPUMPKIN, 2750)
pygame.time.set_timer(BOSSATTACK,   1327)

# Game state variables.
isGameOver = False

witch = Witch()                         # Instantiate player game object.
witch.rect = witch.rect.move(15, 240)   # Move player to their starting position.
objectList.insert(True, witch)          # Add the created player to the list of game objects.

# Make the player hitbox more forgiving.
witch.rect.width -= 10
witch.rect.height -= 10

# Boss spawning.
boss = EyePumpkin()
boss.rect = boss.rect.move(9000, 240)  # 9000 for midway-spawn, 800 for immediate spawn.
objectList.insert(True, boss)
boss.rect.width -= 40
boss.rect.height -= 15

# ------------------------------------------------------------------------------------------------

while True: # Main game loop.

    # Run the game at 30 frames per second.
    pygame.time.Clock().tick(60)

    '''
    Event catcher.
    We can execute game logic per event and per frame inside this for statement.
    Most events are player input, however we also created several custom events.
    These custom events are handled inside this for loop as well.
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        # ------------- EVENT LOGIC --------------

        # We do not want to handle the usual events if the player has 0 hitpoints.
        if witch.hitpoints <= 0:

            # Check mouse position to determine whether the retry button is being clicked on.
            mousePos = pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] == True and retrybuttonRect.collidepoint(mousePos)\
            or event.type == KEYDOWN and event.key == K_r:

                # Empty all lists.
                objectList      = list()
                fireballList    = list()
                bossAttackList  = list()
                cloudList       = list()
                pumpkinList     = list()
                potionList      = list()
                appleList       = list()

                # Recreate the witch.
                witch = Witch()
                witch.rect = witch.rect.move(15, 240)
                objectList.insert(True, witch)

                # Make the player hitbox more forgiving.
                witch.rect.width -= 10
                witch.rect.height -= 10

                isGameOver = False
                sBgm.play()

                # Boss spawning.
                boss = EyePumpkin()
                boss.rect = boss.rect.move(9000, 240)
                objectList.insert(True, boss)
                boss.rect.width -= 20
                boss.rect.height -= 15

        else: # Usual event handling.

            if event.type == KEYDOWN:  # Player controls

                # Moving up and down.
                if event.key == K_UP:
                    witch.flyingUp = True
                elif event.key == K_DOWN:
                    witch.flyingDown = True

                # Shooting a fireball.
                elif event.key == K_SPACE and witch.fireballReady == True:

                    # Create and position an object.
                    fireball = Fireball()
                    fireball.rect.x = witch.rect.x + 65
                    fireball.rect.y = witch.rect.y + 15

                    # Add the created object to relevant lists.
                    objectList.insert(True, fireball)
                    fireballList.insert(True, fireball)

                    witch.fireballReady = False
                    sShootFireball.play()

            elif event.type == KEYUP:  # Player controls.

                if event.key == K_UP:
                    witch.flyingUp = False
                if event.key == K_DOWN:
                    witch.flyingDown = False

            # ----------- Object spawning logic. -----------

            elif event.type == SPAWNAPPLE:

                # Create and position an object.
                apple = Apple()
                randomInt = random.randint(25, 495)

                # Keep resetting the spawn location until it is far enough away from already-existing clouds.
                for existentCloud in cloudList:
                    while (existentCloud.locationSpawned > (randomInt - 25) and existentCloud.locationSpawned < (randomInt + 25)):
                        randomInt = random.randint(25, 495)

                apple.rect.x += 800
                apple.rect.y += randomInt
                apple.locationSpawned = randomInt

                # add the created object to relevant lists.
                appleList.insert(True, apple)
                objectList.insert(True, apple)

            elif event.type == SPAWNPOTION:

                # Create and position an object.
                potion = Potion()
                randomInt = random.randint(25, 495)
                potion.rect.x += 800
                potion.rect.y += randomInt
                potion.locationSpawned = randomInt

                # Keep resetting the spawn location until it is far enough away from already-existing apples.
                for existentApple in appleList:
                    while (existentApple.locationSpawned > (randomInt - 25) and existentApple.locationSpawned < (randomInt + 25)):
                        randomInt = random.randint(25, 495)

                # add the created object to relevant lists.
                potionList.insert(True, potion)
                objectList.insert(True, potion)

            elif event.type == SPAWNCLOUD1:

                # Create and position an object.
                cloud = Cloud()
                randomInt = random.randint(25, 495)
                cloud.rect.x += 800
                cloud.rect.y += randomInt
                cloud.locationSpawned = randomInt

                # Make the object hitbox more forgiving.
                cloud.rect.width -= 10
                cloud.rect.height -= 10

                # add the created object to relevant lists.
                cloudList.insert(True, cloud)
                objectList.insert(True, cloud)

            elif event.type == SPAWNCLOUD2:

                # Create and position an object.
                cloud = Cloud()
                randomInt = random.randint(25, 495)

                # Keep resetting the spawn location until it is far enough away from already-existing clouds.
                for existentCloud in cloudList:
                    while existentCloud.locationSpawned > (randomInt - 75) and existentCloud.locationSpawned < (randomInt + 75):
                        randomInt = random.randint(25, 495)

                cloud.rect.x += 800
                cloud.rect.y += randomInt
                cloud.locationSpawned = randomInt

                # Make the object hitbox more forgiving.
                cloud.rect.width -= 10
                cloud.rect.height -= 10

                # add the created object to relevant lists.
                cloudList.insert(True, cloud)
                objectList.insert(True, cloud)

            elif event.type == SPAWNPUMPKIN:

                # Create and position an object.
                pumpkin = Pumpkin()
                randomInt = random.randint(25, 495)
                pumpkin.rect.x += 800
                pumpkin.rect.y += randomInt
                pumpkin.locationSpawned = randomInt

                # Make the object hitbox more forgiving.
                pumpkin.rect.width -= 5
                pumpkin.rect.height -= 5

                # add the created object to relevant lists.
                pumpkinList.insert(True, pumpkin)
                objectList.insert(True, pumpkin)

            elif event.type == BOSSATTACK and boss.spawned:

                # Create and position an object.
                bossFireball = BossFireball()
                bossFireball.rect.x = boss.rect.x + 75
                bossFireball.rect.y = boss.rect.y + 10

                # Make the object hitbox more forgiving.
                pumpkin.rect.width -= 5
                pumpkin.rect.height -= 5

                bossAttackList.insert(True, bossFireball)
                objectList.insert(True, bossFireball)
                boss.eyeClosed = True
                sBossFireball.play()

        # -------------- LOOP END ----------------

    # Collision handling.

    for apple in appleList:

        if apple.rect.colliderect(witch):
            appleList.remove(apple)
            objectList.remove(apple)
            sAppleCollect.play()

    for potion in potionList:

        if potion.rect.colliderect(witch):
            potionList.remove(potion)
            objectList.remove(potion)

            if witch.fireballReady == False:
                witch.fireballReady = True

                # Show upgrade image.
                upgradeImage = UpgradeImage()
                upgradeImage.image = pygame.image.load('images/fireball_up.png')
                upgradeImage.rect = upgradeImage.image.get_rect()
                objectList.insert(True, upgradeImage)

            elif witch.hitpoints != 4:
                witch.hitpoints += 1

                # Show upgrade image.
                upgradeImage = UpgradeImage()
                upgradeImage.image = pygame.image.load('images/hp_up.png')
                upgradeImage.rect = upgradeImage.image.get_rect()
                objectList.insert(True, upgradeImage)

            elif witch.upSpeed != -9:
                witch.upSpeed -= 1
                witch.downSpeed += 1

                # Show upgrade image.
                upgradeImage = UpgradeImage()
                upgradeImage.image = pygame.image.load('images/speed_up.png')
                upgradeImage.rect = upgradeImage.image.get_rect()
                objectList.insert(True, upgradeImage)

            else:
                # TODO: Score increase.
                pass

            sPotionCollect.play()

    for pumpkin in pumpkinList:

        # Witch colliding with a pumpkin.
        if pumpkin.rect.colliderect(witch) and witch.damageAnimation == False:
            witch.hitpoints -= 1
            witch.damageAnimation = True
            sTakeDamage.play()

        # Fireball colliding with pumpkin.
        for fireball in fireballList:
            if fireball.rect.colliderect(pumpkin):

                fireballList.remove(fireball)
                objectList.remove(fireball)
                pumpkinList.remove(pumpkin)
                objectList.remove(pumpkin)

    for cloud in cloudList:

        # Witch colliding with a cloud.
        if cloud.rect.colliderect(witch) and witch.damageAnimation == False:
            witch.hitpoints -= 1
            witch.damageAnimation = True
            sTakeDamage.play()

        # Fireball colliding with a cloud.
        for fireball in fireballList:
            if fireball.rect.colliderect(cloud):

                fireballList.remove(fireball)
                objectList.remove(fireball)
                cloudList.remove(cloud)
                objectList.remove(cloud)

    # Fireball colliding with the boss.
    for fireball in fireballList:
        if fireball.rect.colliderect(boss) and boss.damageAnimation == False and boss.spawned == True:
            fireballList.remove(fireball)
            objectList.remove(fireball)
            boss.hitpoints -= 1
            boss.damageAnimation = True
            sBossDamage.play()
            if boss.hitpoints == 0:
                boss.spawned = False
                sBossDeath.play()

    for bossFireball in bossAttackList:
        if bossFireball.rect.colliderect(witch) and witch.damageAnimation == False:
            witch.hitpoints -= 1
            witch.damageAnimation = True
            sTakeDamage.play()

        for fireball in fireballList:
            if fireball.rect.colliderect(bossFireball):
                fireballList.remove(fireball)
                objectList.remove(fireball)

    # If the game is over, show the 'game over' screen.
    if witch.hitpoints <= 0:

        # Upon first getting to this screen, handle the audio sequence.
        if isGameOver == False:
            sBgm.stop()
            sGameOver.play()

        screen.fill(background)
        screen.blit(gameover, gameoverRect)
        screen.blit(retrybutton, retrybuttonRect)
        pygame.display.flip()
        isGameOver = True

    else:

        '''
        Drawing a frame.
        After handling all event logic, we erase the last frame.
        Next, we update all game objects.
        Finally, we make the new frame visible.
        '''
        screen.fill(background)
        screen.blit(moon, moonRect)

        # Showing the boss.
        if boss.damageAnimation == True and boss.hitpoints != 0:

            # The first 5 frames after taking damage, do not show the object.
            if boss.frameCounter <= 5:
                boss.frameCounter += 1

            # The next 5 frames, show the object.
            elif boss.frameCounter <= 10:
                if boss.eyeClosed:
                    screen.blit(boss.image2, boss.rect)
                else:
                    screen.blit(boss.image1, boss.rect)
                boss.frameCounter += 1

            # The animation is done, which we add to the loopedAnimation.
            elif boss.frameCounter > 10:
                boss.frameCounter = 0
                boss.loopedAnimation += 1

            # If the animation has looped a number of times, stop it.
            if boss.loopedAnimation == 5:
                boss.damageAnimation = False
                boss.loopedAnimation = 0
        elif boss.hitpoints == 0:
            pass
        else:
            if boss.eyeClosed:
                screen.blit(boss.image2, boss.rect)
            else:
                screen.blit(boss.image1, boss.rect)

        for object in objectList:
            object.Update()

        pygame.display.flip()
