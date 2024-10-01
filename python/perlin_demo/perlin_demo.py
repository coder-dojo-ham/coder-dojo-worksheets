
from typing import List

import pygame
from perlin_noise import PerlinNoise

WIDTH=600
HEIGHT=600

print("Setting up noise")
noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

def make_perlin_layer(source, width: int, height: int, amplitude: float) -> List[List[float]]:
    pic = []
    for i in range(width):
        noise_index = i/width
        row = [amplitude * source([noise_index, j/height]) for j in range(height)]
        pic.append(row)
    return pic
print("Making layers from noise")
layers = [
    make_perlin_layer(noise1, WIDTH, HEIGHT, 1),
    make_perlin_layer(noise2, WIDTH, HEIGHT, 0.5),
    make_perlin_layer(noise3, WIDTH, HEIGHT, 0.25),
    make_perlin_layer(noise4, WIDTH, HEIGHT, 0.125),
]

def make_pic_from_layers(offsets: List[int]) -> List[List[int]]:
    pic = []
    for i in range(WIDTH):
        noise_index = i/WIDTH
        offset_indexes = [offset + noise_index for offset in offsets]
        row = [
            sum(
                128 + int(layer[offset_index][j] * 127) for layer, offset_index in zip(layers, offset_indexes)
            )
            for j in range(HEIGHT)
        ]
        pic.append(row)
    return pic

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perlin!")
running = True
print("starting main loop")
offset2 = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pic = make_pic_from_layers([0, offset2, 0, 0])
    offset2 += 1
    for i in range(100):
        for j in range(100):
            val = int(128 + pic[i][j] * 127)
            screen.set_at((i, j), (val, val, val))
    pygame.display.update()
    print("Next frame")
