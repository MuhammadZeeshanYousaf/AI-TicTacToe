from minimax import *

if __name__ == '__main__':
    # Driver code here
    # print("** Welcome to Tic Tac Toe **".upper())
    print("=========Testing=========")

    myboard = Board()
    # myboard.tick(0, 0)
    # myboard.tick(0, 1)
    # myboard.cross(0, 2)
    # myboard.tick(2, 0)
    myboard.tick(2, 2)
    myboard.cross(1, 0)
    # myboard.tick(2, 2)
    myboard.cross(1, 1)
    myboard.tick(1, 2)
    # myboard.tick(0, 1)
    # myboard.cross(0, 2)

    print(myboard.game_board()[0], "\n", myboard.game_board()[1], "\n", myboard.game_board()[2], ":BOARD")
    # print(myboard.rows(), "\n--")
    # print(myboard.columns(), "\n--")
    # print(myboard.diagonals(), "\n--")
    # print(myboard.row_col_dia(), "\n--")
    # print(myboard.diagonals()[1][0])

    # unit test of evaluation for current state of board
    print("x", get_x(myboard))
    print("o", get_o(myboard))
    print("z", get_z(myboard))
    print("y", get_y(myboard))
    print("Evaluated", evaluate(myboard))

    print("possible child nodes", empty_cells(myboard))

    # dup_board = deepcopy(myboard)     # myboard replica
    # print(myboard)
    # print(duplicate_board)

    val = minimax(0, myboard, True, MIN, MAX)
    print("optimal value", val[0])
    print(val[1], val[2])   # evaluated row and column
    myboard.tick(val[1], val[2])    # mark the optimal ply to the current board
    print("current board now", myboard.game_board())    # after minimax, the current board

    print("==========================")