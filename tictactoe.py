"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    sum_x = 0
    sum_o = 0

    for row in board:
        sum_x = sum_x + row.count('X')
        sum_o = sum_o + row.count('O')

    if sum_x == sum_o:
        return 'X'
    else:
        return 'O'
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possibles = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibles.add((i, j))

    return possibles


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
   
    new_board = copy.deepcopy(board)

    # action is a tuple
    i = action[0]
    j = action[1]

    if board[i][j] is EMPTY:
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception('Not a valid move') 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'X':
            return 'X'
        elif board[i][0] == board[i][1] == board[i][2] == 'O' or board[0][i] == board[1][i] == board[2][i] == 'O':
            return 'O'
     
        if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
            return 'X'
        elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
            return 'O'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    
    sum = 0

    for row in board:
        sum = row.count('X') + row.count('O')

    if sum == 9 :
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)

    if win == 'X':
        return 1
    elif win == 'O':
        return -1

    return 0


def max_value(board):
    if terminal(board):
        return utility(board)

    v = float('-inf')

    for action in actions(board):
        m = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = float('inf')

    for action in actions(board):
        m = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    optimal_action = None

    if player(board) == 'X':
        v = float('-inf')

        for action in actions(board):
            minimum_value = min_value(result(board, action))

            if minimum_value > v:
                v = minimum_value
                optimal_action = action

    elif player(board) == 'O':
        v = float('inf')

        for action in actions(board):
            maximum_value = max_value(result(board, action))

            if maximum_value < v:
                v = maximum_value
                optimal_action = action

    return optimal_action
