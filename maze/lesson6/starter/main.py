# Starter code for Lesson 6
# This code provides the basic structure for visualizing algorithm steps.

import pygame
from constants import CELL_SIZE
from colors import WALL_COLOR, PATH_COLOR, START_COLOR, END_COLOR
from maze_data import MAZE1, START_POSITION, END_POSITION

# Calculate SCREEN_WIDTH and SCREEN_HEIGHT dynamically
NUM_ROWS = 7  # Replace with actual value or configuration
NUM_COLS = 12  # Replace with actual value or configuration
SCREEN_WIDTH = NUM_COLS * CELL_SIZE
SCREEN_HEIGHT = NUM_ROWS * CELL_SIZE

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visualizing Algorithm Steps")

# Draw the maze
def draw_maze(visited):
    for row in range(len(MAZE1)):
        for col in range(len(MAZE1[0])):
            color = WALL_COLOR if MAZE1[row][col] == 1 else (255, 255, 255)
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    # Highlight visited cells
    for cell in visited:
        rect = pygame.Rect(cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, PATH_COLOR, rect)

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
visited = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_maze(visited)
    pygame.display.flip()

pygame.quit()