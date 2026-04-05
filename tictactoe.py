"""
Tic Tac Toe Player
"""

import math

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action")
    
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board using Alpha-Beta Pruning.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        max_eval = -math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            eval = minimax_value(new_board, False, -math.inf, math.inf)
            if eval > max_eval:
                max_eval = eval
                best_action = action
        return best_action
    else:
        min_eval = math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            eval = minimax_value(new_board, True, -math.inf, math.inf)
            if eval < min_eval:
                min_eval = eval
                best_action = action
        return best_action


def minimax_value(board, is_maximizing, alpha, beta):
    """
    Helper function to compute the minimax value of a board state using Alpha-Beta Pruning.
    
    Alpha: the best value that the maximizer currently can guarantee
    Beta: the best value that the minimizer currently can guarantee
    """
    if terminal(board):
        return utility(board)
    
    if is_maximizing:
        max_eval = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            eval = minimax_value(new_board, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            # Beta cutoff: if alpha >= beta, we can prune the remaining branches
            if alpha >= beta:
                break
        return max_eval
    else:
        min_eval = math.inf
        for action in actions(board):
            new_board = result(board, action)
            eval = minimax_value(new_board, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            # Alpha cutoff: if beta <= alpha, we can prune the remaining branches
            if beta <= alpha:
                break
        return min_eval
