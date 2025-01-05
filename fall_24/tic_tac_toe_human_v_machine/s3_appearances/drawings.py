import pygame
import math
from colors import Colors
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


button_font_size = factored_size(40)
status_font_size = factored_size(20)

pygame.font.init()  # Initialize the font module

status_font = pygame.font.SysFont("Arial", status_font_size)
button_font = pygame.font.SysFont(None, button_font_size)

# Button rectangle for hover detection
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)


def draw_status(status, screen):
    text_surface = status_font.render(status, True, colors.BUTTON_TEXT_COLOR)
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
        button_color = colors.BUTTON_COLOR_HOVER  # Mouse is hovering over the button
        button_text_color = colors.BUTTON_TEXT_COLOR_HOVER
    else:
        button_color = colors.BUTTON_COLOR  # Mouse is not hovering over the button
        button_text_color = colors.BUTTON_TEXT_COLOR

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    button_text = button_font.render("Start Over", True, button_text_color)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


def draw_x(screen, row, col, color, offset=0):
    pygame.draw.line(
        screen,
        color,
        (
            col * cell_size + shape_margin - (col * cell_padding) + offset,
            row * cell_size + shape_margin - (row * cell_padding),
        ),
        (
            col * cell_size + cell_size - shape_margin - (col * cell_padding) + offset,
            row * cell_size + cell_size - shape_margin - (row * cell_padding),
        ),
        shape_x_width,
    )
    pygame.draw.line(
        screen,
        color,
        (
            col * cell_size + cell_size - shape_margin - (col * cell_padding) + offset,
            row * cell_size + shape_margin - (row * cell_padding),
        ),
        (
            col * cell_size + shape_margin - (col * cell_padding) + offset,
            row * cell_size + cell_size - shape_margin - (row * cell_padding),
        ),
        shape_x_width,
    )


def draw_o(screen, row, col, color, offset=0):
    pygame.draw.circle(
        screen,
        color,
        (
            col * cell_size + cell_size // 2 - (col * cell_padding) + offset,
            row * cell_size + cell_size // 2 - (row * cell_padding),
        ),
        cell_size // 2 - shape_margin + factored_size(10),
        shape_o_radius,
    )


# Function to draw X or O in the center of the cell
def draw_shape(row, col, board, screen):
    player = board[row][col]
    if player == "X":
        # log(f"drawing {player} at ({row}, {col})")
        draw_x(screen, row, col, colors.CROSS_COLOR)
    elif player == "O":
        draw_o(screen, row, col, colors.CIRCLE_COLOR)


def draw_board(screen, board):
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(
                screen,
                colors.LINE_COLOR,
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


def redraw(screen, board, status, mouse_pos=[0, 0], mode="light", debugging=False):
    global colors, debug
    colors = Colors(mode)
    debug = debugging
    screen.fill(colors.BG_COLOR)
    draw_board(screen, board)
    draw_status(status, screen)
    draw_button(mouse_pos, screen)
    draw_cursor(mouse_pos)


def draw_menu(screen, mouse_pos, mode="light", debugging=False):
    global colors, debug
    colors = Colors(mode)
    debug = debugging

    buttons = menu.game_level_buttons(
        screen_width, screen_height, button_width, button_height
    )
    screen.fill(colors.BG_COLOR)

    for button in buttons:
        button_rect = button["rect"]
        if button_rect.collidepoint(mouse_pos):
            button_color = (
                colors.BUTTON_COLOR_HOVER
            )  # Mouse is hovering over the button
            button_text_color = colors.BUTTON_TEXT_COLOR_HOVER
        else:
            button_color = colors.BUTTON_COLOR  # Mouse is not hovering over the button
            button_text_color = colors.BUTTON_TEXT_COLOR

        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        button_text = button_font.render(button["label"], True, button_text_color)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)


def pulse_winning_symbols(screen, cells, symbol, frame_count):
    """
    Pulsates the winning symbols in the provided cells.

    Args:
        cells (list of tuples): The winning cells as (row, col).
        symbol (str): "X" or "O" (the winning symbol).
    """
    # Choose colors based on the symbol
    if symbol == "X":
        base_color = colors.CROSS_COLOR
        pulse_color = colors.CROSS_PULSE_COLOR
    elif symbol == "O":
        base_color = colors.CIRCLE_COLOR
        pulse_color = colors.CIRCLE_PULSE_COLOR

    # Pulse effect
    color = pulse_color if (frame_count // 10) % 2 == 0 else base_color
    offsets = [-10, 10, -10, 10, 0]
    offset = offsets[(frame_count // 10) % len(offsets)]
    for row, col in cells:
        if symbol == "X":
            draw_x(screen, row, col, color, offset)

        elif symbol == "O":
            draw_o(screen, row, col, color, offset)


def flash_background(screen):
    """
    Flashes the background with a bright yellow color.
    """
    for _ in range(2):
        screen.fill((255, 255, 0, 0.5))
        pygame.display.update()
        pygame.time.delay(200)
        screen.fill(colors.BG_COLOR)
        pygame.display.update()
        pygame.time.delay(200)
