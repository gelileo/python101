# Starter code for Lesson 10
# This code provides the basic structure for testing and debugging.

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Testing and Debugging")

# Main function
def main():
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