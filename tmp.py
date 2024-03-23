import pygame
import sys

# Layout Constants
CELL_SIZE = 112
CELL_BORDER = 7
SHAPE_MARGIN = 26
SHAPE_X_WIDTH = 18
SHAPE_O_THICKNESS = 10
SHAPE_O_RADIUS = CELL_SIZE // 2 - SHAPE_MARGIN + 8
SCREEN_WIDTH = 350
SCREEN_HEIGHT = 350

# Colors
WHITE = (255, 255, 255)
BLUE = (64, 128, 255, 160)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)
DARK_GRAY = (128, 128, 128)

# Initialize Pygame
pygame.init()
pygame.font.init()  # Initialize the font module
status_font = pygame.font.SysFont("Arial", 15)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
# Define the game board
board = [["" for _ in range(3)] for _ in range(3)]
print(board)

def get_cell_position(mouse_pos):
  row = mouse_pos[1] // CELL_SIZE
  col = mouse_pos[0] // CELL_SIZE
  return row, col


def drawX(row, col):
  pygame.draw.line(
      screen,
      BLACK,
      (
          col * CELL_SIZE + SHAPE_MARGIN + (col * CELL_BORDER),
          row * CELL_SIZE + SHAPE_MARGIN + (row * CELL_BORDER),
      ),
      (
          col * CELL_SIZE + CELL_SIZE - SHAPE_MARGIN + (col * CELL_BORDER),
          row * CELL_SIZE + CELL_SIZE - SHAPE_MARGIN + (row * CELL_BORDER),
      ),
    SHAPE_X_WIDTH,
  )
  pygame.draw.line(
      screen,
      BLACK,
      (
          col * CELL_SIZE + CELL_SIZE - SHAPE_MARGIN + (col * CELL_BORDER),
          row * CELL_SIZE + SHAPE_MARGIN + (row * CELL_BORDER),
      ),
      (
          col * CELL_SIZE + SHAPE_MARGIN + (col * CELL_BORDER),
          row * CELL_SIZE + CELL_SIZE - SHAPE_MARGIN + (row * CELL_BORDER),
      ),
    SHAPE_X_WIDTH,
  )
def draw_board():
  pygame.draw.rect(
      screen,
      BLUE,
      (
        (SCREEN_WIDTH - CELL_SIZE) // 2,
        (SCREEN_HEIGHT - CELL_SIZE) // 2,
        CELL_SIZE,
        CELL_SIZE,
      ),
      CELL_BORDER,
      border_radius=5,
  )

  pygame.draw.circle(
    screen,
    "red",
    (
      (SCREEN_WIDTH) // 2,
      (SCREEN_HEIGHT) // 2,
    ),
    SHAPE_O_RADIUS,
    SHAPE_O_THICKNESS,
  )
  drawX(1,1)

  x_font = pygame.font.SysFont("Arial", 90)
  text_surface = x_font.render('X', True, BLACK)
  screen.blit(
      text_surface,
      (
          (15,
          15),
      ),
  )
  
def redraw():
  draw_board()

screen.fill(WHITE)
draw_board()
pygame.display.flip()
running = True
game_over = False
clock = pygame.time.Clock()
# Main loop
while running:
  mouse_pos = pygame.mouse.get_pos()  # Get mouse 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        row, col = get_cell_position(mouse_pos)
        print("Clicked cell:", row, col)

  redraw()
  pygame.display.flip()
  clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()