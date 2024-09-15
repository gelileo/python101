
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

board = [["-" for _ in range(3)] for _ in range(3)]


def printBoard(board):
  for row in board:
    print(f"{row[0]} | {row[1]} | {row[2]}")
    print("-" * 9)

currentPlayer = "X"
winner = None
gameRunning = True

def rowForMove(move):
  return (move - 1) // 3

def colForMove(move):
  return (move - 1) % 3


#take player input
def playerInput(board):
  while True:
    try:
      inp = int(input(f"Player {currentPlayer}, Enter a number 1-9: "))

      if inp >= 1 and inp <= 9 and board[rowForMove(inp)][colForMove(inp)] == "-":
        board[rowForMove(inp)][colForMove(inp)] = currentPlayer
        break
      else:
        print("Invalid Move, Try again")
    except ValueError:
      print("Invalid input. Please enter a number.")


#Check for win or tie
#HORiZONTAL
def check_H(board):
  global winner
  # if board[0] == board[1] == board[2] and board[1] != "-":
  #   winner = board[0]
  #   # print("0 1 2")
  #   return True
  # elif board[3] == board[4] == board[5] and board[3] != "-":
  #   winner = board[3]
  #   # print("0 1 2")
  #   return True
  # elif board[6] == board[7] == board[8] and board[6] != "-":
  #   winner = board[6]
  #   # print("6 7 8")
  #   return True

  for row in range(3):
    if all( row[row][i] == row[row][0] for i in range(3)):
      return true
  
  return False


#VERTICAL
def check_V(board):
  global winner
  for col in range(3):
    if all( board[row][col] == board[0][col] for row in range[3]):
      return True

  return False


#DIAGONAL
def check_D(board):
  global winner
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
    winner = board[0][0]
    return True
  elif board[1][1] == board[2][0] == board[0][2] and board[1][1] != "-":
    winner = board[1][1]
    return True

  return False


#TIE
def check_T(board):
  global gameRunning
  for row in range(3):
    for col in range(3):
      if "-" not in board[row][col]:
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

