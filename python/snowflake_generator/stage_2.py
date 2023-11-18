import math

import pygame

WIDTH=400
HEIGHT=400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class SnowFlake:
    def draw(self, surface):
        mid_x, mid_y = WIDTH/2, HEIGHT/2
        pygame.draw.line(surface, WHITE, (mid_x, mid_y), (mid_x, mid_y-100))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowflake")

snowflake = SnowFlake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    snowflake.draw(screen)
    pygame.display.flip()
pygame.quit()
