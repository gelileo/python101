# - first available
# - random move
# - center move
# - corner move
# - edge move
# - winning move
# - blocking moving
from game_logic import *

import random


def computer_move(board, player, level):
    """
    Make a move for player using strategies based on the level
    """  
    if level == "Easy":
      make_computer_move_easy(board, player)
    elif level == "Hard":
      make_computer_move_hard(board, player)
    else:
        make_computer_move_pro(board, player)
    


def make_computer_move_easy(board,player):
    """
    Make a move for the computer player.
    """
    if not winning_move(board, player):
        random_move(board)


def make_computer_move_hard(board, player):
    """
    Make a move for the computer player.
    """
    if not winning_move(board, player):
        if not corner_move(board):
            random_move(board)


def make_computer_move_pro(board, player):
    """
    Make a move for the computer player.
    """
    if not winning_move(board, player):
        if not blocking_move(board, player):
            if not corner_move(board):
                random_move(board)


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
                board[row][col] = "O"
                print(f"computer move: ({row}, {col})")
                return


def center_move(board):
    if is_available(board, 1, 1):
        board[1][1] = "O"
        return True
    return False


def corner_move(board):
    all_corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in all_corners:
        row = corner[0]
        col = corner[1]
        if is_available(board, row, col):
            board[row][col] = "O"
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
        board[row][col] = player
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
                if check_win(tmp_board, player):
                    # board[row][col] = player
                    return (row, col)
    return None


def blocking_move(board, player):
    other_player = "X" if player == "O" else "O"
    res = try_winning_move(board, other_player)
    if res == None:
        return False
    else:
        row, col = res
        board[row][col] = player
        return True


def blocking_move_0(board, player):
    other_player = "X" if player == "O" else "O"  # Get other player
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":  # If possible move for player
                board2 = board_copy(board)  # Make a copy of the board
                board2[row][col] = other_player
                if check_win(board2, other_player):  # If its win
                    board[row][col] = player
                    return True
    return False
