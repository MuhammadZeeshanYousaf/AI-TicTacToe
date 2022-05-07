from constants import *


class Board:
    # instance variables
    __board = [[None, None, None],
               [None, None, None],
               [None, None, None]]

    # methods
    def game_board(self):
        return self.__board.copy()

    def rows(self):
        return list(self.__board)

    def columns(self):
        from numpy import transpose
        return transpose(self.__board)

    def diagonals(self) -> list:
        b = self.__board
        diagonal1 = [b[0][0], b[1][1], b[2][2]]
        diagonal2 = [b[0][2], b[1][1], b[2][0]]
        return list((diagonal1, diagonal2))

    def row_col_dia(self):
        combine_list = list()
        combine_list.append([i for i in self.rows()])
        combine_list.append([j for j in self.columns()])
        combine_list.append([k for k in self.diagonals()])
        return combine_list

    def __mark(self, row: int, col: int, symbol: bool):
        if self.__board[row][col] is None:
            self.__board[row][col] = symbol
        else:
            raise Exception("The Board Box is not empty.")

    def tick(self, row, col): self.__mark(row, col, TICK)

    def cross(self, row, col): self.__mark(row, col, CROSS)

    # Code Docs
    game_board. __doc__ = "@return __board[list]"
    __mark.     __doc__ = "@params row, col, symbol[bool] \n raises Exception"
    tick.       __doc__ = "@params row, column, symbol[bool]"
    cross.      __doc__ = "@params row, column, symbol[bool]"
    row_col_dia.__doc__= "@returns combine_list[list] it generates a combine list of rows, columns and diagonals"