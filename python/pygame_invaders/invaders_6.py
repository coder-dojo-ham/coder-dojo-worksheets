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
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH/2
player_rect.bottom = HEIGHT-10

alien_img = pygame.image.load(asset_path + "Enemies/enemyRed1.png")
alien_rect = alien_img.get_rect()
alien_rect.centerx = WIDTH/2
alien_rect.top = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.centerx -= 5
    elif keys[pygame.K_RIGHT]:
        player_rect.centerx += 5
    screen.fill((0,0,0))
    screen.blit(player_img, player_rect)
    screen.blit(alien_img, alien_rect)    
    pygame.display.update()
    clock.tick(FPS)
