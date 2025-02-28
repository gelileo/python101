# constants.py

PUZZLE_SIZE = 3  # 3x3 puzzle
EMPTY_TILE = 0  # We'll represent the blank as 0

INITIAL_DATA_FILE = "data.json"  # File to save the initial puzzle data
SOLUTION_STEPS_FILE = "solution_steps.json"  # File to save the solution steps

TILE_SIZE = 80  # Each tile is 80x80 px
TILE_MARGIN = 5  # Margin between tiles
FPS = 30  # Frames per second for the main loop
DEMO_FPS = 5  # Frames per second for the demo mode
# Pygame window dimensions and tile layout
WINDOW_WIDTH = TILE_SIZE * PUZZLE_SIZE + TILE_MARGIN * (PUZZLE_SIZE + 1)
WINDOW_HEIGHT = WINDOW_WIDTH
