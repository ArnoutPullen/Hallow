<<<<<<< HEAD
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
=======
import pygame
import random
import sys

pygame.mixer.init()
pygame.init()

spider_up = pygame.image.load("images/spider_up.png")
spider_down = pygame.image.load("images/spider_down.png")
ghost_left = pygame.image.load("images/ghost_left.png")
ghost_right = pygame.image.load("images/ghost_right.png")
pumpkin_right = pygame.image.load("images/pumpkin_right.png")
pumpkin_left = pygame.image.load("images/pumpkin_left.png")
background = pygame.image.load("images/bg.png")
key_img = pygame.image.load("images/key.png")
finish_img = pygame.image.load("images/finish.png")
box = pygame.image.load("images/box.png")
menu_bg = pygame.image.load("images/menu.png")
pygame.mixer.music.load("audio/bgmusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.05)
ghost_sound = pygame.mixer.Sound("audio/ghost.ogg")
spider_sound = pygame.mixer.Sound('audio/hit.ogg')
key_sound = pygame.mixer.Sound('audio/key.ogg')
open_sound = pygame.mixer.Sound('audio/open.ogg')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 100, 0)
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Halloween Frogger")
clock = pygame.time.Clock()
fps = 30
font = pygame.font.SysFont("consolas", 16)
font_big = pygame.font.SysFont("consolas", 52)
timer = 60
player_health = 10

sprites_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
spider_group = pygame.sprite.Group()
finish_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pumpkin_left
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 250
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.move(-10, 0)
            self.image = pumpkin_left
        if key_pressed[pygame.K_RIGHT]:
            self.move(10, 0)
            self.image = pumpkin_right
        if key_pressed[pygame.K_UP]:
            self.move(0, -10)
        if key_pressed[pygame.K_DOWN]:
            self.move(0, 10)

    def move(self, speed_x, speed_y):
        self.rect.x += speed_x
        self.rect.y += speed_y

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if speed_x > 0:
                    self.rect.right = wall.rect.left
                elif speed_x < 0:
                    self.rect.left = wall.rect.right
                elif speed_y > 0:
                    self.rect.bottom = wall.rect.top
                elif speed_y < 0:
                    self.rect.top = wall.rect.bottom

        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.top < 150:
            self.rect.top = 150
        elif self.rect.bottom > height:
            self.rect.bottom = height


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = box
        self.rect = self.image.get_rect()
>>>>>>> 176ed0bbeeff0a7a5d876f444c6f65c8db84baf0
        self.rect.x = x
        self.rect.y = y


<<<<<<< HEAD
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

    def init(self):
        pygame.init()
        pygame.display.set_caption(Settings.gameTitle)
        self.start = time.time()
        self.font = pygame.font.Font(Settings.font_type, Settings.font_size)
        self.load()

    def load(self):
        x = 0
        y = 0
        for row in self.level:
        # for row in Levels.get_level():
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
=======
class Spider(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 1

    def update(self):
        self.rect.y += self.speed_y

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.speed_y > 0:
                    self.rect.bottom = wall.rect.top
                    self.speed_y *= -1
                else:
                    self.rect.top = wall.rect.bottom
                    self.speed_y *= -1

        if self.rect.right > width:
            self.speed_x *= -1
        elif self.rect.left < 0:
            self.speed_x *= -1
        elif self.rect.top < 180:
            self.speed_y *= -1
        elif self.rect.bottom > height:
            self.speed_y *= -1

        if self.speed_y > 0:
            self.image = spider_down
        elif self.speed_y < 0:
            self.image = spider_up

        if pygame.sprite.groupcollide(spider_group, player_group, True, False):
            spider_sound.play()
            global player_health
            player_health -= 1


class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ghost_right
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 500)
        self.rect.y = random.randrange(100, 500)
        self.speed_x = random.randrange(-10, 10)
        self.speed_y = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.speed_x > 0:
            self.image = ghost_right
        if self.speed_x < 0:
            self.image = ghost_left

        if self.rect.right > width:
            self.speed_x *= -1
        if self.rect.left < 0:
            self.speed_x *= -1
        if self.rect.bottom > height:
            self.speed_y *= -1
        if self.rect.top < 0:
            self.speed_y *= -1

        if pygame.sprite.groupcollide(ghost_group, player_group, True, False):
            ghost_sound.play()
            global player_health
            player_health -= 3


class Finish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = finish_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500

    def update(self):
        if pygame.sprite.groupcollide(finish_group, player_group, False, False):
            if not key.pickup:
                text = font.render("It's locked...", True, white)
                screen.blit(text, (50, 480))


class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = key_img
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 560
        self.pickup = False

    def update(self):
        if self.rect.colliderect(player.rect):
            key_sound.play()
            self.pickup = True
        if key.pickup:
            text = font.render("You've found the key...", True, white)
            screen.blit(text, (100, 100))
            text = font.render("Go!", True, white)
            screen.blit(text, (100, 122))
            text = font.render("Head to your brother!", True, white)
            screen.blit(text, (100, 144))

            self.rect.x = player.rect.x + 65
            self.rect.y = player.rect.y


class Health(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 5))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        for i in range(player_health, 0, -1):
            self.image = pygame.Surface((player_health * 80, 5))
            if player_health < 3:
                self.image.fill(red)
            elif player_health < 6:
                self.image.fill(yellow)
            elif player_health >= 6:
                self.image.fill(green)


player = Player()
finish = Finish()
key = Key()
health = Health()
walls = []


def init():
    ghost_group.empty()
    spider_group.empty()

    level_pattern = [
        "                ",
        "                ",
        "                ",
        "                ",
        "WW    W   WWWW  ",
        "W               ",
        "W   WWWWWWWW    ",
        "   W       WWWWW",
        "   W            ",
        "        W  W   W",
        "        W  W  WW",
        "    WW     W    ",
    ]

    x = 0
    y = 0
    for row in level_pattern:
        for col in row:
            if col == "W":
                walls.append(Wall(x, y))
            x += 50
        y += 50
        x = 0
    for i in range(15):
        spider = Spider(random.randrange(100, 500, 20), random.randrange(220, 550, 50))
        # sprites_group.add(spider)
        spider_group.add(spider)
    for i in range(3):
        ghost = Ghost()
        # sprites_group.add(ghost)
        ghost_group.add(ghost)
    sprites_group.add(walls, player, finish, key, health)
    finish_group.add(finish)
    player_group.add(player)
    key_group.add(key)
    wall_group.add(walls)

    global timer, player_health
    player_health = 10
    timer = 60
    player.__init__()
    key.rect.x = 750
    key.rect.y = 560
    key.pickup = False


menu = True

while True:
    clock.tick(fps)
    if menu:
        screen.fill(black)
        text = font_big.render("Halloween Frogger", True, white)
        x = (width // 2) - (text.get_width() // 2)
        y = (height // 2) - (text.get_height() // 2)
        screen.blit(text, (x, y))
        text = font.render("Press SPACE to play", True, white)
        x = (width // 2) - (text.get_width() // 2)
        y = (height * 0.75) - (text.get_height() // 2)
        screen.blit(text, (x, y))
        pygame.display.flip()
        while True:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE]:
                menu = False
                init()
                break
    # event checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # draw
    screen.blit(background, (0, 0))
    sprites_group.update()
    ghost_group.update()
    spider_group.update()
    sprites_group.draw(screen)
    ghost_group.draw(screen)
    spider_group.draw(screen)
    # countdown timer
    timer -= (1 / 30)
    if timer < 20:
        text = font_big.render(str(round(timer)), True, red)
    else:
        text = font_big.render(str(round(timer)), True, white)
    screen.blit(text, (150, 50))
    # game over
    if timer <= 0:
        menu = True
    if player_health <= 0:
        menu = True
    if pygame.sprite.groupcollide(finish_group, player_group, False, False) and key.pickup:
        menu = True
    # update
    pygame.display.flip()
>>>>>>> 176ed0bbeeff0a7a5d876f444c6f65c8db84baf0
