import pygame
import random


MOVEMENT_SPEED = 5
FONT_SIZE = 72

screen_width, screen_height = 500, 400

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("background.jpg"),
                                          (screen_width, screen_height))

font = pygame.font.SysFont('Times New Roman', FONT_SIZE)

class sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(colour))

        #get position of our rectangle
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.x = min(max(0, self.rect.x), screen_width - self.rect.width)

        self.rect.y += y_change
        self.rect.y = min(max(0, self.rect.y), screen_height - self.rect.height)



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Collision')

all_sprites = pygame.sprite.Group()

sprite_width, sprite_height = 20, 30
sprite1 = sprite(pygame.Color('black'), sprite_width, sprite_height)

sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
sprite1.rect.y = random.randint(0, screen_height - sprite1.rect.height)

all_sprites.add(sprite1)

sprite2 = sprite(pygame.Color('red'), sprite_width, sprite_height)

sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)

all_sprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()

        x_change = 0
        y_change = 0

        if keys[pygame.K_RIGHT]:
            x_change += MOVEMENT_SPEED

        if keys[pygame.K_LEFT]:
            x_change -= MOVEMENT_SPEED

        if keys[pygame.K_DOWN]:
            y_change += MOVEMENT_SPEED

        if keys[pygame.K_UP]:
            y_change -= MOVEMENT_SPEED
            
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2,
                               (screen_height - win_text.get_height()) // 2))
        
    pygame.display.flip()
    clock.tick(90)

pygame.quit()