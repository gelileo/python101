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
pygame.display.set_caption("TIC TAc TOE")

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


# Variable to keep track of current player
current_player = "X"

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_cell_position(mouse_pos)
            print("Clicked cell:", row, col)
            if board[row][col] == "":
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"

    # Clear the screen
    screen.fill(WHITE)

    # Draw the game board
    draw_board()

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
