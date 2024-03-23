import pygame
import sys

# Layout Constants
SCREEN_WIDTH = 350
SCREEN_HEIGHT = 350

# Colors
WHITE = (255, 255, 255)
BLUE = (64, 128, 255, 160)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)
DARK_GRAY = (128, 128, 128)  # Darker color for hover effect

# Initialize Pygame
pygame.init()
pygame.font.init()  # Initialize the font module

status_font = pygame.font.SysFont("Arial", 15)
button_font = pygame.font.SysFont("Arial", 30)


# Game variables
board = [["" for _ in range(3)] for _ in range(3)]
status = "Player X's turn"
current_player = "X"
running = True
game_over = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
clock = pygame.time.Clock()


def reset_game():
    pass


def get_reset_button_rect():
    return pygame.Rect(0, 0, 0, 0)


def draw_reset_button():
    pass


def draw_status():
    print(status)


def draw_game_pieces(row, col):
    pass


def draw_board():
    for row in range(3):
        for col in range(3):
            # draw rects

            # draw X or O
            draw_game_pieces(row, col)


def redraw():
    screen.fill(WHITE)
    draw_board()
    draw_status()
    draw_reset_button()


# Function to get the cell position from mouse click
def get_cell_position(mouse_pos):
    return 0, 0


def check_row(board):
    return False


def check_column(board):
    return False


def check_diagnal(board):
    return False


def check_tie(board):
    # status = "It's a tie!"
    return False


def check_win(board):
    global status
    if check_diagnal(board) or check_row(board) or check_column(board):
        status = f"Game Over! The winner is {current_player}"
        return True
    else:
        return False


def switch_player():
    global current_player
    global status
    current_player = "O" if current_player == "X" else "X"
    status = f"Player {current_player}'s turn"


def clicked_reset_button(mouse_pos):
    return False


# Main loop
while running:
    mouse_pos = pygame.mouse.get_pos()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if clicked_reset_button(mouse_pos):
                reset_game(mouse_pos)
            else:
                if check_win(board):
                    game_over = True
                    break
                elif check_tie(board):
                    game_over = True
                    break

            switch_player()

    redraw()

    pygame.display.flip()
    clock.tick(30)


# Quit Pygame
pygame.quit()
sys.exit()
