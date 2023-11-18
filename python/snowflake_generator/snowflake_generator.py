import colorsys
import math
import random
import typing

import pygame

WIDTH=400
HEIGHT=400
FPS = 60
WHITE = (255, 255, 255)
TURN_SIZE = math.pi / 3
PEN_WIDTH = 3


class Branch:
    distance: float
    length: float
    dist_anim_speed: float
    def __init__(self):
        self.distance = random.uniform(0.1, 0.9)
        self.length = random.uniform(0.1, 0.9)
        self.dist_anim_speed = random.uniform(-0.001, 0.001)
        self.length_anim_speed = random.uniform(-0.001, 0.001)

    def draw(self, surface: pygame.Surface, mid_x: float, mid_y: float, facing: float, branch_angle: float, flake_size: float):
        x = mid_x + math.cos(facing) * flake_size * self.distance
        y = mid_y + math.sin(facing) * flake_size * self.distance
        x2 = x + math.cos(facing + branch_angle) * flake_size * self.length
        y2 = y + math.sin(facing + branch_angle) * flake_size * self.length
        pygame.draw.line(surface, WHITE, (x, y), (x2, y2), width=PEN_WIDTH)


class SnowFlake:
    branches : typing.List[Branch]
    def __init__(self) -> None:
        sub_arm_count = random.randint(3, 10)
        self.branches = [Branch() for _ in range(sub_arm_count)]

    def draw(self, surface: pygame.Surface, angle: float, flake_size: float = None):
        mid_x, mid_y = WIDTH/2, HEIGHT/2
        for n in range(6):
            pygame.draw.line(surface, WHITE, 
                                (mid_x, mid_y), 
                                (mid_x + math.cos(angle) * flake_size, mid_y + math.sin(angle) * flake_size),
                                width=PEN_WIDTH)
            for branch in self.branches:
                branch.draw(surface, mid_x, mid_y, angle, TURN_SIZE, flake_size)
                branch.draw(surface, mid_x, mid_y, angle, -TURN_SIZE, flake_size)       
            angle += TURN_SIZE

    def animate(self):
        for sub_arm in self.branches:
            sub_arm.distance += sub_arm.dist_anim_speed
            if sub_arm.distance < 0.1:
                sub_arm.distance = 0.1
                sub_arm.dist_anim_speed = -sub_arm.dist_anim_speed
            elif sub_arm.distance > 0.9:
                sub_arm.distance = 0.9
                sub_arm.dist_anim_speed = -sub_arm.dist_anim_speed
            if random.randint(0, 1000) == 1:
                sub_arm.dist_anim_speed = -sub_arm.dist_anim_speed
            sub_arm.length += sub_arm.length_anim_speed
            if sub_arm.length < 0.1:
                sub_arm.length = 0.1
                sub_arm.length_anim_speed = -sub_arm.length_anim_speed
            elif sub_arm.length > 0.9:
                sub_arm.length = 0.9
                sub_arm.length_anim_speed = -sub_arm.length_anim_speed
            if random.randint(0, 1000) == 1:
                sub_arm.length_anim_speed = -sub_arm.length_anim_speed


def make_background(surface: pygame.Surface):
    light_per_row = 0.8 / HEIGHT
    # Get a blue hue
    hue = 0.6
    for y in range(HEIGHT):
        light = light_per_row * y
        color = [255 * c for c in colorsys.hsv_to_rgb(hue, 0.1 + 0.7 * (1-light), light)]
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))
    # draw a few random stars
    for n in range(random.randint(200, 500)):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(surface, WHITE, (x, y), random.randint(1, 2))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowflake")
clock = pygame.time.Clock()

background = pygame.Surface((WIDTH, HEIGHT))
make_background(background)
snowflake = SnowFlake()

flake_size = min(WIDTH, HEIGHT) * 0.3
facing = 0
per_frame = facing / FPS
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    snowflake.animate()
    snowflake.draw(screen, facing, flake_size)
    pygame.display.flip()
    facing += 0.01
    clock.tick(FPS)
