import pygame
from config import *

player_img = pygame.image.load(ASSET_PATH + "playerShip1_blue.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10


player_explosion_anim = [
    pygame.image.load(ASSET_PATH + "Damage/playerShip1_damage3.png"),
    pygame.image.load(ASSET_PATH + "Damage/playerShip1_damage2.png"),
    pygame.image.load(ASSET_PATH + "Damage/playerShip1_damage1.png")
]


class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_explosion_anim[0]
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
            if self.frame == len(player_explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = player_explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


def collide_player_alien_bullets(all_sprites, player, alien_bullets):
    hits = pygame.sprite.spritecollide(player, alien_bullets, True)
    if hits:
        player.kill()
        explosion = PlayerExplosion(player.rect.center)
        all_sprites.add(explosion)
