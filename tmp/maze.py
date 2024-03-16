import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 80  # Adjusted block size to fit 10x10 blocks
MAZE_WIDTH, MAZE_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
PLAYER_COLOR = (0, 0, 255)  # Blue color for player

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Maze Game")

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
    color = YELLOW
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(
                    screen,
                    color,
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                )
                color = YELLOW if color == BROWN else BROWN
    pygame.display.flip()


# Function to draw the player figure
def draw_player(x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()


# Generate the maze
generate_maze(1, 1)

# Initial position of the player
player_x, player_y = BLOCK_SIZE, BLOCK_SIZE

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Calculate the new position based on key presses
    new_player_x, new_player_y = player_x, player_y
    if keys[pygame.K_LEFT]:
        new_player_x -= 10
    if keys[pygame.K_RIGHT]:
        new_player_x += 10
    if keys[pygame.K_UP]:
        new_player_y -= 10
    if keys[pygame.K_DOWN]:
        new_player_y += 10

    # Check for collision with maze walls
    maze_x, maze_y = new_player_x // BLOCK_SIZE, new_player_y // BLOCK_SIZE
    if 0 <= maze_x < MAZE_WIDTH and 0 <= maze_y < MAZE_HEIGHT:
        if maze[maze_y][maze_x] == 0:
            # Update player position if it's not colliding with a wall
            player_x, player_y = new_player_x, new_player_y

    # Draw the maze and player
    draw_maze()
    draw_player(player_x, player_y)

pygame.quit()
