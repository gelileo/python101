# Starter code for Lesson 1
# This code draws a static maze with a start and end point.

import pygame
from constants import CELL_SIZE
from colors import WALL_COLOR, START_COLOR, END_COLOR

# Calculate SCREEN_WIDTH and SCREEN_HEIGHT dynamically
NUM_ROWS = 7  # Replace with actual value or configuration
NUM_COLS = 12  # Replace with actual value or configuration
SCREEN_WIDTH = NUM_COLS * CELL_SIZE
SCREEN_HEIGHT = NUM_ROWS * CELL_SIZE

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Static Maze")

# Define the maze layout
MAZE = [
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
]

START_POSITION = (6, 0)
END_POSITION = (0, 11)

# Draw the maze
def draw_maze():
    for row in range(len(MAZE)):
        for col in range(len(MAZE[0])):
            color = WALL_COLOR if MAZE[row][col] == 1 else (255, 255, 255)
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    # Draw start and end points
    start_rect = pygame.Rect(
        START_POSITION[1] * CELL_SIZE, START_POSITION[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, START_COLOR, start_rect)

    end_rect = pygame.Rect(
        END_POSITION[1] * CELL_SIZE, END_POSITION[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, END_COLOR, end_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_maze()
    pygame.display.flip()

pygame.quit()