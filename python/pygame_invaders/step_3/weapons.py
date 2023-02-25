import pygame
from config import *

bullet_img = pygame.image.load(ASSET_PATH + "Lasers/laserBlue01.png")


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = player_rect.centerx
        self.rect.bottom = player_rect.top
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


alien_bullet_img = pygame.image.load(ASSET_PATH + "Lasers/laserRed04.png")


class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, alien_rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = alien_rect.centerx
        self.rect.top = alien_rect.bottom
        self.speedy = 10
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()
