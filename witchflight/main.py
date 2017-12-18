import sys, pygame
from pygame.locals import *
pygame.init()

# Set game window.
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Witchflight')

# Set variables.
speed = [10, 10]
background = 25, 25, 40
up = [0, -10]
down = [0, 10]

# Load image into a variable.
moon = pygame.image.load('images/moon.png')
pumpkin = pygame.image.load('images/pumpkin.png')
witch = pygame.image.load('images/witch.png')

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

# Set up image original position.
witchRect = witchRect.move(15, 20)
moonRect = moonRect.move(540, 70)
pumpkinRect = pumpkinRect.move(70, 340)

while True: # Main game loop.

    pygame.time.Clock().tick(60)

    # Event catcher. If statements allow us to decide what happens per event within this for loop.
    # ( Events such as quitting the game, pressing a key, moving the mouse, etc. )
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Update image position.
    # ( If the image has moved outside the screen, we reverse the speed. )
    pumpkinRect = pumpkinRect.move(speed)
    if pumpkinRect.left < 0 or pumpkinRect.right > width:
        speed[0] = -speed[0]
    if pumpkinRect.top < 0 or pumpkinRect.bottom > height:
        speed[1] = -speed[1]
    if pumpkinRect.colliderect(witchRect):
        lethalDamageSound.play()

    # Play SFX.
    if pumpkinRect.left < 2 or pumpkinRect.right > (width - 2):
        takeDamageSound.play()
    if pumpkinRect.top < 2 or pumpkinRect.bottom > (height - 2):
        takeDamageSound.play()

    # Move witch.
    if event.type == KEYDOWN:
        if event.key == K_UP and witchRect.top > 6:
            witchRect = witchRect.move(up)
        if event.key == K_DOWN and witchRect.bottom < (height - 6):
            witchRect = witchRect.move(down)

    # Erase last frame.
    screen.fill(background)

    # Draw image on the screen.
    screen.blit(moon, moonRect)
    screen.blit(pumpkin, pumpkinRect)
    screen.blit(witch, witchRect)

    # Make everything drawn to the screen visible.
    pygame.display.flip()
