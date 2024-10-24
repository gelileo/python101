def check_row(board, current_player):
    for row in board:
        if all(cell == current_player for cell in row):
            return True

    return False


def check_column(board, current_player):
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)):
            return True
    return False


def check_diagnal(board, current_player):
    if all(board[i][i] == current_player for i in range(3)) or all(
        board[i][2 - i] == current_player for i in range(3)
    ):
        return True
    return False


def check_tie(board):
    if all(cell != "" for row in board for cell in row):
        return True
    else:
        return False


def check_win(board, current_player):
    if (
        check_diagnal(board, current_player)
        or check_row(board, current_player)
        or check_column(board, current_player)
    ):
        return True
    else:
        return False
