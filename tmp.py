from util import demo
from termcolor import cprint


def ex1():
  row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
  print('|'.join(row))

  arr = [f'{i}' for i in range(9)]
  print(arr)

  # cprint('Hello World!', 'red','on_white')


  for i in range(0, 9, 3):
    print(i, end=' ')


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