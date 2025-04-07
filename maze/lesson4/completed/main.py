# Completed code for Lesson 4
# This code includes full argument parsing functionality.

import argparse
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze with Argument Parsing")

# Argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="Maze Project")
    parser.add_argument(
        "--mode", choices=["demo", "interactive"], default="demo", help="Choose the mode"
    )
    parser.add_argument(
        "--algo", choices=["bfs", "dfs"], default="bfs", help="Choose the algorithm for demo mode"
    )
    parser.add_argument(
        "--step_by_step", action="store_true", help="Run the demo one step at a time"
    )
    args = parser.parse_args()
    return args

# Main function
def main():
    args = parse_arguments()
    print(f"Running in {args.mode} mode with {args.algo} algorithm")
    if args.step_by_step:
        print("Step-by-step mode enabled")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()