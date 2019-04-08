#2.40, #2.42
from lisplists import *


def queens(boardsize):
    empty_board = ()

    def is_safe(list_of_positions):
        pass

    def adjoin_pos():
        pass

    def enumerate_interval(i, j):
        if i > j:
            return None
        return cons(i, enumerate_interval(i+1, j))

    def queencols(k):
        if k == 0:
            makelist(empty_board)
        else:
            filterl(lambda positions: is_safe(positions),
                    flatmap(lambda rest_of_queens: mapl(lambda new_row: adjoin_pos(new_row, k, rest_of_queens),
                                                        enumerate_interval(1, boardsize)),
                            queencols(k - 1)))




