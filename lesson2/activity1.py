import pygame
pygame.init()

width, height = 500,500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('my game window')

font = pygame.font.SysFont('Arial', 24)
text_surface = font.render("I am a rectangle", True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (width // 2, 30))

#create rect and position it in center
rect_width, rect_height = 60, 50
rectangle = pygame.Rect(0, 0, rect_width, rect_height)
rectangle.center = (width//2, height//2)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.fill((255, 255, 0))
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (255, 0, 0), rectangle)

    
    pygame.display.flip()