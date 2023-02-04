import pygame

WIDTH=400
HEIGHT=400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Stars")

x = 100
y = 150
size = 10
pygame.draw.circle(screen, (255, 255, 255), (x, y), size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
