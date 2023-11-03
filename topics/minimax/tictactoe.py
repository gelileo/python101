import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to check if a player has won
def is_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function for the user's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == ' ':
                board[move - 1] = 'X'
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

# Function for the computer's move using the Minimax algorithm
def computer_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'Tie': 0}

    if is_winner(board, 'O'):
        return scores['O']
    if is_winner(board, 'X'):
        return scores['X']
    if is_board_full(board):
        return scores['Tie']

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Main game loop
while True:
    display_board(board)
    if is_board_full(board) or is_winner(board, 'X') or is_winner(board, 'O'):
        break

    player_move()
    display_board(board)

    if is_board_full(board) or is_winner(board, 'X') or is_winner(board, 'O'):
        break

    print("Computer's turn:")
    computer_move()

# Display the final result
display_board(board)
if is_winner(board, 'X'):
    print("You win!")
elif is_winner(board, 'O'):
    print("Computer wins!")
else:
    print("It's a tie!")
