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


explosion_anim = [
    pygame.image.load(ASSET_PATH + "Effects/star1.png"),
    pygame.image.load(ASSET_PATH + "Effects/star2.png"),
    pygame.image.load(ASSET_PATH + "Effects/star3.png")
]


class AlienExplosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


def collide_aliens(bullets, all_sprites):
    for alien in aliens:
        hits = pygame.sprite.spritecollide(alien, bullets, True)
        if hits:
            alien.kill()
            explosion = AlienExplosion(alien.rect.center)
            all_sprites.add(explosion)
