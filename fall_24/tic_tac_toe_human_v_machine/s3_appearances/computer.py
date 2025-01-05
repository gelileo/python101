# - first available
# - random move
# - center move
# - corner move
# - edge move
# - winning move
# - blocking moving
from game_logic import (
    check_win,
    check_tie,
    two_in_a_row,
    two_in_a_column,
    two_in_a_diagonal,
)
from log import Logger

import random


def log(msg):
    mylogger.log(msg)


def computer_move(board, player, level, logger=None):
    global mylogger
    if logger:
        mylogger = logger
    else:
        mylogger = Logger()

    if level == "Easy":
        make_computer_mov_easy(board)
    elif level == "Hard":
        make_computer_move_hard(board, player)
    elif level == "Pro":
        make_computer_move_pro(board, player)


def make_computer_mov_easy(board):
    if not center_move(board):
        if not corner_move(board):
            random_move(board)


def make_computer_move_hard(board, player):
    if not winning_move(board, player):
        if not center_move(board):
            if not corner_move(board):
                if not blocking_move(board, player):
                    random_move(board)


def make_computer_move_pro(board, player):
    if not winning_move(board, player):
        # log("no winning move")
        if not blocking_move(board, player):
            # log("no blocking move")
            if not center_move(board):
                # log("no center move")
                if not fork_move(board, player):
                    if not blocking_fork_move(board, player):
                        # if center is 'O'
                        if board[1][1] == "O":
                            # log("I have center piece")
                            if not edge_move(board):
                                # log("no edge")
                                first_awailable_move(board)
                        else:
                            # log("I do not have center piece")
                            if not corner_move(board):
                                # log("no corner move")
                                first_awailable_move(board)


def make_move(board, row, col, player):
    board[row][col] = player
    log(f"computer O: ({row}, {col})")


def random_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = "O"
            break


def first_awailable_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                make_move(board, row, col, "O")
                return


def center_move(board):
    if is_available(board, 1, 1):
        make_move(board, 1, 1, "O")
        return True
    return False


def edge_move(board):
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(edges)
    for edge in edges:
        i, j = edge
        if is_available(board, i, j):
            make_move(board, i, j, "O")
            return True
    return None


def corner_move(board):
    all_corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in all_corners:
        row = corner[0]
        col = corner[1]
        if is_available(board, row, col):
            make_move(board, row, col, "O")
            return True
    return False


def is_available(board, row, col):
    return board[row][col] == ""


def board_copy(board):
    ret = [["" for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            ret[row][col] = board[row][col]

    return ret


def winning_move(board, player):
    res = try_winning_move(board, player)
    if res == None:
        return False
    else:
        row, col = res
        make_move(board, row, col, player)
        return True


def try_winning_move(board, player):
    # loop through all the available
    # make tentative move
    # check for win
    for row in range(3):
        for col in range(3):
            tmp_board = board_copy(board)
            if is_available(board, row, col):
                tmp_board[row][col] = player
                win, _ = check_win(tmp_board, player)
                if win:
                    return (row, col)
    return None


def blocking_move(board, player):
    other_player = "X" if player == "O" else "O"
    res = try_winning_move(board, other_player)
    if res == None:
        return False
    else:
        row, col = res
        make_move(board, row, col, player)
        return True


def blocking_move_0(board, player):
    other_player = "X" if player == "O" else "O"  # Get other player
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":  # If possible move for player
                board2 = board_copy(board)  # Make a copy of the board
                board2[row][col] = other_player
                win, _ = check_win(board2, other_player)
                if win:  # If its win
                    make_move(board, row, col, player)
                    return True
    return False


def fork_move(board, player="O"):
    res = try_fork_move(board, player)
    if res == None:
        return False
    else:
        row, col = res
        make_move(board, row, col, player)
        return True


def blocking_fork_move(board, player="O"):
    other_player = "X" if player == "O" else "O"
    res = try_fork_move(board, other_player)
    if res == None:
        return False
    else:
        row, col = res
        make_move(board, row, col, player)
        return True


def try_fork_move(board, player="O"):
    """
    Check if the player can create a fork.
    Returns: a move (Int, Int) for the computer player. None if no fork move is possible
    """
    for row in range(3):
        for col in range(3):
            if is_available(board, row, col):
                tmp_board = board_copy(board)
                tmp_board[row][col] = player
                winning_moves = 0
                if two_in_a_row(tmp_board, player):
                    winning_moves += 1
                if two_in_a_column(tmp_board, player):
                    winning_moves += 1
                if two_in_a_diagonal(tmp_board, player):
                    winning_moves += 1

                if winning_moves > 1:
                    return (row, col)

    return None
