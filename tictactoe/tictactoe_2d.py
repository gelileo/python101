# Initialize the Tic-Tac-Toe board as a 2D array
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to check if a player has won
def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function for a player's move
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == ' ':
                    board[row][col] = player
                    break
                else:
                    print("Invalid move. Cell is already occupied. Please try again.")
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

# Main game loop
current_player = 'X'
while True:
    display_board(board)
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
