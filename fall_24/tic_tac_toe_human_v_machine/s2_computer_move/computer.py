import random


def random_move(board):
    """
    Make a random move for the computer player
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = "O"
            print(f"Computer's move: {row}, {col}")
            break


def computer_move(board):
    """
    Make a move for the computer player
    """
    random_move(board)
