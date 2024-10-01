import pygame
from typing import List, NamedTuple
import random

WIDTH=400
HEIGHT=400
FPS = 60
MAX_PARTICLES = 16000
EMITTER_COUNT = 20
PARTICLE_SIZE = 1

YELLOW = (255, 255, 0)
RED = (255, 0, 0)

def get_intensity_colour(intensity):
    factor = min(1, intensity/128)
    return (255 * factor, (255-intensity) * factor, 0, intensity)

class ParticleType:
    x: int
    y: int
    intensity: int
    
    def __init__(self, x, y, intensity):
        self.x = x
        self.y = y
        self.intensity = intensity
    
    def draw(self, surface):
        # Lets start with smaller radius 3 circles
        pygame.draw.circle(surface,
           get_intensity_colour(self.intensity),
           (self.x, self.y),
           PARTICLE_SIZE, width=0)

# embers are a particle generator
class EmberType(NamedTuple):
    x: int
    y: int
    intensity: int
    radius: int
    
    def draw(self, surface):
        # Draw a pygame filled circle at the location
        # Colour is determined by intensity - ie red + other 2 colours being the intensity?
        # Width 0 to fill
        
        """pygame.draw.circle(surface,
           get_intensity_colour(self.intensity),
           (self.x, self.y),
           self.radius, width=0)"""
    
    def emit_particle(self) -> ParticleType:
        distance_x = random.randint(-self.radius, self.radius)
        distance_y = random.randint(-self.radius, self.radius)
        intensity = max(5,
                self.intensity - (5*abs(distance_x))
            )
        return ParticleType(
            self.x + distance_x,
            self.y + distance_y,
            intensity
        )

    @staticmethod
    def generate():
        return EmberType(
            x=random.randint(0, WIDTH),
            y=random.randint(HEIGHT - 10, HEIGHT),
            intensity=random.randint(200, 255),
            radius=50
        )


embers: List[EmberType] = []
particles: List[ParticleType] = []


def make_embers():
    number_of_embers = EMITTER_COUNT
    for _ in range(number_of_embers):
        ember = EmberType.generate()
        embers.append(ember)
    
def draw_embers(surface):
    for ember in embers:
        ember.draw(surface)
        
def update_embers():
    while len(particles) < MAX_PARTICLES:
        particles.append(
            random.choice(embers).emit_particle()
        )

def update_particles():
    wind_lower_y = HEIGHT-22
    wind_upper_y = HEIGHT-20
    wind_direction = 1
    for particle in particles:
        # Fire goes upward
        particle.y -= random.randint(1, 7)
        if particle.y >= wind_lower_y and particle.y <= wind_upper_y:
            particle.x += wind_direction
        # Looses intensity
        particle.intensity -= random.randint(1, 10)
        # Some will die
        if particle.intensity <= 0 or particle.y <= 1:
            particles.remove(particle)

def draw_particles(surface):
    for particle in particles:
        particle.draw(surface)

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
    update_particles()
    update_embers()
    screen.fill((0,0,0,0))
    draw_embers(screen)
    draw_particles(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
