import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBJECT_WIDTH, OBJECT_HEIGHT = 20, 20
PLAYER_SPEED = 5
OBJECT_SPEED = 2
OBJECT_COUNT = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Load player image
player = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player.fill(RED)
player_rect = player.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

# Create falling objects
objects = [
    pygame.Rect(random.randint(0, WIDTH - OBJECT_WIDTH), 0, OBJECT_WIDTH, OBJECT_HEIGHT)
    for _ in range(OBJECT_COUNT)
]

# Initialize game variables
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    # Move and update objects
    for obj in objects:
        obj.y += OBJECT_SPEED
        if obj.y > HEIGHT:
            obj.y = 0
            obj.x = random.randint(0, WIDTH - OBJECT_WIDTH)

        # Check for collision with player
        if obj.colliderect(player_rect):
            score += 1
            obj.y = 0
            obj.x = random.randint(0, WIDTH - OBJECT_WIDTH)

    # Clear the screen
    window.fill(WHITE)

    # Draw player and objects
    window.blit(player, player_rect)
    for obj in objects:
        pygame.draw.rect(window, RED, obj)

    # Display score
    score_text = font.render(f"Score: {score}", True, RED)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
