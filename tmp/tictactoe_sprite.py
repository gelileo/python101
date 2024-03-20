import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TIC TAC TOE")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the game board
board = [["" for _ in range(3)] for _ in range(3)]

# Cell properties
cell_size = 200
cell_padding = 10


# Sprite classes
class XSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        pygame.draw.line(
            self.image, BLACK, (50, 50), (cell_size - 50, cell_size - 50), 25
        )
        pygame.draw.line(
            self.image, BLACK, (cell_size - 50, 50), (50, cell_size - 50), 25
        )
        self.rect = self.image.get_rect(topleft=position)


class OSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image, BLACK, (cell_size // 2, cell_size // 2), cell_size // 2 - 50, 25
        )
        self.rect = self.image.get_rect(topleft=position)


# Function to add a shape sprite to the board
def add_shape_sprite(row, col, shape):
    x, y = col * cell_size, row * cell_size
    if shape == "X":
        sprite = XSprite((x, y))
    else:
        sprite = OSprite((x, y))
    shape_sprites.add(sprite)


# Main game loop setup
shape_sprites = pygame.sprite.Group()
current_player = "X"
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // cell_size, x // cell_size
            if board[row][col] == "":
                board[row][col] = current_player
                add_shape_sprite(row, col, current_player)
                current_player = "O" if current_player == "X" else "X"

    screen.fill(WHITE)
    shape_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
