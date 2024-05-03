import pygame
from layouts import *

BRICK_COLOR = (201, 143, 95)


def brick():
    # Create a surface with the brick texture
    brick_texture = pygame.Surface((CELL_SIZE, CELL_SIZE))
    brick_texture.fill(BRICK_COLOR)
    pygame.draw.rect(
        brick_texture, (255, 255, 255), (0, 0, CELL_SIZE, CELL_SIZE), 1
    )  # Draw a white border
    pygame.draw.rect(
        brick_texture, (0, 0, 0), (2, 2, CELL_SIZE - 4, CELL_SIZE - 4), 1
    )  # Draw a black border
    return brick_texture
