import pygame
import random
import sys
"""
openmaak geluid
achtervolgers
punten
hoi
"""
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
pygame.mouse.set_visible(False)

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
        # self.health = 10

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
        self.rect.x = x
        self.rect.y = y


class Spider(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 2

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
# spider = spider()
# ghost = ghost()
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
        "                ",
        "                ",
        "    WWWWWWWW    ",
        "   W          WW",
        "   W            ",
        "         W      ",
        "        W    WWW",
        "        W       ",
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
