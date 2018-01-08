import pygame
from .settings import Settings

class Ghost(object):

    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, Settings.blockSize, Settings.blockSize)
        self.color = color
        game.ghosts.append(self)

    def move(self, x, y):

        if self.rect.colliderect(game.player.rect):
            game.pause()

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
