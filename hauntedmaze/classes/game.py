import pygame
import random
from .settings import Settings
from .player import Player
from .walls import Wall
from .ghosts import Ghost

class Game(object):

    walls = []
    player = Player()
    ghosts = []
    level = Settings.level
    screen = pygame.display.set_mode((Settings.gameSize, Settings.gameSize))
    clock = pygame.time.Clock()

    def init(self):
        pygame.init()
        pygame.display.set_caption(Settings.gameTitle)

    def load(self):
        x = y = 0
        for row in self.level:
            for col in row:
                if col == "W":
                    Wall(x, y)
                if col == "G":
                    Ghost(x, y, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                if col == "P":
                    self.player.start(x, y)
                x += Settings.blockSize
            y += Settings.blockSize
            x = 0

    def restart(self):
        Settings.pause = False
        self.walls = []
        self.player = Player()
        self.ghosts = []
        self.level = Settings.level
        self.load()

    def pause(self):
        Settings.pause = True

    def text(self, text):
        color = (255, 255, 255)
        size = 50
        font_type = 'roboto.ttf'
        font = pygame.font.Font(font_type, size)
        text_width, text_height = font.size(str(text))
        text = font.render(str(text), True, color)
        x = (Settings.gameSize / 2) - (text_width / 2)
        y = (Settings.gameSize / 2) - (text_height / 2)
        self.screen.blit(text, (x, y))

    def draw_rect(self, obj, color):
        pygame.draw.rect(self.screen, color, obj)
