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
    # print(x)
    return x


def get_o(b: Board):
    # row, column, diagonal available for max having one '1' & no '0'
    o = 0
    for rcd in b.row_col_dia():
        if rcd.count(TICK) == 1 and rcd.count(CROSS) == 0: o += 1
    # print(o)
    return o


def get_z(b: Board):
    # row, column, diagonal available for min having two '0' & no '1'
    z = 0
    for rcd in b.row_col_dia():
        if rcd.count(CROSS) == 2 and rcd.count(TICK) == 0: z += 1
    # print(z)
    return z


def get_y(b: Board):
    # row, column, diagonal available for min having one '0' & no '1'
    y = 0
    for rcd in b.row_col_dia():
        if rcd.count(CROSS) == 1 and rcd.count(TICK) == 0: y += 1
    # print(y)
    return y


def evaluate(b: Board):
    return (3 * get_x(b) + get_o(b)) - (3 * get_z(b) + get_y(b))


def empty_cells(b: Board) -> int:
    _empty_cells = 0
    for row in b.game_board():
        _empty_cells += row.count(BLANK)
    return _empty_cells


def ply(b: Board, avoid_mark, mark: bool):
    for i in range(len(b.game_board())):
        for j in range(len(b.game_board()[i])):
            if len(avoid_mark) != 0:     # if we need to avoid marking some cells
                for avoid in avoid_mark:
                    if b.game_board()[i][j] is BLANK and avoid[0] != i and avoid[1] != j:
                        if mark == TICK:
                            b.tick(i, j)
                        elif mark == CROSS:
                            b.cross(i, j)
                        return i, j
            else:       # if we don't need to avoid any cell marking
                if b.game_board()[i][j] is BLANK:
                    if mark == TICK:
                        b.tick(i, j)
                    elif mark == CROSS:
                        b.cross(i, j)
                    return i, j


# function signature minimax(depth=0, board=Board(), maximizingPlayer=True, alpha=MIN, beta=MAX, row=0, col=0):
# Returns optimal value for current player and row column for the optimal ply
def minimax(depth, board, maximizingPlayer, alpha, beta, row=0, col=0):
    _empty_cells = empty_cells(board)
    # Terminating condition
    if depth == 3:
        print(board.game_board())
        print(evaluate(board))
        return evaluate(board), row, col

    max_plys = []
    min_plys = []
    if maximizingPlayer:
        '''MAX Node'''
        best = MIN
        # Recur for possible no. of children for current state of board
        for each in range(_empty_cells):
            # Max making one ply
            row, col = ply(board, max_plys, TICK)
            max_plys.append([row, col])     # store max ply to restore after all iterations
            val = minimax(depth + 1, board, False, alpha, beta, row, col)
            board.blank(row, col)  # undo the ply
            if val[0] > best:
                row, col = val[1], val[2]  # update optimal row column
            alpha = max(alpha, best)
            best = max(best, val[0])
            # Alpha Beta Pruning
            if alpha >= beta:
                break
        del max_plys
        return best, row, col
    else:
        '''MIN Node'''
        best = MAX
        # Recur for possible no. of children for current state of board
        for each in range(_empty_cells):
            # After Max ply, making Min's one ply
            row, col = ply(board, min_plys, CROSS)
            min_plys.append([row, col])     # store min ply to restore after all iterations
            val = minimax(depth + 1, board, True, alpha, beta, row, col)
            board.blank(row, col)  # undo the ply
            if val[0] < best:
                row, col = val[1], val[2]  # update optimal row column
            best = min(best, val[0])
            beta = min(beta, best)
            # Alpha Beta Pruning
            if alpha >= beta:
                break
        del min_plys
        return best, row, col


# Code Docs
empty_cells.__doc__ = "This function takes an argument 'b' of type Board and returns how many children can be " \
                      "created for current board "
ply.        __doc__ = "This function take a board and mark symbol as arguments and return row col of the first " \
              "occurred blank space. "
terminate_test.__doc__ = "Returns BLANK if no player win or return player which player won"
