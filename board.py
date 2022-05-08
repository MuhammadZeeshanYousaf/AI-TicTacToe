from numpy import transpose
from constants import *


class Board:
    # instance variables
    __board = [[BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK],
               [BLANK, BLANK, BLANK]]

    # methods
    def game_board(self):
        return self.__board

    def rows(self):
        return self.__board.copy()

    def columns(self):
        cols = transpose(self.__board)  # -> numpy.ndarray
        return [list(i) for i in cols]  # convert to list

    def diagonals(self) -> list:
        b = self.__board
        diagonal1 = [b[0][0], b[1][1], b[2][2]]
        diagonal2 = [b[0][2], b[1][1], b[2][0]]
        return list((diagonal1, diagonal2))

    def row_col_dia(self):
        return self.rows() + self.columns() + self.diagonals()

    def tick(self, row, col): self.__board[row][col] = TICK

    def cross(self, row, col): self.__board[row][col] = CROSS

    def blank(self, row, col): self.__board[row][col] = BLANK

    # Code Docs
    game_board. __doc__ = "@return __board[list]"
    tick.       __doc__ = "@params row, column, symbol[bool]"
    cross.      __doc__ = "@params row, column, symbol[bool]"
    row_col_dia.__doc__ = "@returns combine_list[list] it generates a combine list of rows, columns and diagonals"
