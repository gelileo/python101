#!/usr/bin/env python3
import pygame
import random
import sys
import colors
import constants
from mazes import maze_data1
import argparse
import json

BUTTON_H = 40
BUTTON_W = 100
FONT_SIZE = 28


def output(maze, file_name="mazes.py"):
    """
    Output maze data to a file
    Args:
        maze: list[list[int]]
        file_name: str, default="mazes.py"
    """
    with open(file_name, "w") as f:
        f.write("maze_data1 = [\n")
        for row in maze:
            f.write("        " + str(row) + ",\n")
        f.write("]\n")


def save_maze_to_file(maze, file_name="maze.json"):
    """Save the maze layout to a JSON file."""
    try:
        with open(file_name, "w") as f:
            json.dump(maze, f)
    except IOError as e:
        print(f"Error saving maze to file: {e}")


def load_maze_from_file(file_name="maze.json"):
    """Load the maze layout from a JSON file."""
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading maze from file: {e}")
        return None


def get_cell_position(mouse_pos):
    """
    Get cell position from mouse position
    Args:
        mouse_pos: tuple[int, int]
        Returns: tuple[int, int]
    """
    cell_x = mouse_pos[0] // constants.CELL_SIZE
    cell_y = mouse_pos[1] // constants.CELL_SIZE
    return cell_x, cell_y


def draw_maze(screen, maze):
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(
                c * constants.CELL_SIZE,
                r * constants.CELL_SIZE,
                constants.CELL_SIZE,
                constants.CELL_SIZE,
            )
            if maze[r][c] == 1:
                color = colors.WALL_COLOR
            else:
                color = colors.UNEXPLORED_COLOR
            pygame.draw.rect(screen, color, rect)


def highlight_cell(screen, mouse_pos):
    """
    Highlight cell boundary on mouseover
    Args:
        screen: pygame.Surface
        mouse_pos: tuple[int, int]
    """
    cell_x, cell_y = get_cell_position(mouse_pos)
    if is_valid_cell(cell_x, cell_y):
        pygame.draw.rect(
            screen,
            colors.FOCUS_COLOR,
            (
                cell_x * constants.CELL_SIZE,
                cell_y * constants.CELL_SIZE,
                constants.CELL_SIZE,
                constants.CELL_SIZE,
            ),
            2,
        )


def draw_button(button_rect, screen, mouse_pos, mouse_pushed_in):
    """
    Draw button on screen
    Args:
        button_rect: pygame.Rect
        screen: pygame.Surface
        mouse_pos: tuple[int, int],
        mouse_pushed_in: tuple[bool, bool, bool], whether mouse buttons are pressed, left_button, middle_button, right_button respectively
    """

    if button_rect.collidepoint(mouse_pos):
        # Change cursor when hovering over the button
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        # Change button color when hovering over the button
        button_color = colors.BUTTON_COLORS["hover"]
        button_text_color = colors.BUTTON_COLORS["hove_text"]
    else:
        # Set to default cursor otherwise
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # Set button color to normal
        button_color = colors.BUTTON_COLORS["normal"]
        button_text_color = colors.BUTTON_COLORS["text"]

    # slightly shrink button when clicked
    if mouse_pushed_in[0] and button_rect.collidepoint(mouse_pos):
        button_rect = button_rect.inflate(-10, -10)

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

    font = pygame.font.Font(None, FONT_SIZE)
    button_text = font.render("Export", True, button_text_color)

    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


def draw_reset_button(button_rect, screen, mouse_pos, mouse_pushed_in):
    """Draw a reset button on the screen."""
    if button_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        button_color = colors.BUTTON_COLORS["hover"]
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        button_color = colors.BUTTON_COLORS["normal"]

    if mouse_pushed_in[0] and button_rect.collidepoint(mouse_pos):
        button_rect = button_rect.inflate(-10, -10)

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    font = pygame.font.Font(None, FONT_SIZE)
    button_text = font.render("Reset", True, colors.BUTTON_COLORS["text"])
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


def is_valid_cell(cell_x, cell_y):
    """
    Check if cell is within maze bounds
    """
    return 0 <= cell_x < constants.NUM_COLS and 0 <= cell_y < constants.NUM_ROWS


def handle_mouse_click(mouse_pos, maze_data, button, reset_button, start_new):
    """
    Flip cell value on click
    Output maze data on button click
    Reset maze on reset button click
    Args:
        mouse_pos: tuple[int, int]
        maze_data: list[list[int]]
        button: pygame.Rect
        reset_button: pygame.Rect
        start_new: bool
    """
    cell_x, cell_y = get_cell_position(mouse_pos)
    if is_valid_cell(cell_x, cell_y):
        maze_data[cell_y][cell_x] = 1 - maze_data[cell_y][cell_x]
    elif button.collidepoint(mouse_pos):
        save_maze_to_file(maze_data)
    elif reset_button.collidepoint(mouse_pos):
        maze_data[:] = init_maze(start_new=True)


def redraw_maze(screen, maze_data, button, reset_button, mouse_pos, mouse_pushed_in):
    screen.fill(colors.WHITE)
    # Draw maze
    draw_maze(screen, maze_data)

    # Draw button
    draw_button(button, screen, mouse_pos, mouse_pushed_in)

    # Draw reset button
    draw_reset_button(reset_button, screen, mouse_pos, mouse_pushed_in)

    # Highlight cell on mouseover
    highlight_cell(screen, mouse_pos)

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)


# Maze data (1s are walls, 0s are empty cells)
def init_maze(start_new):
    if start_new:
        maze_data = [
            [random.choice([0, 1]) for _ in range(NUM_COLS)]
            for _ in range(NUM_ROWS)
        ]
    else:
        maze_data = maze_data1
    return maze_data


def quit():
    pygame.quit()
    sys.exit()


def main():
    parser = argparse.ArgumentParser(description="Maze Editor")
    parser.add_argument(
        "--new", action="store_true", help="Start with a new maze"
    )
    args = parser.parse_args()
    run(args.new)


def run(start_new=False):
    # Adjust the height to add more space for the buttons
    height = constants.SCREEN_HEIGHT + 2 * BUTTON_H  # Add extra height for buttons

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, height))
    pygame.display.set_caption("Maze Editor")

    # Adjust button positions to center them in the lower area
    button_spacing = 20  # Space between buttons
    total_button_width = 2 * BUTTON_W + button_spacing
    button_start_x = (constants.SCREEN_WIDTH - total_button_width) // 2

    # Button Rects
    export_button = pygame.Rect(
        button_start_x,
        height - BUTTON_H - 20,  # Adjusted to fit within the new height
        BUTTON_W,
        BUTTON_H,
    )

    reset_button = pygame.Rect(
        button_start_x + BUTTON_W + button_spacing,
        height - BUTTON_H - 20,  # Adjusted to fit within the new height
        BUTTON_W,
        BUTTON_H,
    )

    maze_data = init_maze(start_new)

    # Main loop
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(mouse_pos, maze_data, export_button, reset_button, start_new)

        mouse_pushed_in = pygame.mouse.get_pressed()
        redraw_maze(screen, maze_data, export_button, reset_button, mouse_pos, mouse_pushed_in)

    quit()


if __name__ == "__main__":
    main()
