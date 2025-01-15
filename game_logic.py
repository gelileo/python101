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
    global status
    if (
        check_diagnal(board, current_player)
        or check_row(board, current_player)
        or check_column(board, current_player)
    ):
        return True
    else:
        return False


def two_in_a_row(board, player="O"):
    """
    Check if the player has two in a row.
    """
    for row in range(3):
        if board[row].count(player) == 2 and "" in board[row]:
            return True

    return False


def two_in_a_column(board, player="O"):
    """
    Check if the player has two in a column.
    """
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(player) == 2 and "" in column:
            return True
    return False


def two_in_a_diagonal(board, player="O"):
    """
    Check if the player has two in a diagonal.
    """
    diagonal1 = [board[i][i] for i in range(3)]  # \ diagonal
    if diagonal1.count(player) == 2 and "" in diagonal1:
        return True

    diagonal2 = [board[i][2 - i] for i in range(3)]  # / diagonal
    if diagonal2.count(player) == 2 and "" in diagonal2:
        return True

    return False
