import pygame
import random

WIDTH=800
HEIGHT=600
FPS=30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invaders!")
clock = pygame.time.Clock()
asset_path = "assets/space-shooter-redux/PNG/"
player_img = pygame.image.load(asset_path + "playerShip1_blue.png")
bullet_img = pygame.image.load(asset_path + "Lasers/laserBlue01.png")

alien_img = pygame.image.load(asset_path + "Enemies/enemyRed1.png")
alien_bullet_img = pygame.image.load(asset_path + "Lasers/laserRed04.png")

explosion_anim = [
    pygame.image.load(asset_path + "Effects/star1.png"),
    pygame.image.load(asset_path + "Effects/star2.png"),
    pygame.image.load(asset_path + "Effects/star3.png")
]

player_explosion_anim = [
    pygame.image.load(asset_path + "Damage/playerShip1_damage3.png"),
    pygame.image.load(asset_path + "Damage/playerShip1_damage2.png"),
    pygame.image.load(asset_path + "Damage/playerShip1_damage1.png")
]

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()
alien_bullets = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10


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


class Alien(pygame.sprite.Sprite):
    fire_rate = 1000
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = 10
        self.speedx = 5
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
            all_sprites.add(bullet)
            alien_bullets.add(bullet)


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


def collide_aliens(aliens, bullets, all_sprites):
    for alien in aliens:
        hits = pygame.sprite.spritecollide(alien, bullets, True)
        if hits:
            alien.kill()
            explosion = AlienExplosion(alien.rect.center)
            all_sprites.add(explosion)


def collide_player_alien_bullets(player, alien_bullets):
    hits = pygame.sprite.spritecollide(player, alien_bullets, True)
    if hits:
        player.kill()
        explosion = PlayerExplosion(player.rect.center)
        all_sprites.add(explosion)


player = Player()
all_sprites.add(player)


for i in range(10):
    alien = Alien()
    alien.rect.x = 100 + i * 100
    all_sprites.add(alien)
    aliens.add(alien)


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
    collide_aliens(aliens, bullets, all_sprites)
    collide_player_alien_bullets(player, alien_bullets)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
