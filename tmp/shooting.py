import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
TARGET_WIDTH, TARGET_HEIGHT = 20, 20
PLAYER_SPEED = 4
BULLET_SPEED = 7
TARGET_SPEED = 2
MAX_TARGETS = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooting Game")

# Load player image (triangle)
player = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT), pygame.SRCALPHA)
pygame.draw.polygon(
    player,
    RED,
    [(PLAYER_WIDTH // 2, 0), (0, PLAYER_HEIGHT), (PLAYER_WIDTH, PLAYER_HEIGHT)],
)
player_rect = player.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

# Create bullets and targets
bullets = []
targets = [
    pygame.Rect(
        random.randint(0, WIDTH - TARGET_WIDTH),
        -TARGET_HEIGHT,
        TARGET_WIDTH,
        TARGET_HEIGHT,
    )
    for _ in range(MAX_TARGETS)
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

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(
            player_rect.centerx - BULLET_WIDTH // 2,
            player_rect.top,
            BULLET_WIDTH,
            BULLET_HEIGHT,
        )
        bullets.append(bullet)

    # Move and update bullets
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    for bullet in bullets:
        bullet.y -= BULLET_SPEED

    # Move and update targets
    for target in targets:
        target.y += TARGET_SPEED
        if target.y > HEIGHT:
            target.y = 0
            target.x = random.randint(0, WIDTH - TARGET_WIDTH)

    # Check for collisions between bullets and targets
    for bullet in bullets:
        for target in targets:
            if bullet.colliderect(target):
                score += 1
                targets.remove(target)
                target.y = -TARGET_HEIGHT
                target.x = random.randint(0, WIDTH - TARGET_WIDTH)

    # Clear the screen
    window.fill(WHITE)

    # Draw player, bullets, and targets
    window.blit(player, player_rect)
    for bullet in bullets:
        pygame.draw.rect(window, RED, bullet)
    for target in targets:
        pygame.draw.rect(window, RED, target)

    # Display score
    score_text = font.render(f"Score: {score}", True, RED)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control frame rate
    clock.tick(60)


ending_text = font.render("Insert Coins To Continue", True, RED)
window.blit(ending_text, (20, 200))
pygame.display.update()
# Quit the game
pygame.quit()
