import pygame

from config import *
from player import Player
from weapons import Bullet
from alien import spawn_aliens, collide_aliens

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invaders!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
alien_bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

spawn_aliens(all_sprites, alien_bullets)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect)
                all_sprites.add(bullet)
                bullets.add(bullet)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.centerx -= 5
    elif keys[pygame.K_RIGHT]:
        player.rect.centerx += 5
    all_sprites.update()
    collide_aliens(bullets, all_sprites)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
