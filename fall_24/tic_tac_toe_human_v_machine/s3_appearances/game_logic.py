def check_row(board, current_player):
    for row_idx, row in enumerate(board):
        if all(cell == current_player for cell in row):
            # Collect the winning cells for the row
            return [(row_idx, col_idx) for col_idx in range(3)]
    return []


def check_column(board, current_player):
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)):
            # Collect the winning cells for the column
            return [(row_idx, col) for row_idx in range(3)]
    return []


def check_diagnal(board, current_player):
    # Check the main diagonal
    if all(board[i][i] == current_player for i in range(3)):
        return [(i, i) for i in range(3)]
    # Check the anti-diagonal
    if all(board[i][2 - i] == current_player for i in range(3)):
        return [(i, 2 - i) for i in range(3)]
    return []


def check_tie(board):
    if all(cell != "" for row in board for cell in row):
        return True
    else:
        return False


def check_win(board, current_player):
    # Check rows
    winning_cells = check_row(board, current_player)
    if winning_cells:
        return (True, winning_cells)

    # Check columns
    winning_cells = check_column(board, current_player)
    if winning_cells:
        return (True, winning_cells)

    # Check diagonals
    winning_cells = check_diagnal(board, current_player)
    if winning_cells:
        return (True, winning_cells)

    # No win detected
    return (False, [])


def two_in_a_row(board, player="O"):
    for row in range(3):
        if board[row].count(player) == 2 and "" in board[row]:
            return True

    return False


def two_in_a_column(board, player="O"):
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(player) == 2 and "" in column:
            return True
    return False


def two_in_a_diagonal(board, player="O"):
    diagonal1 = [board[i][i] for i in range(3)]  # \ diagonal
    if diagonal1.count(player) == 2 and "" in diagonal1:
        return True

    diagonal2 = [board[i][2 - i] for i in range(3)]  # / diagonal
    if diagonal2.count(player) == 2 and "" in diagonal2:
        return True

    return False
