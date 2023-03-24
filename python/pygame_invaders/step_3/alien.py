import random

import pygame

from config import *
from weapons import AlienBullet


alien_img = pygame.image.load(ASSET_PATH + "Enemies/enemyRed1.png")

class Alien(pygame.sprite.Sprite):
    fire_rate = 1300
    def __init__(self, all_sprites, alien_bullets):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = 10
        self.speedx = 5

        self.all_sprites = all_sprites
        self.alien_bullets = alien_bullets
        # firing
        self.next_shot = pygame.time.get_ticks() + random.randint(Alien.fire_rate, Alien.fire_rate * 2)

    def update(self):
        self.rect.centerx += self.speedx
        if self.rect.right > WIDTH:
            self.speedx = -5
        if self.rect.left < 0:
            self.speedx = 5
        # fire if it's time
        now = pygame.time.get_ticks()
        if now > self.next_shot:
            self.next_shot = now + random.randint(Alien.fire_rate, Alien.fire_rate * 2)
            bullet = AlienBullet(self.rect)
            self.all_sprites.add(bullet)
            self.alien_bullets.add(bullet)

aliens = pygame.sprite.Group()

def spawn_aliens(all_sprites, alien_bullets):
    for i in range(10):
        alien = Alien(all_sprites, alien_bullets)
        alien.rect.x = 100 + i * 100
        all_sprites.add(alien)
        aliens.add(alien)
