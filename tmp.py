from utils.util import demo
from termcolor import cprint


def print_2d_array(array):
  for row in array:
    for element in row:
      print("{:3}".format(element), end=" ")  # Adjust the width as needed
    print()


def ex1():
  # row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
  # print('|'.join(row))

  arr = [f'{i}' for i in range(9)]
  print(arr)

  arr2 = [[f'{i+3*j}' for i in range(3)] for j in range(3)]

  # for i in range(0, 9, 3):
  #   print(i, end=' ')
  #   print()
  # print(arr2)

  print(f'{arr2}')

  for row in arr2:
    print(row)

  print()
  print_2d_array(arr2)


demo(ex1, "Array")


def board():
  board = [' ' for _ in range(9)]

  line = f" X | {board[1]} | {board[2]} "
  cprint(line, 'red', 'on_white', attrs=["bold"])
  cprint("---+---+---", 'black', 'on_white')
  line = f" {board[3]} | O | {board[5]} "
  cprint(line, 'red', 'on_white')
  cprint("---+---+---", 'black', 'on_white')
  line = f" {board[6]} | {board[7]} | {board[8]} "
  cprint(line, 'red', 'on_white')


demo(board, "Board")


def board2d():
  board = [[' ' for _ in range(3)] for _ in range(3)]

  i = 1
  for row in board:
    # print("{:>3}".format("|").join(row))
    # items = list(map(lambda x: "{:^3}".format(x), row))
    print("|".join(list(map(lambda x: "{:^3}".format(x), row)) ))
    print(("-" if i < 3 else "") * 11)
    i += 1


demo(board2d, "Board with 2D Array")


def board2dClr():
  board = [[' ' for _ in range(3)] for _ in range(3)]

  i = 1
  for row in board:
    # line = "{:>3}".format("|").join(row)
    line = "|".join(list(map(lambda x: "{:^3}".format(x), row)) )
    cprint(line, 'red', 'on_white')
    line = ("-" if i < 3 else "") * 11
    cprint(line, 'black', 'on_white')
    i += 1


demo(board2dClr, "Color Board with 2D Array")


board = [' ' for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-"*9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-"*9)
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
board[0] = 'X'
board[2] = 'O'
board[5] = 'X'
board[7] = 'X'
board[8] = 'O'

display_board(board)