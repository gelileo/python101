# Starter code for Lesson 11
# This code provides the basic structure for the final presentation.

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Final Presentation")

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