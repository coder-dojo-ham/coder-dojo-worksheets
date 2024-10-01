import pygame
import colorsys
from typing import List, Tuple, NamedTuple
import random

WIDTH=600
HEIGHT=800
FPS = 60


def make_background(surface: pygame.Surface):
    surface.fill((0,0,0))
    light = 0
    light_per_row = 0.8 / HEIGHT
    # Get a blue hue
    hue = 0.6
    for y in range(HEIGHT, 0, -1):
        light += light_per_row
        color = [255 * c for c in colorsys.hsv_to_rgb(hue, 0.1 + 0.7 * (1-light), 0.2 + light)]
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

def draw_foreground(surface: pygame.Surface):
    # draw a city scene
    surface.fill((0, 0, 0, 0))
    # start with the ground
    ground_height = 100
    ground_color = (100, 100, 100, 255)
    pygame.draw.rect(surface, ground_color, (0, HEIGHT-ground_height, WIDTH, ground_height))
    # add some buildings
    building_colors = [
        (200, 200, 200, 255),
        (150, 150, 150, 255),
        (100, 100, 100, 255),
        (50, 50, 50, 255)
    ]
    building_width = 50
    for n in range(0, 5):
        building_color = random.choice(building_colors)
        building_height = random.randint(100, 300)
        building_x = random.randint(0, WIDTH-building_width)
        building_rect = (building_x, HEIGHT-building_height-ground_height, building_width, building_height)
        pygame.draw.rect(surface, building_color, building_rect)
    # draw a christmas tree
    tree_color = (0, 255, 0, 255)
    tree_width = 100
    tree_height = 200
    tree_x = WIDTH/3 - tree_width/2
    tree_y = HEIGHT - ground_height - tree_height
    pygame.draw.rect(surface, tree_color, (tree_x, tree_y, tree_width, tree_height))
    


class SnowFlake:
    x: int # x position
    y: int # y position
    speed: int # speed of fall
    settled: bool # has it settled?

    def __init__(self) -> None:
            self.x = random.randint(0, WIDTH-1)
            self.y = 0
            self.speed = random.randint(1, 5)
            self.settled = False


class SnowStorm:
    """Snowstorm is a particle system"""
    def __init__(self, max_snow: int, foreground: pygame.Surface):
        self.max_snow = max_snow
        self.foreground : pygame.Surface = foreground
        # x, y, speed, settled
        self.snow_flakes: List[SnowFlake] = []
        self.settled_snow: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.snow_surface: pygame.Surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        # wind
        self.wind = 0

    def update(self):
        # move snow flakes, and update their settled status
        for snow_flake in self.snow_flakes:
            self.wind += random.randint(-100, 100) * 0.001
            if self.wind < -2:
                self.wind = -2
            elif self.wind > 2:
                self.wind = 2
            # move down by the speed
            if random.randint(0, 100) < 30:
                snow_flake.x = (snow_flake.x + random.randint(-1, 1)) % WIDTH
            proposed_y = snow_flake.y + snow_flake.speed
            # check if we're off the bottom of the screen
            if proposed_y >= HEIGHT:
                snow_flake.settled = True
            # check if we're on settled snow (use alpha)
            elif self.settled_snow.get_at((snow_flake.x, proposed_y))[3] > 0:
                snow_flake.settled = True
                snow_flake.y += snow_flake.speed - 1
            # check if we are on the foreground (use alpha)
            elif self.foreground.get_at((snow_flake.x, proposed_y))[3] > 0:
                snow_flake.settled = True
                snow_flake.y += snow_flake.speed - 1
            else:
                snow_flake.y = proposed_y

        # Add settled snow flakes to the settled snow surface
        for snow_flake in self.snow_flakes:
            if snow_flake.settled:
                self.settled_snow.set_at((snow_flake.x, snow_flake.y), (255, 255, 255, 255))

        # remove settled snow flakes
        self.snow_flakes = [snow_flake for snow_flake in self.snow_flakes if not snow_flake.settled]
        # renew the particles
        if len(self.snow_flakes) < self.max_snow:
            self.snow_flakes.append(SnowFlake())

    def draw(self, screen):
        # clear the snow surface
        self.snow_surface.fill((0, 0, 0, 0))
        # draw the snow flakes
        for snow_flake in self.snow_flakes:
            self.snow_surface.set_at((snow_flake.x, snow_flake.y), (255, 255, 255, 255))
        # draw the settled snow
        screen.blit(self.settled_snow, (0, 0))
        screen.blit(self.snow_surface, (0, 0))




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowy Scene")
clock = pygame.time.Clock()

background = pygame.Surface((WIDTH, HEIGHT))
make_background(background)
foreground = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
draw_foreground(foreground)
snow_storm = SnowStorm(400, foreground)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    screen.blit(foreground, (0, 0))
    snow_storm.update()
    snow_storm.draw(screen)
    
    pygame.display.update()
    clock.tick(FPS)
