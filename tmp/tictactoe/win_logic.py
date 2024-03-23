status = "Player X's turn"
current_player = "X"


def check_row(board):
    global winner
    for row in board:
        if all(cell == current_player for cell in row):
            return True

    return False


def check_column(board):
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)):
            return True
    return False


def check_diagnal(board):
    if all(board[i][i] == current_player for i in range(3)) or all(
        board[i][2 - i] == current_player for i in range(3)
    ):
        return True
    return False


def check_tie(board):
    global status
    if all(cell != "" for row in board for cell in row):
        status = "It's a tie!"
        return True
    else:
        return False


def check_win(board):
    global status
    if check_diagnal(board) or check_row(board) or check_column(board):
        # print(f"The winner is {current_player}")
        status = f"Game Over! The winner is {current_player}"
        return True
    else:
        return False
