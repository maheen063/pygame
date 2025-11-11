import pygame
import random
import constants
from enemy import Enemy

img_width, img_height = 50, 50
black_color = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

# Background
background = pygame.transform.scale(pygame.image.load("backdrop.jpg"),
                                    (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

# Caption and icon
pygame.display.set_caption("Space Invader")
# icon = pygame.image.load("ufo.png")
# pygame.display.set_icon(icon)

# player image
playerImg = pygame.transform.scale(pygame.image.load("pacman.png"),
                                    (img_width, img_height))
playerX = constants.PLAYER_START_X
playerY = constants.PLAYER_START_Y

# Bullet
bulletImg = pygame.transform.scale(pygame.image.load("bullet.jpg"),
                                    (15, 15))

bulletY = constants.PLAYER_START_Y
bulletX = constants.PLAYER_START_X
bulletY_change = constants.BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.SysFont('Times New Roman', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('aprilafont.otf', 64)

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, black_color)
    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, black_color)
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 15, y + 10))

# Game loop
running = True
clock = pygame.time.Clock()

# creating enemies using sprite group
enemy_group = pygame.sprite.Group()
enemy_img = pygame.transform.scale(pygame.image.load("enemy.png").convert_alpha(), (img_width, img_height))

# creating 6 enemies
for _ in range(6):
    enemy = Enemy(enemy_img)
    enemy_group.add(enemy)

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # for pressing and releasing keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and bullet_state == "ready":
            #bulletX = playerX
                fire_bullet(bulletX, bulletY)

    # for keys continuously being held
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= 2
    if keys[pygame.K_RIGHT]:
        playerX += 2

    #Player Movement
    playerX = max(0, min(playerX, constants.SCREEN_WIDTH - playerImg.get_width()))

    enemy_group.update()  # Moves all enemies
    enemy_group.draw(screen)  # Draws all enemies

    for enemy in enemy_group:
        if enemy.rect.y > constants.MAX_Y_ALLOWED_ENEMY:
            for e in enemy_group:
                e.rect.y = constants.RESET_ENEMIES_POSITION
            game_over_text()
            break

        if bullet_state == "fire":
            bullet_rect = bulletImg.get_rect(topleft=(bulletX, bulletY))
            # works for rectangle
            if enemy.rect.colliderect(bullet_rect):
                bulletY = constants.PLAYER_START_Y
                bullet_state = "ready"
                score_value += 1

        enemy.rect.x = random.randint(0, constants.SCREEN_WIDTH - enemy.rect.width)
        enemy.rect.y = random.randint(constants.ENEMY_START_Y_MIN, constants.ENEMY_START_Y_MAX)

    if bulletY <= 0:
        bulletY = constants.PLAYER_START_Y
        bullet_state = "ready"

    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.flip()
    clock.tick(30)