import pygame
import sys

# Initialize Pygame
pygame.init()

pygame.font.init()  # Initialize the font module
status_font = pygame.font.SysFont("Arial", 20)

# Set up the screen
cell_size = 150
cell_padding = 10
shape_margin = 35
shape_x_width = 25
shape_o_radius = 20
screen_width = 3 * cell_size - 2 * cell_padding
screen_height = screen_width + 200
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
                col * cell_size + shape_margin - (col * cell_padding),
                row * cell_size + shape_margin - (row * cell_padding),
            ),
            (
                col * cell_size + cell_size -
                shape_margin - (col * cell_padding),
                row * cell_size + cell_size -
                shape_margin - (row * cell_padding),
            ),
            shape_x_width,
        )
        pygame.draw.line(
            screen,
            BLACK,
            (
                col * cell_size + cell_size -
                shape_margin - (col * cell_padding),
                row * cell_size + shape_margin - (row * cell_padding),
            ),
            (
                col * cell_size + shape_margin - (col * cell_padding),
                row * cell_size + cell_size -
                shape_margin - (row * cell_padding),
            ),
            shape_x_width,
        )
    elif player == "O":
        pygame.draw.circle(
            screen,
            "red",
            (
                col * cell_size + cell_size // 2 - (col * cell_padding),
                row * cell_size + cell_size // 2 - (row * cell_padding),
            ),
            cell_size // 2 - shape_margin + 10,
            shape_o_radius,
        )


status = ''


def draw_status():
    text_surface = status_font.render(status, False, BLACK)
    screen.blit(text_surface, ((screen_width -
                text_surface.get_width()) // 2,
                               screen_height - 150))


#
# Variable to keep track of current player
current_player = "X"

# Switch player


def switch_player():
    global current_player
    global status
    current_player = "O" if current_player == "X" else "X"
    # print(f"Now waiting for player {current_player}:")
    status = f"Player {current_player}'s turn"

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
    global status
    if all(cell != '' for row in board for cell in row):
        status = "It's a tie!"
        return True
    else:
        return False


def check_win():
    global status
    if check_diagnal(board) or check_row(board) or check_column(board):
        # print(f"The winner is {current_player}")
        status = f"Game Over! The winner is {current_player}"
        return True
    else:
        return False


clock = pygame.time.Clock()


def redraw():
    screen.fill(WHITE)
    draw_board()
    draw_status()
    pygame.display.flip()


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

    clock.tick(30)


# Quit Pygame
pygame.quit()
sys.exit()
