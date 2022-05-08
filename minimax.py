# here we are taking TICK for Max and CROSS for Min
from board import *


def terminate_test(b: Board):
    # returns BLANK if no player win
    for rcd in b.row_col_dia():
        if rcd.count(TICK) == 3: return TICK
        if rcd.count(CROSS) == 3: return CROSS
    return BLANK


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


def child_nodes(b: Board) -> int:
    empty_nodes = 0
    for row in b.game_board():
        empty_nodes += row.count(BLANK)
    return empty_nodes


def ply(b: Board, mark: bool):
    for i in range(len(b.game_board())):
        for j in range(len(b.game_board()[i])):
            if b.game_board()[i][j] is BLANK:
                if mark == TICK:
                    b.tick(i, j)
                elif mark == CROSS:
                    b.cross(i, j)
                return i, j


# function signature minimax(depth=0, board=Board(), maximizingPlayer=True, alpha=MIN, beta=MAX, row=0, col=0):
# Returns optimal value for current player and row column for the optimal ply
def minimax(depth, board, maximizingPlayer, alpha, beta, row=0, col=0):
    empty_cells = child_nodes(board)
    # Terminating condition
    if depth == 3:
        return evaluate(board), row, col

    if maximizingPlayer:
        '''MAX Node'''
        best = MIN
        # Recur for possible no. of children for current state of board
        for each in range(empty_cells):
            # Max making one ply
            row, col = ply(board, TICK)
            val = minimax(depth + 1, board, False, alpha, beta, row, col)
            board.blank(row, col)  # undo the ply
            row, col = val[1], val[2]  # update optimal row column
            alpha = max(alpha, best)
            best = max(best, val[0])
            # Alpha Beta Pruning
            if alpha >= beta:
                break
        return best, row, col
    else:
        '''MIN Node'''
        best = MAX
        # Recur for possible no. of children for current state of board
        for each in range(empty_cells):
            # After Max ply, making Min's one ply
            row, col = ply(board, CROSS)
            val = minimax(depth + 1, board, True, alpha, beta, row, col)
            board.blank(row, col)  # undo the ply
            row, col = val[1], val[2]  # update optimal row column
            best = min(best, val[0])
            beta = min(beta, best)
            # Alpha Beta Pruning
            if alpha >= beta:
                break
        return best, row, col


# Code Docs
child_nodes.__doc__ = "This function takes an argument 'b' of type Board and returns how many children can be " \
                      "created for current board "
ply.        __doc__ = "This function take a board and mark symbol as arguments and return row col of the first " \
              "occurred blank space. "
terminate_test.__doc__ = "Returns BLANK if no player win or return player which player won"
