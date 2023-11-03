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

# Function for a player's move
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == ' ':
                if player == 'X':
                    board[move - 1] = 'X'
                else:
                    board[move - 1] = 'O'
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

# Main game loop
current_player = 'X'
while True:
    display_board(board
                  )
    if is_board_full(board) or is_winner(board, 'X') or is_winner(board, 'O'):
        break

    player_move(current_player)

    if is_board_full(board) or is_winner(board, 'X') or is_winner(board, 'O'):
        break

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'

# Display the final result
display_board(board)
if is_winner(board, 'X'):
    print("Player X wins!")
elif is_winner(board, 'O'):
    print("Player O wins!")
else:
    print("It's a tie!")
