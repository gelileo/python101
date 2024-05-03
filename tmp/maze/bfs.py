import pygame
import sys
from collections import deque

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Maze dimensions
MAZE_WIDTH = 20
MAZE_HEIGHT = 15

# Cell size
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Maze data (1s are walls, 0s are empty cells)
maze_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Start and end points
start = (1, 1)
end = (MAZE_HEIGHT - 2, MAZE_WIDTH - 2)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Solver")

# Cell colors
cell_colors = [(255, 255, 255), (50, 50, 50), (255, 0, 0), (0, 255, 0)]


# BFS algorithm
def bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < MAZE_HEIGHT
                and 0 <= ny < MAZE_WIDTH
                and maze[nx][ny] == 0
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny))
                visited.add((nx, ny))
    return False


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw maze
    for y, row in enumerate(maze_data):
        for x, cell in enumerate(row):
            color = cell_colors[cell]
            pygame.draw.rect(
                screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    # Draw start and end points
    pygame.draw.rect(
        screen, RED, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )
    pygame.draw.rect(
        screen, GREEN, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

    # Run BFS algorithm
    # if bfs(maze_data, start, end):
    #     print("Path found!")
    # else:
    #     print("No path found!")

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)
