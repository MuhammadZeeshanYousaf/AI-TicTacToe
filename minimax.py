# here we are taking TICK for Max and CROSS for Min
# from constants import *
from board import *


def terminate_test(b: Board):
    # we can also return string instead of list(won?, who_won?)
    for rcd in b.row_col_dia():
        if rcd.count(TICK) == 3: return list((True, TICK))
        if rcd.count(CROSS) == 3: return list((True, CROSS))
    return False


def get_x(b: Board):
    # row, column, diagonal available for max having two '1' & no '0'
    x = 0
    for rcd in b.row_col_dia():
        if rcd.count(TICK) == 2 and rcd.count(CROSS) == 0: x += 1
    return x


def get_o(b: Board):
    # row, column, diagonal available for max having one '1' & no '0'
    o = 0
    for rcd in b.row_col_dia():
        if rcd.count(TICK) == 1 and rcd.count(CROSS) == 0: o += 1
    return o


def get_z(b: Board):
    # row, column, diagonal available for min having two '0' & no '1'
    z = 0
    for rcd in b.row_col_dia():
        if rcd.count(CROSS) == 2 and rcd.count(TICK) == 0: z += 1
    return z


def get_y(b: Board):
    # row, column, diagonal available for min having one '0' & no '1'
    y = 0
    for rcd in b.row_col_dia():
        if rcd.count(CROSS) == 1 and rcd.count(TICK) == 0: y += 1
    return y


def evaluate(b: Board):
    return (3 * get_x(b) + get_o(b)) - (3 * get_z(b) + get_y(b))


# empty = lambda variable: isinstance(variable, type(None))


def child_nodes(b: Board) -> int:
    empty_nodes = 0
    for row in b.game_board():
        empty_nodes += row.count(None)
    return empty_nodes


# function signature with default params
# def minimax(depth=0, board=Board(), maximizingPlayer=True, alpha=MIN, beta=MAX):
# Returns optimal value for current player
def minimax(depth, board, maximizingPlayer, alpha, beta):
    def ply(mark: bool):
        game_board = board.game_board()
        for i in range(len(game_board)):
            for j in range(len(game_board[i])):
                if game_board[i][j] is None:
                    if mark == TICK: board.tick(i, j)
                    elif mark == CROSS: board.cross(i, j)
                    return

    # Terminating condition. i.e.
    # terminate after one move ( 1 move = 2 ply = 1 max ply + 1 min ply )
    if depth == 2:
        return evaluate(board), board

    if maximizingPlayer:
        '''MAX Node'''
        best = MIN
        # Recur for possible no. of children for current state of board
        for each in range(child_nodes(board)):
            # Max making one ply
            ply(TICK)
            val = minimax(depth + 1, board, False, alpha, beta)[0]
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning
            if alpha >= beta:
                break
        return best, board
    else:
        '''MIN Node'''
        best = MAX
        # Recur for possible no. of children for current state of board
        for each in range(child_nodes(board)):
            # After Max ply, making Min's one ply
            ply(CROSS)
            val = minimax(depth + 1, board, True, alpha, beta)[0]
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if alpha >= beta:
                break
        return best, board


# Code Docs
# empty.__doc__ = "@params variable[any] \n @return bool \n It checks whether the variable is of type None or not."
child_nodes.__doc__ = "This function takes an argument 'b' of type Board and returns how many children can be " \
                      "created for current board "
