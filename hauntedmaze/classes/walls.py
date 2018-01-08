import pygame
from .game import Game
from .settings import Settings

class Wall(object):

    game = Game()

    def __init__(self, x, y):
        game.walls.append(self)
        self.rect = pygame.Rect(x, y, Settings.blockSize, Settings.blockSize)
