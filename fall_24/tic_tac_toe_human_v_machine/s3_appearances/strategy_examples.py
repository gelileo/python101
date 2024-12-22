"""
Some strategies for the computer to play the tic-tac-toe game are:
- Random move: The computer makes a random move on the board.
- Winning move: The computer makes a move that will lead to a win.
- Center move: The computer makes a move to occupy the center of the board.
- Corner move: The computer makes a move to occupy a corner of the board.
- Edge move: The computer makes a move to occupy an edge of the board.
- Blocking move: The computer makes a move to block the opponent from winning.
- Fork move: The computer makes a move that creates multiple winning opportunities.
- Minimax algorithm: The computer uses the minimax algorithm to find the best move.
"""

import random
from game_logic import check_win, check_tie


def random_move(board):
    """
    Make a random move for the computer player
    Returns: a move (Int, Int) for the computer player
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = "O"
            print(f"Computer's move: {row}, {col}")
            return row, col


def winning_move(board, player="O"):
    """
    Make a winning move for the computer player
    Returns: a move (Int, Int) for the computer player. None if no winning move is possible
    """
    move = winning_move_three_in_a_row(board, player)
    if move:
        return move

    move = winning_move_three_in_a_column(board, player)
    if move:
        return move

    move = winning_move_three_in_a_diagonal(board, player)
    if move:
        return move

    return None


def blocking_move(board, player="X"):
    """
    Make a blocking move for the computer player.
    Fork is a scenario where it has two ways to win in the next move.
    This forces the opponent to block in two places, which is impossible.
    Returns: a move (Int, Int) for the computer player. None if no blocking move is possible
    """
    return winning_move(board, player)


def fork_move(board, player="O"):
    """
    Check if the player can create a fork.
    Returns: a move (Int, Int) for the computer player. None if no fork move is possible
    """
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    temp_board = board
    for pos in empty_positions:
        # Temporarily place the player in the empty position
        i, j = pos
        temp_board[i][j] = player

        # Count the number of winning moves created by this placement
        winning_moves = 0
        if winning_move_three_in_a_row(temp_board, player):
            winning_moves += 1
        if winning_move_three_in_a_column(temp_board, player):
            winning_moves += 1
        if winning_move_three_in_a_diagonal(temp_board, player):
            winning_moves += 1

        temp_board[i][j] = ""  # Undo the move

        # If the player can create more than one winning move, it's a fork
        if winning_moves > 1:
            return pos

    return None


def center_move(board):
    """
    Make a move to occupy the center of the board
    Returns: a move (Int, Int) for the computer player. None if the center is already occupied
    """
    if board[1][1] == "":
        print("Computer's move: 1, 1")
        return 1, 1
    return None


def corner_move(board):
    """
    Make a move to occupy a corner of the board
    Returns: a move (Int, Int) for the computer player. None if no corner move is possible
    """
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for corner in corners:
        i, j = corner
        if board[i][j] == "":
            print(f"Computer's move: {i}, {j}")
            return i, j
    return None


def edge_move(board):
    """
    Make a move to occupy an edge of the board
    Returns: a move (Int, Int) for the computer player. None if no edge move is possible
    """
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(edges)
    for edge in edges:
        i, j = edge
        if board[i][j] == "":
            print(f"Computer's move: {i}, {j}")
            return i, j
    return None


def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm to find the best move for the computer player
    Returns: the best score (Int) for the computer player
    """
    scores = {"X": -1, "O": 1, "Tie": 0}

    if check_win(board, "O"):
        return scores["O"]
    if check_win(board, "X"):
        return scores["X"]
    if check_tie(board):
        return scores["Tie"]

    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if is_maximizing:
        best_score = -float("inf")
        for pos in empty_positions:
            i, j = pos
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)

        return best_score
    else:
        best_score = float("inf")
        for pos in empty_positions:
            i, j = pos
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)

        return best_score


def minimax_move(board):
    """
    Make a move for the computer player using the Minimax algorithm
    Returns: a move (Int, Int) for the computer player
    """
    best_score = -float("inf")
    best_move = None
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    for pos in empty_positions:
        i, j = pos
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = pos
    if best_move:
        i, j = best_move
        print(f"Computer's move: {i}, {j}")
        return i, j

    return None


## Supporting functions for winning_move
def winning_move_three_in_a_row(board, player="O"):
    """
    Find a winning move for the computer player in a row
    Returns: a move (Int, Int) for the computer player. None if no winning move is possible
    """
    for row in range(3):
        if board[row].count(player) == 2 and "" in board[row]:
            col = board[row].index("")
            print(f"Computer's move: {row}, {col}")
            return row, col


def winning_move_three_in_a_column(board, player="O"):
    """
    Find a winning move for the computer player in a column
    Returns: a move (Int, Int) for the computer player. None if no winning move is possible
    """
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(player) == 2 and "" in column:
            row = column.index("")
            print(f"Computer's move: {row}, {col}")
            return row, col


def winning_move_three_in_a_diagonal(board, player="O"):
    """
    Find a winning move for the computer player in a diagonal
    Returns: a move (Int, Int) for the computer player. None if no winning move is possible
    """
    diagonal1 = [board[i][i] for i in range(3)]  # \ diagonal
    if diagonal1.count(player) == 2 and "" in diagonal1:
        index = diagonal1.index("")
        print(f"Computer's move: {index}, {index}")
        return index, index

    diagonal2 = [board[i][2 - i] for i in range(3)]  # / diagonal
    if diagonal2.count(player) == 2 and "" in diagonal2:
        index = diagonal2.index("")
        print(f"Computer's move: {index}, {2 - index}")
        return index, 2 - index
