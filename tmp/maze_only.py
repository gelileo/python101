import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
MAZE_WIDTH, MAZE_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Maze Generator")

# Create a 2D list to represent the maze
maze = [[0 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]


# Function to generate the maze using Depth-First Search algorithm
def generate_maze(x, y):
    maze[y][x] = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            generate_maze(nx, ny)


# Function to draw the maze on the screen
def draw_maze():
    screen.fill(WHITE)
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(
                    screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
    pygame.display.flip()


# Generate the maze
generate_maze(1, 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze
    draw_maze()

pygame.quit()
