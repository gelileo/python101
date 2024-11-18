
# - first available
# - random move
# - center move
# - corner move
# - edge move
# - winning move
# - blocking moving

import random
def computer_move(board):
  if not center_move(board):
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


def is_available(board, row, col):
  return board[row][col] == ""