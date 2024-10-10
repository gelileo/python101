import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fibonacci Flower Petal Simulator")

# Colors
WHITE = (255, 255, 255)
PURPLE = (138, 43, 226)
BLACK = (0, 0, 0)

# Font settings for the label
font = pygame.font.SysFont("Arial", 30)


# Function to generate Fibonacci numbers up to a limit
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


# Function to draw the flower with Fibonacci petals and dynamic line width
def draw_flower(petals):
    screen.fill(WHITE)
    center = (width // 2, height // 2)

    # Dynamic line width calculation: thinner lines with more petals
    line_width = max(
        1, 10 - petals // 5
    )  # Adjust line width between 1 and 10 based on petal count

    for i in range(petals):
        angle = i * (2 * math.pi / petals)
        radius = 10 * math.sqrt(i + 1)  # Petal radius grows with sqrt of index
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))

        # Draw each petal as a circle with dynamic line width
        pygame.draw.circle(screen, PURPLE, (x, y), 20, line_width)

    # Create label text to show the number of petals
    label = font.render(f"Number of Petals: {petals}", True, BLACK)
    screen.blit(
        label, (width // 2 - label.get_width() // 2, 10)
    )  # Center label at the top

    pygame.display.flip()


# Main loop
def main():
    running = True
    petals = fibonacci(10)[-1]  # Default Fibonacci number of petals (you can adjust)
    draw_flower(petals)

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Increase the Fibonacci index
                    petals = fibonacci(petals + 1)[-1]
                    draw_flower(petals)
                elif event.key == pygame.K_DOWN:  # Decrease the Fibonacci index
                    petals = max(
                        3, fibonacci(petals - 1)[-1]
                    )  # Ensure a minimum of 3 petals
                    draw_flower(petals)
        clock.tick(30)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
