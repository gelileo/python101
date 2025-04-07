# Completed code for Lesson 11
# This code includes the final presentation with a showcase of features.

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from bfs import bfs
from maze_data import MAZE1, START_POSITION, END_POSITION

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Final Presentation")

# Showcase function
def showcase():
    print("Showcasing BFS Algorithm...")
    path = bfs(MAZE1, START_POSITION, END_POSITION)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

# Main function
def main():
    showcase()

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