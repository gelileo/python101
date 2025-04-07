# Completed code for Lesson 3
# This code includes player movement for interactive mode.

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
from colors import WALL_COLOR, START_COLOR, END_COLOR
from maze_data import MAZE1, START_POSITION, END_POSITION

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Maze")

# Player position
player_pos = list(START_POSITION)

# Draw the maze
def draw_maze():
    for row in range(len(MAZE1)):
        for col in range(len(MAZE1[0])):
            color = WALL_COLOR if MAZE1[row][col] == 1 else (255, 255, 255)
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

    # Draw player
    player_rect = pygame.Rect(
        player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, (0, 200, 200), player_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_pos = player_pos[:]
            if event.key == pygame.K_UP:
                new_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                new_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                new_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                new_pos[1] += 1

            # Check if the new position is valid
            if (
                0 <= new_pos[0] < len(MAZE1)
                and 0 <= new_pos[1] < len(MAZE1[0])
                and MAZE1[new_pos[0]][new_pos[1]] == 0
            ):
                player_pos[:] = new_pos

    screen.fill((0, 0, 0))
    draw_maze()
    pygame.display.flip()

pygame.quit()