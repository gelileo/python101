# Starter code for Lesson 4
# This code provides the basic structure for argument parsing without full functionality.

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
    args = parser.parse_args()
    return args

# Main function
def main():
    args = parse_arguments()
    print(f"Running in {args.mode} mode")

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