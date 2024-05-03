import pygame
import sys
from mazes import maze_data1
from colors import GRID_COLOR, BRICK_COLOR, BLACK, WHITE
from layouts import *
from appearance import brick

# Pygame initialization
pygame.init()
pygame.font.init()

cell_pos_font = pygame.font.Font(None, 14)
brick_texture = brick()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Peek")


def draw_maze():
    screen.fill(BLACK)
    draw_grid()
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze_data1[y][x] == 1:
                screen.blit(brick_texture, (x * CELL_SIZE, y * CELL_SIZE))


def draw_cell_pos(mouse_x, mouse_y):
    cell_x = mouse_x // CELL_SIZE
    cell_y = mouse_y // CELL_SIZE
    cell_pos_text = cell_pos_font.render(f"({cell_x}, {cell_y})", True, WHITE)
    screen.blit(cell_pos_text, (mouse_x + 10, mouse_y + 10))


def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))


while True:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_maze()
    draw_cell_pos(x, y)
    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
