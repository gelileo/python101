import pygame
import sys

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (64, 128, 255, 160)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200, 128)
DARK_GRAY = (128, 128, 128)

# Initialize Pygame
pygame.init()
pygame.font.init()  # Initialize the font module
clock = pygame.time.Clock()

status = "Player X's turn"
board = [["" for _ in range(3)] for _ in range(3)]

CELL_SIZE = 112
CELL_BORDER = 7
SCREEN_WIDTH = 350
SCREEN_HEIGHT = 350
SHAPE_MARGIN = 12
SHAPE_O_THICKNESS = 10
SHARP_O_RADIUS = CELL_SIZE // 2 - SHAPE_MARGIN
SHAPE_X_THICKNESS = 12

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))

def draw_pieces():
  pygame.draw.circle(
    screen,
    RED,
    (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
    SHARP_O_RADIUS,
    SHAPE_O_THICKNESS
  )

  # draw 'x'
  pygame.draw.line(
    screen, 
    BLACK,
    ( (SCREEN_WIDTH - CELL_SIZE) // 2 + SHAPE_MARGIN * 2, (SCREEN_HEIGHT -  CELL_SIZE) // 2 + SHAPE_MARGIN * 2),
    ( (SCREEN_WIDTH + CELL_SIZE) // 2 - SHAPE_MARGIN * 2, (SCREEN_HEIGHT +  CELL_SIZE) // 2 - SHAPE_MARGIN * 2),
    SHAPE_X_THICKNESS
  )

  pygame.draw.line(
    screen,
    BLACK,
    ( (SCREEN_WIDTH - CELL_SIZE) // 2 + SHAPE_MARGIN * 2, (SCREEN_HEIGHT +  CELL_SIZE) // 2 - SHAPE_MARGIN * 2),
    ( (SCREEN_WIDTH + CELL_SIZE) // 2 - SHAPE_MARGIN * 2, (SCREEN_HEIGHT -  CELL_SIZE) // 2 + SHAPE_MARGIN * 2),
    SHAPE_X_THICKNESS
    
  )

def draw_board():
  for row in range(3):
    for col in range(3):
      pygame.draw.rect(
        screen, 
        BLUE,
        (
          col * CELL_SIZE - (col * CELL_BORDER), 
          row * CELL_SIZE - (row * CELL_BORDER), 
          CELL_SIZE, 
          CELL_SIZE
        ),
        CELL_BORDER

      )
  

  draw_pieces()
  pass

def draw_status():
  print(status)
  pass

def draw_reset_button():
  pass

def redraw():
  # do the drawing here
  draw_board()
  draw_status()
  draw_reset_button()


running = True
game_over = False
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  
  redraw()
  pygame.display.flip()
  clock.tick(5)

# Quit Pygame
pygame.quit()
sys.exit()