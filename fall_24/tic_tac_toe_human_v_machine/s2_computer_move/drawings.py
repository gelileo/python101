import pygame
import math
from colors import BLUE, BLACK, GRAY, DARK_GRAY, WHITE
import menu


size_factor = 1


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

pygame.font.init()  # Initialize the font module

status_font = pygame.font.SysFont("Arial", status_font_size)
button_font = pygame.font.SysFont(None, button_font_size)

# Button rectangle for hover detection
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)


def draw_status(status, screen):
    text_surface = status_font.render(status, True, BLACK)
    screen.blit(
        text_surface,
        (
            (screen_width - text_surface.get_width()) // 2,
            screen_height - factored_size(150),
        ),
    )


def draw_button(mouse_pos, screen):
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
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


# Function to draw X or O in the center of the cell
def draw_shape(row, col, board, screen):
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


def draw_board(screen, board):
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
            draw_shape(row, col, board, screen)


def draw_cursor(mouse_pos):
    # Check if the mouse is hovering over the button
    if button_rect.collidepoint(mouse_pos):
        # Change cursor when hovering over the button
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        # Set to default cursor otherwise
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def redraw(screen, board, status, mouse_pos=[0, 0]):
    screen.fill(WHITE)
    draw_board(screen, board)
    draw_status(status, screen)
    draw_button(mouse_pos, screen)
    draw_cursor(mouse_pos)


def draw_menu(screen, mouse_pos):
    buttons = menu.game_level_buttons(
        screen_width, screen_height, button_width, button_height
    )
    screen.fill(WHITE)

    for button in buttons:
        button_rect = button["rect"]
        if button_rect.collidepoint(mouse_pos):
            button_color = DARK_GRAY  # Mouse is hovering over the button
            button_text_color = WHITE
        else:
            button_color = GRAY  # Mouse is not hovering over the button
            button_text_color = BLUE

        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        button_text = button_font.render(button["label"], True, button_text_color)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)
