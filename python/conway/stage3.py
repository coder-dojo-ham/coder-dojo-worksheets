import pygame

WIDTH=400
HEIGHT=400
CELL_SIZE = 5
COLS = WIDTH//CELL_SIZE
ROWS = HEIGHT//CELL_SIZE

FPS = 60
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

next_generation.fill(DEAD)
set_cell(5, 5, ALIVE)
screen.blit(next_generation, (0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    next_generation.fill(DEAD)
    for row in range(ROWS):
        for col in range(COLS):
            if row > 0 and get_cell(col, row-1) != DEAD:
                set_cell(col, row, ALIVE)
    screen.blit(next_generation, (0,0))
    pygame.display.flip()
    clock.tick(FPS)    
pygame.quit()

