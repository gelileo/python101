import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
GRID_SIZE = 4
TILE_SIZE = 100
PADDING = 10
WIDTH = GRID_SIZE * (TILE_SIZE + PADDING) + PADDING
HEIGHT = WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
COLORS = {
    0: GRAY,
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Fonts
FONT = pygame.font.SysFont("Arial", 32)

# Game logic
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def add_new_tile():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4

def merge_tiles(row):
    new_row = [value for value in row if value != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [value for value in new_row if value != 0]
    new_row.extend([0] * (GRID_SIZE - len(new_row)))
    return new_row

def move(direction):
    global grid
    if direction == "up":
        grid = [merge_tiles([grid[j][i] for j in range(GRID_SIZE)]) for i in range(GRID_SIZE)]
    elif direction == "down":
        grid = [merge_tiles([grid[j][i] for j in range(GRID_SIZE - 1, -1, -1)]) for i in range(GRID_SIZE)]
    elif direction == "left":
        grid = [merge_tiles(row) for row in grid]
    elif direction == "right":
        grid = [merge_tiles(row[::-1])[::-1] for row in grid]

# Initial setup
add_new_tile()
add_new_tile()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move("up")
            elif event.key == pygame.K_DOWN:
                move("down")
            elif event.key == pygame.K_LEFT:
                move("left")
            elif event.key == pygame.K_RIGHT:
                move("right")
            add_new_tile()

    # Draw grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, COLORS[grid[i][j]], (j * (TILE_SIZE + PADDING) + PADDING, i * (TILE_SIZE + PADDING) + PADDING, TILE_SIZE, TILE_SIZE))
            if grid[i][j] != 0:
                text_surface = FONT.render(str(grid[i][j]), True, BLACK)
                text_rect = text_surface.get_rect(center=(j * (TILE_SIZE + PADDING) + PADDING + TILE_SIZE // 2, i * (TILE_SIZE + PADDING) + PADDING + TILE_SIZE // 2))
                screen.blit(text_surface, text_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
