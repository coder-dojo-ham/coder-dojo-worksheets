import pygame

WIDTH=400
HEIGHT=400
CELL_SIZE = 5

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

next_generation.fill(DEAD)
set_cell(5, 5, ALIVE)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(next_generation, (0,0))
    pygame.display.flip()
    clock.tick(FPS)    
pygame.quit()
