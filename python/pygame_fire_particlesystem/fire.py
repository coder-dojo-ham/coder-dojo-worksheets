import pygame
import colorsys
from typing import List, Tuple, NamedTuple
import random

WIDTH=600
HEIGHT=800
FPS = 60

# embers are a particle generator
class EmberType(NamedTuple):
    x: int
    y: int
    intensity: int
    
    def draw(self, surface):
        # Draw a pygame filled circle at the location
        # Colour is determined by intensity - ie red + other 2 colours being the intensity?
        # Width 0 to fill
        
        pygame.draw.circle(surface,
           (255, self.intensity, self.intensity),
           (self.x, self.y),
           10, width=0)

class ParticleType(NamedTuple):
    x: int
    y: int
    intensity: int

embers: List[EmberType] = []
particles: List[ParticleType] = []
max_particles = 200

def make_embers():
    number_of_embers = random.randint(0,5)
    for n in range(number_of_embers):
        ember: EmberType = EmberType(
            x=random.randint(0, WIDTH),
            y=random.randint(HEIGHT - 10, HEIGHT),
            intensity=random.randint(200, 255)
            )
        embers.append(ember)
        
def draw_embers(surface):
    for ember in embers:
        ember.draw(surface)
"""
def update_particles():
    global particles
    for particle in particles:
        # Fire goes upward
        particle.y -= 1
        # Looses intensity
        particle.intensity -= 5
    # Some will die
    particles = [particle for particle in particles if particle.intensity > 0]
    
def update_embers():
    while len(particles) < max_particles:
        source = random.choice(embers)
        
"""

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire")
clock = pygame.time.Clock()
make_embers()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_embers(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
