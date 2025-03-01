#!/usr/bin/env python3

"""
sliding_puzzle.py

Usage:
  python sliding_puzzle.py game
    - Starts a random puzzle and allows manual play with arrow keys.
    - Saves the initial puzzle data in data.json (or the file specified in constants).

  python sliding_puzzle.py solve <data_file.json>
    - Loads puzzle from JSON, runs IDA* to find solution, replays it automatically.
    - Saves solution steps in solution_steps.json (or the file specified in constants).
"""

import sys
import json
import random
import pygame
import time
from copy import deepcopy

import constants
import colors

################################################################################
# Puzzle Logic
################################################################################


def generate_solvable_puzzle(size=constants.PUZZLE_SIZE):
    """Generate a random solvable puzzle of given size (4x4 by default)."""
    puzzle = list(range(size * size))  # [0..15] for a 4x4
    while True:
        random.shuffle(puzzle)
        if is_solvable(puzzle, size):
            return puzzle


def is_solvable(puzzle, size):
    """
    Check if puzzle is solvable.
    For a 4x4 puzzle:
      - If grid width is even, puzzle is solvable if:
        (Number of inversions + row of blank from the bottom) is odd.
    """
    inversions = 0
    blank_row = 0
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            blank_row = i // size  # 0-based
            continue
        for j in range(i + 1, len(puzzle)):
            if puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1

    # row_from_bottom = size - blank_row
    row_from_bottom = size - blank_row
    return (inversions + row_from_bottom) % 2 == 1


def is_solved(puzzle):
    """Check if puzzle is in goal state: [1,2,3,...,15,0]."""
    goal = list(range(1, len(puzzle))) + [0]
    return puzzle == goal


def find_blank(puzzle, size):
    """Return (row, col) of the blank (0) in the puzzle list."""
    index = puzzle.index(0)
    return (index // size, index % size)


def move_blank(puzzle, direction, size):
    """
    Move the blank tile up/down/left/right if possible.
    Returns a new puzzle list if move is valid, else None.
    """
    puzzle_copy = puzzle[:]
    r, c = find_blank(puzzle_copy, size)
    blank_index = r * size + c

    if direction == "up" and r > 0:
        swap_index = (r - 1) * size + c
    elif direction == "down" and r < size - 1:
        swap_index = (r + 1) * size + c
    elif direction == "left" and c > 0:
        swap_index = r * size + (c - 1)
    elif direction == "right" and c < size - 1:
        swap_index = r * size + (c + 1)
    else:
        return None  # invalid move

    puzzle_copy[blank_index], puzzle_copy[swap_index] = (
        puzzle_copy[swap_index],
        puzzle_copy[blank_index],
    )
    return puzzle_copy


def get_neighbors(puzzle, size):
    """Return list of (new_puzzle, move) for each valid neighbor."""
    neighbors = []
    for direction in ["up", "down", "left", "right"]:
        new_p = move_blank(puzzle, direction, size)
        if new_p is not None:
            neighbors.append((new_p, direction))
    return neighbors


################################################################################
# IDA* Search for Puzzle Solution
################################################################################


def manhattan_distance(puzzle, size):
    """Heuristic: sum of Manhattan distances of each tile from its goal position."""
    distance = 0
    for index, tile in enumerate(puzzle):
        if tile == 0:
            continue
        goal_row = (tile - 1) // size
        goal_col = (tile - 1) % size
        row = index // size
        col = index % size
        distance += abs(row - goal_row) + abs(col - goal_col)
    return distance


def ida_star_search(initial, size):
    """
    Perform IDA* search to find a solution (list of moves).
    Returns [] if no solution found.
    """
    start = tuple(initial)
    bound = manhattan_distance(start, size)
    path = [start]
    moves_path = []

    while True:
        t = search(path, moves_path, 0, bound, size)
        if t == True:
            return moves_path
        if t == float("inf"):
            return []
        bound = t


def search(path, moves_path, g, bound, size):
    current = path[-1]
    f = g + manhattan_distance(current, size)
    if f > bound:
        return f
    if is_solved(list(current)):
        return True

    min_cost = float("inf")
    for nbr, move in get_neighbors(list(current), size):
        nbr_tup = tuple(nbr)
        if nbr_tup in path:
            continue
        path.append(nbr_tup)
        moves_path.append(move)
        t = search(path, moves_path, g + 1, bound, size)
        if t == True:
            return True
        if t < min_cost:
            min_cost = t
        path.pop()
        moves_path.pop()
    return min_cost


################################################################################
# Data Persistence
################################################################################


def save_puzzle_data(puzzle, filename=constants.INITIAL_DATA_FILE):
    """Save puzzle data to JSON."""
    data = {"puzzle": puzzle}
    with open(filename, "w") as f:
        json.dump(data, f)


def load_puzzle_data(filename):
    """Load puzzle data from JSON."""
    with open(filename, "r") as f:
        data = json.load(f)
    return data["puzzle"]


def save_solution_steps(steps, filename=constants.SOLUTION_STEPS_FILE):
    """Save solution steps (list of moves) to JSON."""
    data = {"moves": steps}
    with open(filename, "w") as f:
        json.dump(data, f)


################################################################################
# Pygame Rendering and Main Loops
################################################################################


def draw_puzzle(screen, puzzle, highlight=False):
    """
    Draw the 4x4 puzzle in the pygame window.
    If highlight=True, color the background or tile to show a winning state.
    """
    screen.fill(colors.BLACK)
    font = pygame.font.SysFont(None, 40)  # Basic font, size 40

    size = constants.PUZZLE_SIZE
    for i in range(size):
        for j in range(size):
            tile = puzzle[i * size + j]
            x = (
                j * (constants.TILE_SIZE + constants.TILE_MARGIN)
                + constants.TILE_MARGIN
            )
            y = (
                i * (constants.TILE_SIZE + constants.TILE_MARGIN)
                + constants.TILE_MARGIN
            )

            rect = pygame.Rect(x, y, constants.TILE_SIZE, constants.TILE_SIZE)
            if tile == 0:
                # Blank tile
                pygame.draw.rect(screen, colors.GRAY, rect)
            else:
                if highlight:
                    # If highlighting, draw a special color background
                    pygame.draw.rect(screen, colors.HIGHLIGHT, rect)
                else:
                    pygame.draw.rect(screen, colors.BLUE, rect)

                # Render the tile number
                text_surf = font.render(str(tile), True, colors.WHITE)
                text_rect = text_surf.get_rect(center=rect.center)
                screen.blit(text_surf, text_rect)

    pygame.display.flip()


def run_game(puzzle):
    """
    Run the puzzle in 'game' mode (manual play with arrow keys).
    """
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Sliding Puzzle - Game Mode")
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(constants.FPS)

        if is_solved(puzzle):
            # Highlight the final state
            draw_puzzle(screen, puzzle, highlight=True)
            # Show a quick message or wait a bit
            time.sleep(1.0)
            running = False
            break

        draw_puzzle(screen, puzzle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    new_p = move_blank(puzzle, "up", constants.PUZZLE_SIZE)
                    if new_p:
                        puzzle = new_p
                elif event.key == pygame.K_DOWN:
                    new_p = move_blank(puzzle, "down", constants.PUZZLE_SIZE)
                    if new_p:
                        puzzle = new_p
                elif event.key == pygame.K_LEFT:
                    new_p = move_blank(puzzle, "left", constants.PUZZLE_SIZE)
                    if new_p:
                        puzzle = new_p
                elif event.key == pygame.K_RIGHT:
                    new_p = move_blank(puzzle, "right", constants.PUZZLE_SIZE)
                    if new_p:
                        puzzle = new_p

    pygame.quit()


def run_solve(initial_puzzle, steps):
    """
    Run the puzzle in 'solve' mode (automatically replay the solution steps repeatedly).
    The replay continues until the user quits (closes the window or presses any key).
    """
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    pygame.display.set_caption("Sliding Puzzle - Solve Mode")
    clock = pygame.time.Clock()

    running = True
    # Save the initial state to restart each replay cycle
    while running:
        # Start from the initial puzzle each time
        puzzle = initial_puzzle[:]

        # Replay each move in the solution steps
        for move in steps:
            clock.tick(constants.FPS)
            # Check for quit events during replay
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    running = False
                    break
            if not running:
                break

            puzzle = move_blank(puzzle, move, constants.PUZZLE_SIZE)
            draw_puzzle(screen, puzzle)
            pygame.time.wait(600)

        if not running:
            break

        # After finishing the replay, highlight the solved state if achieved
        if is_solved(puzzle):
            draw_puzzle(screen, puzzle, highlight=True)
        # Pause briefly before restarting the replay cycle
        pygame.time.wait(1000)

        # Check again for any quit events during the pause
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

    pygame.quit()


################################################################################
# Main
################################################################################


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python sliding_puzzle.py game")
        print("  python sliding_puzzle.py solve <data_file.json>")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "game":
        # Generate a random solvable puzzle
        if len(sys.argv) < 3:
            puzzle = generate_solvable_puzzle()
            # Save to file
            save_puzzle_data(puzzle, constants.INITIAL_DATA_FILE)
            print(f"Puzzle generated and saved to {constants.INITIAL_DATA_FILE}")
            run_game(puzzle)
        else:
            data_file = sys.argv[2]
            puzzle = load_puzzle_data(data_file)
            run_game(puzzle)
    elif mode == "solve":
        if len(sys.argv) < 3:
            print("Usage: python sliding_puzzle.py solve <data_file.json>")
            sys.exit(1)
        data_file = sys.argv[2]
        puzzle = load_puzzle_data(data_file)
        print("Solving puzzle... (this may take a while for certain configurations)")

        steps = ida_star_search(puzzle, constants.PUZZLE_SIZE)
        if not steps:
            print("No solution found or puzzle is already solved.")
            steps = []

        save_solution_steps(steps, constants.SOLUTION_STEPS_FILE)
        print(f"Solution steps saved to {constants.SOLUTION_STEPS_FILE}")

        run_solve(puzzle, steps)

    else:
        print(f"Unknown mode: {mode}")


if __name__ == "__main__":
    main()
