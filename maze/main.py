# main.py

import pygame
import sys
import argparse
import json
from typing import Dict, Tuple
from constants import CELL_SIZE, FPS
from colors import WALL_COLOR, UNEXPLORED_COLOR, PATH_COLOR, START_COLOR, END_COLOR, GRID_COLOR
from maze_data import MAZE1, START_POSITION, END_POSITION
from algorithms.bfs import bfs
from algorithms.dfs import dfs

def load_config(file_name="config.json"):
    """Load configuration settings from a JSON file."""
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading configuration: {e}")
        return {}

# Load configuration at the start of the program
config = load_config()
CELL_SIZE = config.get("cell_size", CELL_SIZE) * 2
FPS = config.get("fps", FPS)

# Load NUM_ROWS and NUM_COLS dynamically from the configuration file
NUM_ROWS = config.get("num_rows", 7)  # Default to 7 if not specified
NUM_COLS = config.get("num_cols", 12)  # Default to 12 if not specified

# Calculate SCREEN_WIDTH and SCREEN_HEIGHT dynamically
SCREEN_WIDTH = NUM_COLS * CELL_SIZE
SCREEN_HEIGHT = NUM_ROWS * CELL_SIZE

def draw_grid(screen):
    rows = len(MAZE1)
    cols = len(MAZE1[0])
    for r in range(rows):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, r * CELL_SIZE),
            (cols * CELL_SIZE, r * CELL_SIZE),
        )
    
    for c in range(cols):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (c * CELL_SIZE, 0),
            (c * CELL_SIZE, rows * CELL_SIZE),
        )


def draw_maze(
    screen,
    maze,
    visited_with_steps: Dict[Tuple[int, int], int] | None = None,
    path=None,
):
    """
    Draw the maze, highlighting visited cells, step numbers,
    and optionally the final path. Also label start/end squares.
    """
    font = pygame.font.SysFont(None, 20)  # Font for step labels

    rows = len(maze)
    cols = len(maze[0])

    # 1) Draw the base maze
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if maze[r][c] == 1:
                color = WALL_COLOR
            else:
                color = UNEXPLORED_COLOR
            pygame.draw.rect(screen, color, rect)

    # 2) Highlight visited squares & draw their step number
    if visited_with_steps:
        for (vr, vc), step_num in visited_with_steps.items():
            rect = pygame.Rect(vc * CELL_SIZE, vr * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, PATH_COLOR, rect)

            # Draw the step number in the center
            step_text = font.render(str(step_num), True, (0, 0, 0))  # black text
            text_rect = step_text.get_rect(center=rect.center)
            screen.blit(step_text, text_rect)

    # 3) Draw the final path (if provided)
    if path:
        for pr, pc in path:
            rect = pygame.Rect(pc * CELL_SIZE, pr * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (255, 165, 0), rect)  # orange for final path

    # 4) Label the start and end squares with "A" and "B"
    #    (on top of whatever color they currently have)
    start_r, start_c = START_POSITION
    start_rect = pygame.Rect(
        start_c * CELL_SIZE, start_r * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, START_COLOR, start_rect)
    start_text = font.render("A", True, (255, 255, 255))  # white text
    start_text_rect = start_text.get_rect(center=start_rect.center)
    screen.blit(start_text, start_text_rect)

    end_r, end_c = END_POSITION
    end_rect = pygame.Rect(end_c * CELL_SIZE, end_r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, END_COLOR, end_rect)
    end_text = font.render("B", True, (255, 255, 255))  # white text
    end_text_rect = end_text.get_rect(center=end_rect.center)
    screen.blit(end_text, end_text_rect)

    ## Draw grid lines, optional
    # draw_grid(screen)


def run_demo(
    screen: pygame.Surface, clock: pygame.time.Clock, algorithm: str = "bfs"
) -> None:
    """
    Demonstrate the selected algorithm by showing the exploration and final path.
    Once the demo completes, it will automatically restart.
    """
    # Compute the visited order and final path once (assuming a static maze)
    if algorithm == "bfs":
        order_visited, path = bfs(MAZE1, START_POSITION, END_POSITION)
    else:
        order_visited, path = dfs(MAZE1, START_POSITION, END_POSITION)

    current_step = 0
    running = True

    while running:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # You could allow key presses to speed up or reset, if desired.
                pass

        # When demo completes, show the final state, wait, then restart.
        if current_step >= len(order_visited):
            # Build visited_with_steps for the complete run
            visited_with_steps = {cell: i for i, cell in enumerate(order_visited)}
            screen.fill((0, 0, 0))
            # Optionally, you can pass `path` here to highlight the final path.
            draw_maze(screen, MAZE1, visited_with_steps, path=path)
            pygame.display.flip()
            # Wait 2 seconds before restarting the demo.
            pygame.time.wait(2000)
            # Reset the demo progress
            current_step = 0
            continue

        # Show the portion of the visited order up to the current step.
        visited_up_to_now = order_visited[:current_step]
        visited_with_steps = {}
        for i, cell in enumerate(visited_up_to_now):
            visited_with_steps[cell] = i  # Step numbers starting from 0

        screen.fill((0, 0, 0))
        draw_maze(screen, MAZE1, visited_with_steps, path=None)
        pygame.display.flip()

        current_step += 1

    return


def draw_labels(screen, visited_with_steps):
    """
    Redraws the labels (visited step numbers, and "A"/"B" for start/end)
    on top of everything else.
    """
    font = pygame.font.SysFont(None, 20)

    # Redraw step numbers for each visited cell.
    for (vr, vc), step_num in visited_with_steps.items():
        rect = pygame.Rect(vc * CELL_SIZE, vr * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        step_text = font.render(
            str(step_num), True, (0, 0, 0)
        )  # black text for numbers
        text_rect = step_text.get_rect(center=rect.center)
        screen.blit(step_text, text_rect)

    # Redraw start label "A"
    start_r, start_c = START_POSITION
    start_rect = pygame.Rect(
        start_c * CELL_SIZE, start_r * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    start_text = font.render("A", True, (255, 255, 255))  # white text for clarity
    start_text_rect = start_text.get_rect(center=start_rect.center)
    screen.blit(start_text, start_text_rect)

    # Redraw end label "B"
    end_r, end_c = END_POSITION
    end_rect = pygame.Rect(end_c * CELL_SIZE, end_r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    end_text = font.render("B", True, (255, 255, 255))
    end_text_rect = end_text.get_rect(center=end_rect.center)
    screen.blit(end_text, end_text_rect)


def run_demo_step_by_step(screen, clock, algorithm="bfs"):
    """
    Step-by-step mode:
      - SPACE to move forward one step
      - SHIFT to move backward one step
      - Show step numbers in each visited cell
      - Label start with 'A' and end with 'B'
    """
    # 1) Get visited order + path from BFS or DFS
    if algorithm == "bfs":
        order_visited, path = bfs(MAZE1, START_POSITION, END_POSITION)
    else:
        order_visited, path = dfs(MAZE1, START_POSITION, END_POSITION)

    step_index = 0
    show_final_path = False
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Press ESC to quit
                if event.key == pygame.K_ESCAPE:
                    running = False

                # SPACE to move forward
                elif event.key == pygame.K_SPACE:
                    # If we haven't visited all cells yet, move forward
                    if step_index < len(order_visited):
                        step_index += 1
                    else:
                        # Once we've shown all visited cells, show final path
                        show_final_path = True

                # SHIFT to move backward
                elif event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                    if step_index > 0:
                        step_index -= 1
                    # Hide final path if we move backward
                    if step_index < len(order_visited):
                        show_final_path = False

        # 2) Build a map of the visited cells and their step numbers
        #    up to the current step_index
        visited_up_to_now = order_visited[:step_index]
        visited_with_steps = {}
        for i, cell in enumerate(visited_up_to_now):
            # visited_with_steps[cell] = i + 1  # step numbers start at 1
            visited_with_steps[cell] = i  # skip the starting cell

        # 3) Draw the maze
        screen.fill((0, 0, 0))  # clear background
        if show_final_path:
            # Show final path if we've completed all steps
            draw_maze(screen, MAZE1, visited_with_steps, path)
        else:
            # Just show visited squares so far
            draw_maze(screen, MAZE1, visited_with_steps, None)

        pygame.display.flip()

    return


def run_interactive(screen, clock):
    """
    Interactive mode:
      - The player moves with arrow keys.
      - Each visited cell is labeled with its step number (using visited_with_steps).
      - The player's continuous route is recorded in path_taken.
      - The starting square is labeled "A" and the ending square "B".
      - When the player reaches END_POSITION, the route is highlighted
        (instead of quitting).
    """
    # Start at the defined starting position.
    player_pos = list(START_POSITION)

    # Use a dictionary to map visited cell coordinates to their step numbers.
    # The first visited cell (start) is step 1.
    visited_with_steps = {tuple(player_pos): 1}

    # Record the player's actual route (for the final highlighted path).
    path_taken = [tuple(player_pos)]

    show_final_path = False
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                new_pos = player_pos[:]
                if event.key == pygame.K_UP:
                    new_pos[0] -= 1
                elif event.key == pygame.K_DOWN:
                    new_pos[0] += 1
                elif event.key == pygame.K_LEFT:
                    new_pos[1] -= 1
                elif event.key == pygame.K_RIGHT:
                    new_pos[1] += 1
                elif event.key == pygame.K_ESCAPE:
                    running = False

                # Check that the new position is within bounds and not a wall.
                r, c = new_pos
                if (
                    0 <= r < len(MAZE1)
                    and 0 <= c < len(MAZE1[0])
                    and MAZE1[r][c] == 0
                ):

                    # If the new position is the same as the cell before the current one,
                    # assume it's a backtracking move and update path_taken accordingly.
                    if len(path_taken) >= 2 and tuple(new_pos) == path_taken[-2]:
                        path_taken.pop()  # remove the last cell since we're going back
                        player_pos = new_pos
                    else:
                        # Otherwise, move forward and record the new cell.
                        player_pos = new_pos
                        path_taken.append(tuple(new_pos))

                    # If this cell was never visited before, record its step number.
                    if tuple(player_pos) not in visited_with_steps:
                        visited_with_steps[tuple(player_pos)] = (
                            len(visited_with_steps)
                        )

                # End the interactive mode if the player reaches the END_POSITION.
                if tuple(player_pos) == END_POSITION:
                    show_final_path = True

        # Clear the screen.
        screen.fill((0, 0, 0))

        # Draw the maze with visited cells labeled.
        # (The draw_maze function should display the step numbers for each visited cell.)
        if show_final_path:
            draw_maze(screen, MAZE1, visited_with_steps, path_taken)
        else:
            draw_maze(screen, MAZE1, visited_with_steps, path=None)

        # Draw the player (a highlighted rectangle) on top of the maze.
        player_rect = pygame.Rect(
            player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(screen, (0, 200, 200), player_rect)
        # Redraw the labels on top of the player, so they remain visible.
        draw_labels(screen, visited_with_steps)
        pygame.display.flip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["demo", "interactive"],
        default="demo",
        help="Choose the mode: demo or interactive",
    )
    parser.add_argument(
        "--algo",
        choices=["bfs", "dfs"],
        default="bfs",
        help="Choose the algorithm for demo mode",
    )

    parser.add_argument(
        "--step_by_step",
        action="store_true",
        help="If set, run the demo one step at a time",
    )
    args = parser.parse_args()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Search Demo")
    clock = pygame.time.Clock()

    if args.mode == "demo":
        if args.step_by_step:
            run_demo_step_by_step(screen, clock, algorithm=args.algo)
        else:
            run_demo(screen, clock, algorithm=args.algo)
    else:
        run_interactive(screen, clock)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
