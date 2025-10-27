import pygame
pygame.init()

width, height = 500,500

colors = {
    'red' : pygame.Color('red'),
    'green' : pygame.Color('green'),
    'blue' : pygame.Color('blue'),
    'yellow' : pygame.Color('yellow')
}

keys = {
    'left' : pygame.K_LEFT,
    'right' : pygame.K_RIGHT,
    'up' : pygame.K_UP,
    'down' : pygame.K_DOWN
}

current_colour = pygame.Color('white')

rect_width, rect_height = 50, 50


# get the perfect center
x = (width - rect_width) // 2
y = (height - rect_height) // 2

# pygame screen of 500 x 500
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

        keyPressed = pygame.key.get_pressed()

    if keyPressed[keys['up']]:
        y = y - 1

    elif keyPressed[keys['down']]:
        y = y + 1

    elif keyPressed[keys['left']]:
        x = x - 1

    elif keyPressed[keys['right']]:
        x = x + 1

    x= min(max(0, x), width - rect_width )
    y = min(max(0, y), height - rect_height)
    rectangle= pygame.Rect(x, y, rect_width, rect_height)

    screen.fill((0, 0, 0))

    if x == 0:
        current_colour = colors['blue']
    elif x == width - rect_width: 
        current_colour = colors['red']
    elif y == 0:
        current_colour = colors['green']
    elif y == height - rect_height:
        current_colour = colors['yellow']

    pygame.draw.rect(screen, current_colour, rectangle)

    pygame.display.flip()

pygame.quit()
