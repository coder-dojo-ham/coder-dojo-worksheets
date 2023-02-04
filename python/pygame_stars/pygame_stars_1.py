import pygame

WIDTH=400
HEIGHT=400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Stars")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
