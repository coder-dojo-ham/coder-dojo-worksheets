import colorsys
import math
import random

import pygame

WIDTH=400
HEIGHT=400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURN_SIZE = math.pi / 3
PEN_WIDTH = 3

class Branch:
    def __init__(self):
        self.distance = 1/ random.randint(1, 10)
        self.size = 1 / random.randint(1, 10)

    def draw(self, surface, mid_x, mid_y, angle, branch_angle, flake_size):
        scaled_distance = flake_size * self.distance
        scaled_size = flake_size * self.size
        x = mid_x + math.cos(angle) * scaled_distance
        y = mid_y + math.sin(angle) * scaled_distance
        x2 = x + math.cos(angle + branch_angle) * scaled_size
        y2 = y + math.sin(angle + branch_angle) * scaled_size
        pygame.draw.line(surface, WHITE, (x, y), (x2, y2), PEN_WIDTH)


class SnowFlake:
    def __init__(self, flake_size = 100):
        self.flake_size = flake_size
        self.branches = [Branch() for _ in range(random.randint(3, 10))]

    def draw(self, surface):
        mid_x, mid_y = WIDTH/2, HEIGHT/2
        angle = 0
        for n in range(6):
            pygame.draw.line(surface, WHITE, (mid_x, mid_y), 
                (mid_x + math.cos(angle)*self.flake_size, 
                mid_y + math.sin(angle)*self.flake_size), PEN_WIDTH)
            for branch in self.branches:
                branch.draw(surface, mid_x, mid_y, angle, TURN_SIZE, self.flake_size)
                branch.draw(surface, mid_x, mid_y, angle, -TURN_SIZE, self.flake_size)
            angle += TURN_SIZE
            
def make_background(surface):
    light_per_row = 0.8 / HEIGHT
    # Get a blue hue
    hue = 0.6
    for y in range(HEIGHT):
        light = light_per_row * y
        hsv = colorsys.hsv_to_rgb(hue, 0.1 + 0.7 * (1 - light), light)
        color = [int(255 * c) for c in hsv]
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowflake")

background = pygame.Surface((WIDTH, HEIGHT))
make_background(background)

snowflake = SnowFlake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    snowflake.draw(screen)
    pygame.display.flip()
pygame.quit()




