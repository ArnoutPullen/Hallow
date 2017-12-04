import pygame

player1 = ''
player2 = ''

XO = "X"

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

run = 1

def init():
    global player1, player2
    player1 = input('Enter player 1 name: ')
    check = input('Do you want to play with another player or computer? Enter player or computer: ')
    if(check == 'player'):
        player2 = input('Enter player 2 name: ')
    elif(check == 'computer'):
        player2 = 'pc'
    else:
        print('input incorrect')
        init()
init()

print(player1)
print(player2)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Tic Tac Toe XO')

while (run == 1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = 0