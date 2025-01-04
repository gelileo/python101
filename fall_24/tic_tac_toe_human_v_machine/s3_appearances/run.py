import pygame
import sys
import random
import math
import os
from game_logic import check_win, check_tie
import argparse
from log import Logger


# from colors import WHITE, BLUE, BLACK, GRAY, DARK_GRAY
from drawings import (
    redraw,
    screen_height,
    screen_width,
    cell_size,
    button_rect,
    button_width,
    button_height,
    draw_menu,
    pulse_winning_symbols,
    flash_background,
)
from computer import computer_move
from menu import game_level_buttons, clicked_level

# Add the directory containing the module to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))
from particle import Particle, draw_particles, celebration

# Parse command line arguments

parser = argparse.ArgumentParser(description="Tic Tac Toe")
parser.add_argument("--dark", action="store_true", help="Enable dark mode")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

mode = "light"
if args.dark:
    mode = "dark"

debug = False
if args.verbose:
    debug = True

logger = Logger(debug)

# Initialize Pygame
pygame.init()


view = "menu"
level = "Easy"
status = "Player X's turn"

# Variable to keep track of current player
current_player = "X"

# Global list to store particles
particles = []

# Define the game board
board = [["" for _ in range(3)] for _ in range(3)]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TIC TAC TOE")

menu_buttons = game_level_buttons(
    screen_width, screen_height, button_width, button_height
)


def log(msg):
    logger.log(msg)


def log_boar_simple(board):
    for row in board:
        print([cell if (cell is not None and cell != "") else " " for cell in row])
    print()


def log_board(board):
    for i, row in enumerate(board):
        # Print the row with '|' as cell delimiters, replacing None with a space
        print(
            " | ".join(
                cell if (cell is not None and cell != "") else " " for cell in row
            )
        )
        # Print a row divider after each row except the last
        if i < len(board) - 1:
            print("-" * (len(row) * 4 - 1))
    print()


def show_menu(mouse_pos):
    global view
    view = "menu"
    draw_menu(screen, mouse_pos)


def show_game(mouse_pos):

    global view, win, winning_cells
    view = "game"
    print("Game started for level:", level)

    global board, current_player, game_over, status
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    status = "Player X's turn"
    win = False
    winning_cells = []
    redraw(screen, board, status, mouse_pos)


def reset_game(mouse_pos):
    show_menu(mouse_pos)


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
    # log(f"Now waiting for player {current_player}:")
    status = f"Player {current_player}'s turn"


def check_game(mouse_pos, desc):

    global current_player
    global status
    global board
    global particles, game_over
    global frame_count
    # log(f"Entering check_game for {desc} move")
    win, winning_cells = check_win(board, current_player)
    if win:
        game_over = True
        if current_player == "X":
            status = "Player X wins!"
        else:
            status = "Computer wins!"
        flash_background(screen)
        celebration(mouse_pos[0], mouse_pos[1], particles)
        return (True, win, winning_cells)

    if check_tie(board):
        status = "It's a draw!"
        game_over = True
        # redraw(mouse_pos)
        return (True, win, winning_cells)

    log_board(board)
    # log("Continue")
    return (False, win, winning_cells)


clock = pygame.time.Clock()

win = False
winning_cells = []
running = True
game_over = False
frame_count = 0
# Main loop
while running:
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position continuously

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if view == "menu":
                level = clicked_level(mouse_pos, menu_buttons)
                if level:
                    show_game(mouse_pos)
            else:
                if button_rect.collidepoint(mouse_pos):
                    reset_game(mouse_pos)
                else:
                    row, col = get_cell_position(mouse_pos)
                    # log(f"Clicked cell: {row}, {col}")
                    if row < 3 and col < 3:
                        if not game_over and board[row][col] == "":
                            board[row][col] = current_player
                            log("")
                            log(f"Player {current_player}: ({row}, {col})")
                            end, win, winning_cells = check_game(mouse_pos, "player")
                            if end:
                                break
                            switch_player()

                            computer_move(board, "O", level, logger)
                            end, win, winning_cells = check_game(mouse_pos, "computer")
                            if end:
                                break
                            switch_player()

    if view == "menu":
        draw_menu(screen, mouse_pos, mode)
    else:
        redraw(screen, board, status, mouse_pos, mode, debug)
        particles = draw_particles(particles, screen)
        if win:
            pulse_winning_symbols(screen, winning_cells, current_player, frame_count)

    pygame.display.flip()
    clock.tick(30)
    frame_count += 1


# Quit Pygame
pygame.quit()
sys.exit()
