import pygame
from config import *
from explosion import Explosion

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


def collide_player_alien_bullets(all_sprites, player, alien_bullets):
    if not player.alive():
        return
    hits = pygame.sprite.spritecollide(player, alien_bullets, True)
    if hits:
        player.kill()
        explosion = Explosion(player.rect.center, player_explosion_anim)
        all_sprites.add(explosion)
