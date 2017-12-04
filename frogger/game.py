import pygame

# screen
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 0, 0))
pygame.display.set_caption("Halloween Memory")
pygame.init()

# loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    pygame.display.flip()



pygame.quit()