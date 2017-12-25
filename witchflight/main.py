# Standard initialisation stuff.
import sys, pygame
from pygame.locals import *
pygame.init()

# Set game window.
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Witchflight')

# Set variables.
speed = [10, 10]            # Pumpkin movement speed.
background = 25, 25, 40     # Background RGB color.
up = [0, -10]               # Move witch up.
down = [0, 10]              # Move witch down.
frameCounter = 0            # Witch frame counter.

# This variable represents the player's lives.
global hitpoints            # Declare global int: hitpoints.
hitpoints = 4               # Set hitpoint amount.

# This variable is used to check whether the player has recently taken damage.
global damageAnimation      # Declare global bool: damageAnimation.
damageAnimation = False     # Set damageAnimation state.

# This variable is used to execute spacebar-activated code only once per press.
global spacebarPressed      # Declare global bool: damageTaken.
spacebarPressed = False     # Set spacebarPressed state.

# This variable is used to loop the 'Taking damage' animation.
global looped               # Declare global int: looped.
looped = 0                  # Set looped value.

# Load image into a variable.
moon = pygame.image.load('images/moon.png')
pumpkin = pygame.image.load('images/pumpkin.png')
witch = pygame.image.load('images/witch.png')
retrybutton = pygame.image.load('images/retrybutton.png')
gameover = pygame.image.load('images/gameover.png')

# Load SFX.
appleCollectSound = pygame.mixer.Sound('audio/apple_collect.wav')
potionCollectSound = pygame.mixer.Sound('audio/potion_collect.wav')
takeDamageSound = pygame.mixer.Sound('audio/take_damage.wav')
lethalDamageSound = pygame.mixer.Sound('audio/lethal_damage.wav')
gameoverSound = pygame.mixer.Sound('audio/gameover.wav')

# Set a rectangle version of the image variable.
moonRect = moon.get_rect()
pumpkinRect = pumpkin.get_rect()
witchRect = witch.get_rect()
retrybuttonRect = retrybutton.get_rect()
gameoverRect = gameover.get_rect()

# Make the player hitbox more forgiving.
witchRect.width -= 15
witchRect.height -= 15

# Set up image original position.
witchRect = witchRect.move(15, 240)
moonRect = moonRect.move(540, 70)
pumpkinRect = pumpkinRect.move(140, 140)
retrybuttonRect = retrybuttonRect.move(345, 380)
gameoverRect = gameoverRect.move(162, 60)

# Defining a fireball.
class fireball:
    def __init__(self):
        self.image1 = pygame.image.load('images/fireball1.png')
        self.image2 = pygame.image.load('images/fireball2.png')
        self.rect = self.image1.get_rect()
        self.flippedImage = False

# Set up a list that will be filled with all fireball objects.
fireballList = list()

while True: # Main game loop.

    # Run the game at 60 frames per second.
    pygame.time.Clock().tick(60)

    # Event catcher. If statements allow us to decide what happens per event within this for loop.
    # ( Events such as quitting the game, pressing a key, moving the mouse, etc. )
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # If at any point in our game loop the player has 0 hitpoints, we do not want to handle the usual events.
    if hitpoints == 0:

        mousePos = pos = pygame.mouse.get_pos()

        # If the player clicks the retry button or presses spacebar, we reset the image positions and hitpoints.
        if pygame.mouse.get_pressed()[0] == True and retrybuttonRect.collidepoint(mousePos)\
        or event.type == KEYDOWN and event.key == K_SPACE:

            # Empty our list of fireballs.
            fireballList = list()

            # Reset rectangles.
            moonRect = moon.get_rect()
            pumpkinRect = pumpkin.get_rect()
            witchRect = witch.get_rect()
            retrybuttonRect = retrybutton.get_rect()
            gameoverRect = gameover.get_rect()

            # Reset rectangle positions.
            witchRect = witchRect.move(15, 240)
            moonRect = moonRect.move(540, 70)
            pumpkinRect = pumpkinRect.move(140, 140)
            retrybuttonRect = retrybuttonRect.move(345, 380)
            gameoverRect = gameoverRect.move(162, 60)

            # Reset pumpkin movement trajectory.
            speed = [10, 10]

            hitpoints = 3

            damageAnimation = False

    else:

        # Instantiate a fireball and add it to the list of fireballs.
        # ( We check the state of spacebarPressed to make sure we don't get a line of fireballs )
        if event.type == KEYDOWN:
            if event.key == K_SPACE and spacebarPressed == False:

                potionCollectSound.play()
                fireballObject = fireball()
                fireballObject.rect.x = witchRect.x + 65
                fireballObject.rect.y = witchRect.y + 15
                fireballList.insert(True, fireballObject)
                spacebarPressed = True

        # Make sure we catch the player no longer holding down the spacebar.
        if event.type == KEYUP:
            if event.key == K_SPACE and spacebarPressed == True:
                spacebarPressed = False

        # Update pumpkin position.
        # ( If the image has moved outside the screen, we reverse the speed. )
        pumpkinRect = pumpkinRect.move(speed)
        if pumpkinRect.left < 0 or pumpkinRect.right > width:
            speed[0] = -speed[0]
        if pumpkinRect.top < 0 or pumpkinRect.bottom > height:
            speed[1] = -speed[1]

        # Taking damage logic.
        if pumpkinRect.colliderect(witchRect) and damageAnimation == False:
            lethalDamageSound.play()
            hitpoints -= 1
            damageAnimation = True

        # Play SFX.
        if pumpkinRect.left < 2 or pumpkinRect.right > (width - 2):
            takeDamageSound.play()
        if pumpkinRect.top < 2 or pumpkinRect.bottom > (height - 2):
            takeDamageSound.play()

        # Move witch.
        if event.type == KEYDOWN:
            if event.key == K_UP and witchRect.top > 18:
                witchRect = witchRect.move(up)
            if event.key == K_DOWN and witchRect.bottom < (height - 18):
                witchRect = witchRect.move(down)

        # Erase last frame.
        screen.fill(background)

        # If the player has 0 hitpoints in this iteration, show the game over screen. otherwise load the next frame.
        if hitpoints == 0:
            screen.blit(gameover, gameoverRect)
            screen.blit(retrybutton, retrybuttonRect)
            gameoverSound.play()
        else:

            # Draw images on the screen.
            screen.blit(moon, moonRect)
            screen.blit(pumpkin, pumpkinRect)

            # If a damage animation is queued, execute it.
            if damageAnimation == True:

                # The first 5 frames after damage, do not show the witch.
                if (frameCounter <= 5):

                    frameCounter += 1

                # The next 5 frames, show the witch.
                elif (frameCounter <= 10):
                    screen.blit(witch, witchRect)
                    frameCounter += 1

                # After those frame sets, update variables.
                elif (frameCounter > 10):
                    frameCounter = 0
                    looped += 1

                # If the damage animation has looped enough times, stop the animation.
                if (looped == 5):
                    damageAnimation = False
                    looped = 0
            else:
                screen.blit(witch, witchRect)

            # Each fireball moves to the right.
            for fireballObject in fireballList:
                fireballObject.rect = fireballObject.rect.move(14, 0)

                # Constantly switch between image1 and image2.
                if (fireballObject.flippedImage == True):
                    screen.blit(fireballObject.image1, fireballObject.rect)
                    fireballObject.flippedImage = False
                else:
                    screen.blit(fireballObject.image2, fireballObject.rect)
                    fireballObject.flippedImage = True

        # Make everything drawn to the screen visible.
        pygame.display.flip()
