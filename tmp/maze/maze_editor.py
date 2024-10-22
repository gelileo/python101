import pygame
import random
import sys
from colors import *
from layouts import *
from appearance import brick
from mazes import maze_data1
import fire


brick_texture = brick()


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


def get_cell_position(mouse_pos):
    """
    Get cell position from mouse position
    Args:
        mouse_pos: tuple[int, int]
        Returns: tuple[int, int]
    """
    cell_x = mouse_pos[0] // CELL_SIZE
    cell_y = mouse_pos[1] // CELL_SIZE
    return cell_x, cell_y


def draw_maze(screen, maze_data):
    for y, row in enumerate(maze_data):
        for x, cell in enumerate(row):
            if cell == 1:
                screen.blit(brick_texture, (x * CELL_SIZE, y * CELL_SIZE))
            else:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )


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
            YELLOW_GREEN,
            (cell_x * CELL_SIZE, cell_y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
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
        button_color = BUTTON_COLORS["hover"]
        button_text_color = BUTTON_COLORS["hove_text"]
    else:
        # Set to default cursor otherwise
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # Set button color to normal
        button_color = BUTTON_COLORS["normal"]
        button_text_color = BUTTON_COLORS["text"]

    # slightly shrink button when clicked
    if mouse_pushed_in[0] and button_rect.collidepoint(mouse_pos):
        button_rect = button_rect.inflate(-10, -10)

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

    font = pygame.font.Font(None, FONT_SIZE)
    button_text = font.render("Export", True, button_text_color)

    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


def is_valid_cell(cell_x, cell_y):
    """
    Check if cell is within maze bounds
    """
    return 0 <= cell_x < MAZE_WIDTH and 0 <= cell_y < MAZE_HEIGHT


def handle_mouse_click(mouse_pos, maze_data, button):
    """
    Flip cell value on click
    Output maze data on button click
    Args:
        mouse_pos: tuple[int, int]
        maze_data: list[list[int]]
        button: pygame.Rect
    """
    cell_x, cell_y = get_cell_position(mouse_pos)
    if is_valid_cell(cell_x, cell_y):
        maze_data[cell_y][cell_x] = 1 - maze_data[cell_y][cell_x]
    # Output maze data on button click
    elif button.collidepoint(pygame.mouse.get_pos()):
        output(maze_data)


def redraw_maze(screen, maze_data, button, mouse_pos, mouse_pushed_in):
    screen.fill(WHITE)
    # Draw maze
    draw_maze(screen, maze_data)

    # Draw button
    draw_button(button, screen, mouse_pos, mouse_pushed_in)

    # Highlight cell on mouseover
    highlight_cell(screen, mouse_pos)

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)


# Maze data (1s are walls, 0s are empty cells)
def init_maze(start_new):
    if start_new:
        maze_data = [
            [random.choice([0, 1]) for _ in range(MAZE_WIDTH)]
            for _ in range(MAZE_HEIGHT)
        ]
    else:
        maze_data = maze_data1
    return maze_data


def quit():
    pygame.quit()
    sys.exit()


def run(start_new=False):
    width = WINDOW_WIDTH
    height = WINDOW_HEIGHT + 2 * BUTTON_H

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Editor")

    # Button Rect
    button = pygame.Rect(
        (width - BUTTON_W) // 2,
        (height - BUTTON_H) - BUTTON_H // 2,
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(mouse_pos, maze_data, button)

        mouse_pushed_in = pygame.mouse.get_pressed()
        redraw_maze(screen, maze_data, button, mouse_pos, mouse_pushed_in)

    quit()


if __name__ == "__main__":
    fire.Fire({"run": run})
    # run()
