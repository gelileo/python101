import pygame
import random
import sys
from colors import *
from layouts import *
from appearance import brick

button_h = 50
width = WINDOW_WIDTH
height = WINDOW_HEIGHT + 2 * button_h
brick_texture = brick()
# Maze data (1s are walls, 0s are empty cells)
maze_data = [
    [random.choice([0, 1]) for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)
]


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Editor")

# Button
button = pygame.Rect(width / 2 - 50, (height - button_h) - button_h // 2, 100, 50)

# Main loop
while True:
    screen.fill(WHITE)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Flip cell value on click

            cell_x = mouse_x // CELL_SIZE
            cell_y = mouse_y // CELL_SIZE
            if 0 <= cell_x < MAZE_WIDTH and 0 <= cell_y < MAZE_HEIGHT:
                maze_data[cell_y][cell_x] = 1 - maze_data[cell_y][cell_x]
            # Output maze data on button click
            if button.collidepoint(pygame.mouse.get_pos()):
                print(maze_data)

    # Draw maze
    for y, row in enumerate(maze_data):
        for x, cell in enumerate(row):
            if cell == 1:
                screen.blit(brick_texture, (x * CELL_SIZE, y * CELL_SIZE))
            else:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )

    # Draw button

    font = pygame.font.Font(None, 34)
    if button.collidepoint(mouse_x, mouse_y):
        button_color = DARK_GRAY  # Mouse is hovering over the button
        button_text_color = WHITE
    else:
        button_color = GRAY  # Mouse is not hovering over the button
        button_text_color = BLUE

    pygame.draw.rect(screen, button_color, button, border_radius=10)
    text = font.render("Output", True, button_text_color)
    screen.blit(text, (button.x + 10, button.y + 10))

    # Highlight cell on mouseover
    x, y = pygame.mouse.get_pos()
    cell_x = x // CELL_SIZE
    cell_y = y // CELL_SIZE
    if 0 <= cell_x < MAZE_WIDTH and 0 <= cell_y < MAZE_HEIGHT:
        pygame.draw.rect(
            screen,
            YELLOW_GREEN,
            (cell_x * CELL_SIZE, cell_y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            2,
        )

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)
