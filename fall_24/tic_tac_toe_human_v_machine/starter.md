```
import pygame
import sys
import random
import math
from lib.particle import Particle

# Initialize Pygame
pygame.init()

pygame.font.init()  # Initialize the font module

size_factor = 0.75


def factored_size(value):
    return math.floor(value * size_factor)


# Set up the screen

cell_size = factored_size(150)
cell_padding = factored_size(10)
shape_margin = factored_size(35)
shape_x_width = factored_size(25)
shape_o_radius = factored_size(20)
screen_width = 3 * cell_size - 2 * cell_padding
status_height = factored_size(200)
screen_height = screen_width + status_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TIC TAC TOE")

# Colors
WHITE = (255, 255, 255)
BLUE = (64, 128, 255, 160)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)
DARK_GRAY = (128, 128, 128)  # Darker color for hover effect

# Button properties
button_width, button_height = factored_size(200), factored_size(50)

button_x = (screen_width - button_width) // 2
button_y = (
    screen_height - (status_height + button_height) // 2
)  # Position button at the bottom
button_color = GRAY
button_text_color = BLUE


button_font_size = factored_size(40)
status_font_size = factored_size(20)
status_font = pygame.font.SysFont("Arial", status_font_size)
button_font = pygame.font.SysFont(None, button_font_size)

# Button rectangle for hover detection
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Define the game board
board = [["" for _ in range(3)] for _ in range(3)]

# Global list to store particles
particles = []


def celebration(x, y, particles):
    for _ in range(100):  # Number of particles
        color = random.choice(
            [(255, 255, 255), (255, 215, 0), (255, 69, 0)]
        )  # Particle colors
        particles.append(Particle(x, y, color))


def reset_game(mouse_pos):
    global board, current_player, game_over, status
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    status = "Player X's turn"
    redraw(mouse_pos)


def draw_button(mouse_pos):
    # print(f"Drawing button at {mouse_pos}")
    # Check if mouse is over the button
    if button_rect.collidepoint(mouse_pos):
        button_color = DARK_GRAY  # Mouse is hovering over the button
        button_text_color = WHITE
    else:
        button_color = GRAY  # Mouse is not hovering over the button
        button_text_color = BLUE

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    button_text = button_font.render("Start Over", True, button_text_color)
    # text_rect = button_text.get_rect(
    #     center=(button_x + button_width / 2, button_y + button_height / 2))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


status = "Player X's turn"


def draw_status():
    text_surface = status_font.render(status, True, BLACK)
    screen.blit(
        text_surface,
        (
            (screen_width - text_surface.get_width()) // 2,
            screen_height - factored_size(150),
        ),
    )


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
        # print(f"drawing {current_player} at ({row}, {col})")
        pygame.draw.line(
            screen,
            BLACK,
            (
                col * cell_size + shape_margin - (col * cell_padding),
                row * cell_size + shape_margin - (row * cell_padding),
            ),
            (
                col * cell_size + cell_size - shape_margin - (col * cell_padding),
                row * cell_size + cell_size - shape_margin - (row * cell_padding),
            ),
            shape_x_width,
        )
        pygame.draw.line(
            screen,
            BLACK,
            (
                col * cell_size + cell_size - shape_margin - (col * cell_padding),
                row * cell_size + shape_margin - (row * cell_padding),
            ),
            (
                col * cell_size + shape_margin - (col * cell_padding),
                row * cell_size + cell_size - shape_margin - (row * cell_padding),
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
            cell_size // 2 - shape_margin + factored_size(10),
            shape_o_radius,
        )


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
    if all(board[i][i] == current_player for i in range(3)) or all(
        board[i][2 - i] == current_player for i in range(3)
    ):
        return True
    return False


def check_tie(board):
    global status
    if all(cell != "" for row in board for cell in row):
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


def redraw(mouse_pos=[0, 0]):
    screen.fill(WHITE)
    draw_board()
    draw_status()
    draw_button(mouse_pos)


# Init the screen
running = True
game_over = False
# Main loop
while running:
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position continuously
    # Check if the mouse is hovering over the button
    if button_rect.collidepoint(mouse_pos):
        # Change cursor when hovering over the button
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        # Set to default cursor otherwise
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if button_rect.collidepoint(mouse_pos):
                reset_game(mouse_pos)
            else:
                row, col = get_cell_position(mouse_pos)
                print("Clicked cell:", row, col)
                if not game_over and board[row][col] == "":
                    board[row][col] = current_player
                    if check_win():
                        game_over = True
                        celebration(mouse_pos[0], mouse_pos[1], particles)
                        break

                    if check_tie(board):
                        game_over = True
                        break

                    switch_player()
                    # redraw(mouse_pos)
        # else:
        #     redraw(mouse_pos)
    redraw(mouse_pos)
    for particle in particles[:]:
        particle.update()
        particle.draw(screen)
        if particle.lifetime <= 0:
            particles.remove(particle)

    pygame.display.flip()
    clock.tick(30)


# Quit Pygame
pygame.quit()
sys.exit()

```
