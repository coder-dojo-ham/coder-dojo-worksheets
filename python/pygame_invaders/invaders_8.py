import pygame

WIDTH=800
HEIGHT=600
FPS=30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invaders!")
clock = pygame.time.Clock()
asset_path = "assets/space-shooter-redux/PNG/"
player_img = pygame.image.load(asset_path + "playerShip1_blue.png")
alien_img = pygame.image.load(asset_path + "Enemies/enemyRed1.png")
bullet_img = pygame.image.load(asset_path + "Lasers/laserBlue01.png")

player_rect = player_img.get_rect()
player_rect.centerx = WIDTH/2
player_rect.bottom = HEIGHT-10

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = 10
        self.speedx = 5

    def update(self):
        self.rect.centerx += self.speedx
        if self.rect.right > WIDTH:
          self.speedx = -5
        if self.rect.left < 0:
          self.speedx = 5

    def draw(self):
        screen.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
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

    def draw(self):
        screen.blit(self.image, self.rect)

alien = Alien()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(alien)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet()
                all_sprites.add(bullet)
                bullets.add(bullet)            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.centerx -= 5
    elif keys[pygame.K_RIGHT]:
        player_rect.centerx += 5
    all_sprites.update()
    screen.fill((0,0,0))
    screen.blit(player_img, player_rect)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)