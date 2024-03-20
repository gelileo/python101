import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
cell_size = 200
cell_padding = 10
screen_width = 3 * cell_size - 2 * cell_padding
screen_height = screen_width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TIC TAC TOE")

# Colors
WHITE = (255, 255, 255)
BLUE = (64, 128, 255, 160)
BLACK = (0, 0, 0)

# Define the game board
board = [["" for _ in range(3)] for _ in range(3)]


# Function to draw the game board
def draw_board():
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    col * cell_size - (col * cell_padding),
                    row * cell_size - (row * cell_padding),
                    cell_size,
                    cell_size,
                ),
                cell_padding,
                border_radius=5,
            )
            draw_shape(row, col)


# Function to get the cell position from mouse click
def get_cell_position(mouse_pos):
    row = mouse_pos[1] // cell_size
    col = mouse_pos[0] // cell_size
    return row, col


# Function to draw X or O in the center of the cell
def draw_shape(row, col):
    player = board[row][col]
    if player == "X":
        print(f"drawing {current_player} at ({row}, {col})")
        pygame.draw.line(
            screen,
            BLACK,
            (
                col * cell_size + 50 - (col * cell_padding),
                row * cell_size + 50 - (row * cell_padding),
            ),
            (
                col * cell_size + cell_size - 50 - (col * cell_padding),
                row * cell_size + cell_size - 50 - (row * cell_padding),
            ),
            25,
        )
        pygame.draw.line(
            screen,
            BLACK,
            (
                col * cell_size + cell_size - 50 - (col * cell_padding),
                row * cell_size + 50 - (row * cell_padding),
            ),
            (
                col * cell_size + 50 - (col * cell_padding),
                row * cell_size + cell_size - 50 - (row * cell_padding),
            ),
            25,
        )
    elif player == "O":
        pygame.draw.circle(
            screen,
            "red",
            (
                col * cell_size + cell_size // 2 - (col * cell_padding),
                row * cell_size + cell_size // 2 - (row * cell_padding),
            ),
            cell_size // 2 - 50 + 10,
            20,
        )


#
# Variable to keep track of current player
current_player = "X"

# Switch player


def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    print(f"Now waiting for player {current_player}:")

# Check win


def check_row(board):
    global winner
    for row in board:
        if all(cell == current_player for cell in row):
            return True

    return False


def check_column(board):
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)):
            return True
    return False


def check_diagnal(board):
    if all(board[i][i] == current_player for i in range(3)) or all(board[i][2 - i] == current_player for i in range(3)):
        return True
    return False


def check_tie(board):
    return all(cell != '' for row in board for cell in row)


def check_win():
    if check_diagnal(board) or check_row(board) or check_column(board):
        print(f"The winner is {current_player}")
        return True
    else:
        return False


clock = pygame.time.Clock()


def redraw():
    draw_board()
    pygame.display.flip()
    clock.tick(30)


# Init the screen
screen.fill(WHITE)
draw_board()
pygame.display.flip()
running = True
game_over = False
# Main loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_cell_position(mouse_pos)
            print("Clicked cell:", row, col)
            if not game_over and board[row][col] == "":
                board[row][col] = current_player
                needs_redraw = True
                if check_win():
                    game_over = True
                    redraw()
                    break

                if check_tie(board):
                    game_over = True
                    redraw()
                    break

                switch_player()
                redraw()


# Quit Pygame
pygame.quit()
sys.exit()
