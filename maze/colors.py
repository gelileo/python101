# import pygame

# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200, 128)
DARK_GRAY = (128, 128, 128)

# For your maze
WALL_COLOR = BLACK
# WALL_COLOR = (43, 13, 13)
UNEXPLORED_COLOR = (115, 119, 255)  # Light blue
PATH_COLOR = (200, 200, 100)  # Light highlight
START_COLOR = RED
END_COLOR = GREEN
GRID_COLOR = (162, 208, 224)


YELLOW_GREEN = (173, 255, 47)
FOCUS_COLOR = YELLOW_GREEN
BUTTON_COLORS = {
    "normal": GRAY,
    "hover": DARK_GRAY,
    "text": BLUE,
    "hove_text": WHITE,
}