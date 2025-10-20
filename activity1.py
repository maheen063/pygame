import pygame
pygame.init()

width, height = 500,500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('my game window')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 0, 0))
    pygame.display.flip()