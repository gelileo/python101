
# - first available
# - random move
# - center move
# - corner move
# - edge move
# - winning move
# - blocking moving
from game_logic import *

import random
def computer_move(board):
  if not winning_move(board):
    if not center_move(board):
      if not corner_move(board):
        random_move(board)
  
  


def random_move(board):
  while True:
    row = random.randint(0,2)
    col = random.randint(0,2)
    if board[row][col] == "":
      board[row][col] = "O"
      break

  
def first_awailable_move(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "":
        board[row][col] = "O"
        print(f"computer move: ({row}, {col})")
        return


def center_move(board):
  if is_available(board, 1,1):
    board[1][1] = "O"
    return True
  return False

def corner_move(board):
  all_corners = [(0,0),
                 (0,2),
                 (2,0),
                 (2,2)]
  for corner in all_corners:
    row = corner[0]
    col = corner[1]
    if is_available(board, row, col):
      board[row][col] = "O"
      return True
  return False

def is_available(board, row, col):
  return board[row][col] == ""


def board_copy(board):
  ret = [["" for _ in range(3)] for _ in range(3)]

  for row in range(3):
    for col in range(3):
      ret[row][col]= board[row][col]

  return ret

def winning_move(board):
  # loop through all the available
  # make tentative move
  # check for win
  for row in range(3):
    for col in range(3):
      tmp_board = board_copy(board)
      if is_available(board, row, col):
        tmp_board[row][col] = "O"
        if check_win(tmp_board, "O"):
          board[row][col] = "O"
          return True
  return False
        
        