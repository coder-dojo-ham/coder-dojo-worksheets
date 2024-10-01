import pygame
import random

WIDTH=400
HEIGHT=400
CELL_SIZE = 20
COLS = WIDTH//CELL_SIZE
ROWS = HEIGHT//CELL_SIZE

FPS = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALIVE = WHITE
DEAD = BLACK

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway")
clock = pygame.time.Clock()

next_generation = pygame.Surface((WIDTH, HEIGHT))

def set_cell(cell_x, cell_y, colour):
    x = cell_x * CELL_SIZE
    y = cell_y * CELL_SIZE
    pygame.draw.rect(next_generation,
                     colour,
                     (x, y, CELL_SIZE, CELL_SIZE),
                     width=0)

def get_cell(cell_x, cell_y):
    x = cell_x * CELL_SIZE
    y = cell_y * CELL_SIZE
    return screen.get_at((x, y))


def count_neighbours(cell_x, cell_y):
    neighbours = 0
    if cell_y > 0:
        if cell_x > 0 and get_cell(cell_x - 1, cell_y - 1) != DEAD:
            neighbours += 1
        if get_cell(cell_x, cell_y - 1) != DEAD:
            neighbours += 1
        if cell_x < COLS-1 and get_cell(cell_x + 1, cell_y - 1)!= DEAD:
            neighbours += 1
    if cell_x > 0 and get_cell(cell_x - 1, cell_y)!= DEAD:
        neighbours += 1
    if cell_x < COLS-1 and get_cell(cell_x + 1, cell_y)!= DEAD:
        neighbours += 1
    if cell_y < ROWS-1:
        if cell_x > 0 and get_cell(cell_x - 1, cell_y + 1)!= DEAD:
            neighbours += 1
        if get_cell(cell_x, cell_y + 1)!= DEAD:
            neighbours += 1
        if cell_x < COLS-1 and get_cell(cell_x + 1, cell_y + 1)!= DEAD:
            neighbours += 1
    return neighbours
    
def apply_rules(cell_x, cell_y):
    neighbours = count_neighbours(cell_x, cell_y)
    state = get_cell(cell_x, cell_y)
    if state == DEAD and neighbours == 3:
        set_cell(cell_x, cell_y, ALIVE)
    else:
        if neighbours < 2 or neighbours > 3:
            set_cell(cell_x, cell_y, DEAD)

next_generation.fill(DEAD)
for n in range(50):
    set_cell(random.randint(0, COLS), random.randint(0, ROWS), ALIVE)
screen.blit(next_generation, (0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    next_generation.fill(DEAD)
    for row in range(ROWS):
        for col in range(COLS):
            apply_rules(col, row)
    screen.blit(next_generation, (0,0))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()


