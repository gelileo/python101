# Completed code for Lesson 9
# This code includes enhancements to the maze editor, such as reset and dynamic resizing.

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
from colors import WALL_COLOR, UNEXPLORED_COLOR, START_COLOR, END_COLOR
from mazes import maze_data1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Maze Editor")

# Draw the maze
def draw_maze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = WALL_COLOR if maze[row][col] == 1 else UNEXPLORED_COLOR
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

# Reset the maze
def reset_maze():
    return [[0 for _ in range(len(maze_data1[0]))] for _ in range(len(maze_data1))]

# Main loop
maze = maze_data1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset the maze
                maze = reset_maze()

    screen.fill((0, 0, 0))
    draw_maze(maze)
    pygame.display.flip()

pygame.quit()