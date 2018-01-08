import pygame
from .settings import Settings

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(Settings.blockSize, Settings.blockSize, Settings.blockSize, Settings.blockSize)

    def move(self, x, y):
        if x != 0:
            self.move_single_axis(x, 0)
        if y != 0:
            self.move_single_axis(0, y)

    def move_single_axis(self, x, y):

        # moving
        self.rect.x += x
        self.rect.y += y

        # collision
        for wall in game.walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                if x < 0:
                    self.rect.left = wall.rect.right
                if y > 0:
                    self.rect.bottom = wall.rect.top
                if y < 0:
                    self.rect.top = wall.rect.bottom

    def start(self, x, y):
        self.rect.x = x
        self.rect.y = y
