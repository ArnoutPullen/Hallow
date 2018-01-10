import pygame
# from .classes import *
from classes.game import Game
from classes.settings import Settings

# Init game
game = Game()
game.init()

running = True
while running:

    # Init
    game.clock.tick(10)
    game.screen.fill(Settings.backgroundColor)

    # Movement while game is not paused
    if Settings.pause is not True:
        # Player movement
        key = pygame.key.get_pressed()
        # Left
        if key[pygame.K_LEFT]:
            game.player.move(-Settings.blockSize, 0)
        # Right
        if key[pygame.K_RIGHT]:
            game.player.move(Settings.blockSize, 0)
        # Up
        if key[pygame.K_UP]:
            game.player.move(0, -Settings.blockSize)
        # Down
        if key[pygame.K_DOWN]:
            game.player.move(0, Settings.blockSize)

        # Ghost movement
        for ghost in game.ghosts:
            x = Settings.blockSize * random.randint(-1, 1)
            y = Settings.blockSize * random.randint(-1, 1)
            ghost.move(x, y)

    # Pause
    if Settings.pause is True:
        game.text('Game Paused')

    # Render objects
    for wall in game.walls:
        game.draw_rect(wall.rect, Settings.wallColor)
    for ghost in game.ghosts:
        game.draw_rect(ghost.rect, ghost.color)
    game.draw_rect(game.player.rect, Settings.playerColor)
    game.counter_points()
    pygame.display.flip()

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and Settings.pause is True:
            game.restart()
