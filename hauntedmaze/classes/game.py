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
    screen = pygame.display.set_mode((Settings.gameHeight, Settings.gameWidth))
    clock = pygame.time.Clock()
    points = 1
    start = 0
    font = None
    level = 1

    def init(self):
        pygame.init()
        pygame.display.set_caption(Settings.gameTitle)
        self.start = time.time()
        self.font = pygame.font.Font(Settings.font_type, Settings.font_size)
        self.load()

    def load(self):
        x = 0
        y = 0
        # for row in game.level:
        for row in Levels.get_level():
            for col in row:
                if col == "W":
                    Wall(x, y)
                if col == "G":
                    Ghost(x, y, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                if col == "P":
                    game.player.start(x, y)
                x += Settings.blockSize
            y += Settings.blockSize
            x = 0

    def restart(self):
        Settings.pause = False
        self.points = 1
        self.start = time.time()
        self.walls = []
        self.player = Player()
        self.ghosts = []
        self.level = Settings.level
        self.load()

    def pause(self):
        Settings.pause = True

    def text(self, text):
        text_width, text_height = self.font.size(str(text))
        text = self.font.render(str(text), True, Settings.font_color)
        x = (Settings.gameWidth / 2) - (text_width / 2)
        y = (Settings.gameHeight / 2) - (text_height / 2)
        self.screen.blit(text, (x, y))

    def draw_rect(self, obj, color):
        pygame.draw.rect(self.screen, color, obj)

    def draw_points(self):
        text = round(self.points)
        text = self.font.render(str(text), True, Settings.font_color)
        x = Settings.blockSize
        y = Settings.blockSize
        self.screen.blit(text, (x, y))

    def counter_points(self):
        if Settings.pause is not True:
            self.points = time.time() - self.start
        self.draw_points()