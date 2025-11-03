import pygame
import random

pygame.init()

colors = {
    'blue' : pygame.Color('blue'),
    'light_blue' : pygame.Color('lightblue'),
    'dark_blue' : pygame.Color('darkblue'),
    'yellow' : pygame.Color('yellow'),
    'magenta' : pygame.Color('magenta'),
    'orange' : pygame.Color('orange'),
    'white' : pygame.Color('white'),
    'black' : pygame.Color('black')
}

screen_width, screen_height = 500,500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Boundry Sprite')

bg_colour=colors['blue']
screen.fill(bg_colour)

BG_COLOUR_CHANGE = pygame.USEREVENT + 1

class My_Sprite (pygame.sprite.Sprite):

    def __init__(self, colour, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):

        self.rect.x = self.rect.x + self.velocity[0]
        self.rect.y = self.rect.y + self.velocity[1]

        boundary_hit = False

        if self.rect.left == 0 or self.rect.right == (screen_width - self.rect.width):
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top == 0 or self.rect.bottom == (screen_height - self.rect.height):
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            self.change_colour()
            bg_colour_change_event = pygame.event.Event(BG_COLOUR_CHANGE)
            pygame.event.post(bg_colour_change_event)

    def change_colour(self):
        self.image.fill(random.choice(colors['blue'], colors['lightblue'], colors['darkblue']))

def change_background_color():
    global bg_color
    bg_color = random.choice([colors['yellow'], colors['white'], colors['magenta']])

all_sprites_list = pygame.sprite.Group()

sp_width, sp_height = 20, 30

sp1 = My_Sprite(colors['white'], sp_width, sp_height)

sp1.rect.x = random.randint(0, (screen_width - sp_width))
sp1.rect.y = random.randint(0, (screen_height - sp_height))

all_sprites_list.add(sp1)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == BG_COLOUR_CHANGE:
            change_background_color()

        all_sprites_list.update()

        screen.fill(bg_colour)

        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(120)


pygame.quit()