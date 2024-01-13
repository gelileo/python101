
# board = [1,2,3,4,5,6,7,8,9]


# board2d = [[1,2,3],
#            [4,5,6],
#            [7,8,9]]

# print(board2d)

# print(board2d[0][0])
# print(board2d[1][1])
# print(board2d[2][2])

# board2d[1][0] = 'X'
# print(board2d)


#  X | O | X
# ----------
#  O | X | O
# ----------
#  X | O | X

#make board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


def printBoard(board):
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print('-' * 9)
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print('-' * 9)
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])


#take player input
def playerInput(board):
  while True:
    try:
      inp = int(input(f"Player {currentPlayer}, Enter a number 1-9: "))
      if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
        break
      else:
        print("Invalid Move, Try again")
    except ValueError:
      print("Invalid input. Please enter a number.")


#Check for win or tie
#HORiZONTAL
def check_H(board):
  global winner
  if board[0] == board[1] == board[2] and board[1] != "-":
    winner = board[0]
    # print("0 1 2")
    return True
  elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[3]
    # print("0 1 2")
    return True
  elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    # print("6 7 8")
    return True

  return False


#VERTICAL
def check_V(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True

  return False


#DIAGONAL
def check_D(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True

  return False


#TIE
def check_T(board):
  global gameRunning
  if "-" not in board:
    printBoard(board)
    print("Its a Tie :)")
    gameRunning = False


def check_win():
  if check_D(board) or check_H(board) or check_V(board):
    printBoard(board)
    print(f"The winner is {winner}")
    return True
  else:
    return False


#Switch player
def switch_P():
  global currentPlayer
  currentPlayer = "O" if currentPlayer == "X" else "X"
  

#game runs :DDDD
while gameRunning:
  printBoard(board)
  playerInput(board)
  if check_win():
    break

  if check_T(board):
    break

  switch_P()


