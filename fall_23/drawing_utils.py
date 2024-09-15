from colors import *
from layouts import *

def draw_O(row, col):
  pygame.draw.circle(
    screen,
    RED,
    # (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
    ((col * CELL_SIZE + CELL_SIZE // 2 - CELL_BORDER * col ),  
     (row * CELL_SIZE + CELL_SIZE // 2 - CELL_BORDER * row )),
    SHARP_O_RADIUS,
    SHAPE_O_THICKNESS
  )

def draw_X(row, col):
  # draw 'x'
  x1 = col * CELL_SIZE + SHAPE_MARGIN - CELL_BORDER * col
  y1 = row * CELL_SIZE + SHAPE_MARGIN - CELL_BORDER * row
  x2 = (col + 1) * CELL_SIZE - SHAPE_MARGIN - (col + 1) * CELL_BORDER
  y2 = (row + 1) * CELL_SIZE - SHAPE_MARGIN - (row + 1) * CELL_BORDER
  pygame.draw.line(
    screen, 
    BLACK,
    (x1, y1),
    (x2, y2),
    SHAPE_X_THICKNESS
  )
  
  pygame.draw.line(
    screen,
    BLACK,
    (x1, y2),
    (x2, y1),
    SHAPE_X_THICKNESS
  )


def draw_pieces(board, row, col):
  # print(f"drawing pieces at {row}, {col}")
  if board[row][col] == 'O':
    draw_O(row, col)
  elif board[row][col] == 'X':
    draw_X(row, col)
  return