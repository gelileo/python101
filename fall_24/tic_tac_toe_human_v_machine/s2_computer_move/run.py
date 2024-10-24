import pygame
import sys
import random
import math
import os
from game_logic import check_win, check_tie
from colors import WHITE, BLUE, BLACK, GRAY, DARK_GRAY
from drawings import redraw, screen_height, screen_width, cell_size, button_rect
from computer import computer_move

# Add the directory containing the module to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))
from particle import Particle, draw_particles, celebration

# Initialize Pygame
pygame.init()


status = "Player X's turn"

# 'X' will start the game
# 'O' will be the computer
current_player = "X"

# Global list to store particles
particles = []

# Define the game board
board = [["" for _ in range(3)] for _ in range(3)]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TIC TAC TOE")


def reset_game(mouse_pos):
    global board, current_player, game_over, status
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    status = "Player X's turn"
    redraw(screen, board, status, mouse_pos)


# Function to get the cell position from mouse click
def get_cell_position(mouse_pos):
    row = mouse_pos[1] // cell_size
    col = mouse_pos[0] // cell_size
    return row, col


# Switch player
def switch_player():
    global current_player
    global status
    current_player = "O" if current_player == "X" else "X"
    # print(f"Now waiting for player {current_player}:")
    status = f"Player {current_player}'s turn"


clock = pygame.time.Clock()


running = True
game_over = False
# Main loop
while running:
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position continuously

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_pos):
                reset_game(mouse_pos)
            else:
                row, col = get_cell_position(mouse_pos)
                # print("Clicked cell:", row, col)
                if not game_over and board[row][col] == "":
                    board[row][col] = current_player
                    if check_win(board, current_player):
                        game_over = True
                        status = f"Game Over! The winner is {current_player}"
                        celebration(mouse_pos[0], mouse_pos[1], particles)
                        break

                    if check_tie(board):
                        status = "It's a tie!"
                        game_over = True
                        # redraw(mouse_pos)
                        break

                    # switch_player()
                    computer_move(board)

    redraw(screen, board, status, mouse_pos)
    particles = draw_particles(particles, screen)

    pygame.display.flip()
    clock.tick(30)


# Quit Pygame
pygame.quit()
sys.exit()
