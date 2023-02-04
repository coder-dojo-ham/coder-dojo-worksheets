import pygame
import random

WIDTH=400
HEIGHT=400
FPS=30
NUMBER_OF_STARS=100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Stars")
clock = pygame.time.Clock()

class Star:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0

stars = []
for i in range(NUMBER_OF_STARS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(1, 3)
    speed = random.randint(1, 5)
    star = Star(x, y, size, speed)
    stars.append(star)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for star in stars:
        star.draw()
        star.update()

    pygame.display.update()


