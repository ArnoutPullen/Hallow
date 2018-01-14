import random
import time
import pygame


class Levels:
    level = [
        "WWWWWWWWWWWWWWWWWWWWWWW",
        "W          W          W",
        "W WWW WWWW W WWWW WWW W",
        "W WWW WWWW W WWWW WWW W",
        "W                     W",
        "W WWW W WWWWWWW W WWW W",
        "W     W WWWWWWW W     W",
        "WWWWW W    W    W WWWWW",
        "WWWWW WWWW W WWWW WWWWW",
        "WWWWW W         W WWWWW",
        "WWWWW W WWW WWW W WWWWW",
        "        WGG GGW        ",
        "WWWWW W WWWWWWW W WWWWW",
        "WWWWW W         W WWWWW",
        "WWWWW W WWWWWWW W WWWWW",
        "WWWWW W WWWWWWW W WWWWW",
        "W          W          W",
        "W WWW WWWW W WWWW WWW W",
        "W   W      P      W   W",
        "WWW W WWWWWWWWWWW W WWW",
        "W          W          W",
        "W  WWWWWWW W WWWWWWWW W",
        "W  WWWWWWW W WWWWWWWW W",
        "W                     W",
        "WWWWWWWWWWWWWWWWWWWWWWW",
    ]

    def get_level(level):
        print(level)
        return self.level


class Settings:
    gameTitle = "Haunted Maze"
    font_type = 'roboto.ttf'
    font_size = 30
    font_color = (255, 255, 255)
    backgroundColor = (0, 0, 0)
    playerColor = (255, 255, 255)
    wallColor = (0, 100, 0)
    blockSize = 32
    gameHeight = 23 * blockSize
    gameWidth = 25 * blockSize
    pause = False
    level = [
        "WWWWWWWWWWWWWWWWWWWWWWW",
        "W          W          W",
        "W WWW WWWW W WWWW WWW W",
        "W WWW WWWW W WWWW WWW W",
        "W                     W",
        "W WWW W WWWWWWW W WWW W",
        "W     W WWWWWWW W     W",
        "WWWWW W    W    W WWWWW",
        "WWWWW WWWW W WWWW WWWWW",
        "WWWWW W         W WWWWW",
        "WWWWW W WWW WWW W WWWWW",
        "        WGG GGW        ",
        "WWWWW W WWWWWWW W WWWWW",
        "WWWWW W         W WWWWW",
        "WWWWW W WWWWWWW W WWWWW",
        "WWWWW W WWWWWWW W WWWWW",
        "W          W          W",
        "W WWW WWWW W WWWW WWW W",
        "W   W      P      W   W",
        "WWW W WWWWWWWWWWW W WWW",
        "W          W          W",
        "W  WWWWWWW W WWWWWWWW W",
        "W  WWWWWWW W WWWWWWWW W",
        "W                     W",
        "WWWWWWWWWWWWWWWWWWWWWWW",
    ]


class Images:
    background = pygame.image.load('background.jpg')


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


class Ghost(object):

    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, Settings.blockSize, Settings.blockSize)
        self.color = color
        self.x = round(x / Settings.blockSize)
        self.y = round(y / Settings.blockSize)
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


class Wall(object):

    def __init__(self, x, y):
        game.walls.append(self)
        self.x = round(x / Settings.blockSize)
        self.y = round(y / Settings.blockSize)
        self.rect = pygame.Rect(x, y, Settings.blockSize, Settings.blockSize)


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
