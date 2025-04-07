# Completed code for Lesson 2
# This code includes mouse event handling for the maze editor.

import pygame
import random
import sys
from constants import *
from colors import *
from mazes import maze_data1

BUTTON_H = 40
BUTTON_W = 100
FONT_SIZE = 28

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 2 * BUTTON_H))
pygame.display.set_caption("Maze Editor")

# Button Rect
button = pygame.Rect(
    (SCREEN_WIDTH - BUTTON_W) // 2,
    (SCREEN_HEIGHT + BUTTON_H) - BUTTON_H // 2,
    BUTTON_W,
    BUTTON_H,
)

# Maze data
maze_data = maze_data1

# Draw the maze
def draw_maze():
    for row in range(len(maze_data)):
        for col in range(len(maze_data[0])):
            color = WALL_COLOR if maze_data[row][col] == 1 else UNEXPLORED_COLOR
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

# Draw the button
def draw_button():
    pygame.draw.rect(screen, GRAY, button, border_radius=10)
    font = pygame.font.Font(None, FONT_SIZE)
    button_text = font.render("Export", True, BLUE)
    text_rect = button_text.get_rect(center=button.center)
    screen.blit(button_text, text_rect)

# Handle mouse click
def handle_mouse_click(pos):
    col = pos[0] // CELL_SIZE
    row = pos[1] // CELL_SIZE
    if 0 <= row < len(maze_data) and 0 <= col < len(maze_data[0]):
        maze_data[row][col] = 1 - maze_data[row][col]
    elif button.collidepoint(pos):
        print("Maze exported!")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event.pos)

    screen.fill(WHITE)
    draw_maze()
    draw_button()
    pygame.display.flip()

pygame.quit()