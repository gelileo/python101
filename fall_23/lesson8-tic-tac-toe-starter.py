
board = [' ' for _ in range(9)]

#  X | O | X
# ----------
#  O | X | O
# ----------
#  X | O | X

def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print('-'*9)
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print('-'*9)
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])
  print()

# board[1] = 'O'
# board[4] = 'O'
# board[7] = 'O'
# display_board()

def make_a_move(current_player: str):
  move = int(input(f'Player {current_player} make a move(1-9):'))
  board[move-1] = current_player

def check_winner():
  print("to be implemented")
  # if board[0] == current_player and board[1] == current_player and board[2] == current_player:
  return False

def check_draw():
  print("to be implemented")
  return True

def switch_player():
  if current_player == 'X':
    current_player = 'O'
  else:
    current_player = 'X'
# current_player = 'O' if current_player == 'X' else 'X'
  
current_player = 'X'
while True:
  display_board()
  make_a_move(current_player)
  if check_winner():
    print("Winner is Player: " + current_player)
    break
  elif check_draw():
    print("It's a draw!")
    break
  else:
    switch_player()
  


# ask player X to make a move
# display_board()
# Whether game over
#   sb. get 3 in a row
#   or board is full 
# If true: display player [] wins!!
# If False:
# ask player O to make a move
# Go back to line 24
# display_board()
# Whether game over
#   sb. get 3 in a row
#   or board is full 
# If true: display player [] wins!! 
#   It's a draw
# If False:
# repeat



