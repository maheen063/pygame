import pygame
import random
from constants import SCREEN_WIDTH, ENEMY_START_Y_MIN, ENEMY_START_Y_MAX, ENEMY_SPEED_X, ENEMY_SPEED_Y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyImg):
        super().__init__()
        self.image = enemyImg
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        self.speed_x = ENEMY_SPEED_X
        self.speed_y = ENEMY_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x

        if self.rect.x <=0 or self.rect.x >=SCREEN_WIDTH - self.rect.width:
            self.speed_x *= -1 
            self.rect.y += self.speed_y
            