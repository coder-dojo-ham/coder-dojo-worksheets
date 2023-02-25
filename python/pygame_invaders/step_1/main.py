import pygame

from config import *
from player import Player
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invaders!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
