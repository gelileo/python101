# Completed code for Lesson 10
# This code includes testing and debugging features.

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from bfs import bfs
from maze_data import MAZE1, START_POSITION, END_POSITION

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Testing and Debugging")

# Test BFS function
def test_bfs():
    path = bfs(MAZE1, START_POSITION, END_POSITION)
    if path:
        print("BFS Test Passed: Path found.")
    else:
        print("BFS Test Failed: No path found.")

# Main function
def main():
    test_bfs()

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