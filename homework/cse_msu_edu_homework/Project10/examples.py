"""
Created on Wed May 16 13:47:17 2018

@author: khaled
"""
from checkers import Piece
from checkers import Board

"""
This file contains some example boards for testing your code.
"""


def board_initial():
    """
    An example initial board.
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    board = Board()
    cells = eval("[[None, 'b', None, 'b', None, 'b', None, 'b'], " + \
                 "['b', None, 'b', None, 'b', None, 'b', None], " + \
                 "[None, 'b', None, 'b', None, 'b', None, 'b'], " + \
                 "[None, None, None, None, None, None, None, None], " + \
                 "[None, None, None, None, None, None, None, None], " + \
                 "['w', None, 'w', None, 'w', None, 'w', None], " + \
                 "[None, 'w', None, 'w', None, 'w', None, 'w'], " + \
                 "['w', None, 'w', None, 'w', None, 'w', None]]")
    for row, lst in enumerate(cells):
        for col, item in enumerate(lst):
            if item is not None:
                if item == 'w':
                    board.place(row, col, Piece('white'))
                else:
                    board.place(row, col, Piece())
    return board


def board_figure1():
    """
    The board from Figure 1.
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    board = Board()
    board.place(0, 7, Piece('white', is_king=True))
    board.place(1, 2, Piece('white', is_king=True))
    board.place(1, 4, Piece('white', is_king=True))
    board.place(3, 0, Piece('white'))
    board.place(3, 2, Piece('white'))
    board.place(4, 7, Piece('white'))
    board.place(5, 0, Piece('white'))
    board.place(5, 2, Piece('white'))
    board.place(6, 3, Piece('white'))
    board.place(6, 5, Piece('white'))
    board.place(6, 7, Piece('white'))
    board.place(7, 0, Piece('white'))
    board.place(2, 5, Piece())
    board.place(2, 7, Piece())
    board.place(3, 6, Piece())
    board.place(4, 3, Piece())
    board.place(4, 5, Piece())
    return board


def board_capture_blacks():
    """
    A board where a white captures a series of blacks.
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    board = Board()
    board.place(7, 0, Piece('white'))
    board.place(1, 6, Piece('white', is_king=True))
    board.place(2, 1, Piece())
    board.place(2, 3, Piece())
    board.place(2, 5, Piece())
    board.place(4, 1, Piece())
    board.place(4, 3, Piece())
    board.place(4, 5, Piece())
    board.place(6, 1, Piece())
    board.place(6, 3, Piece())
    board.place(6, 5, Piece())
    return board


def board_capture_whites():
    """
    A board where a black captures a series of white.
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    board = Board()
    board.place(7, 0, Piece(is_king=True))
    board.place(1, 6, Piece())
    board.place(2, 1, Piece('white'))
    board.place(2, 3, Piece('white'))
    board.place(2, 5, Piece('white'))
    board.place(4, 1, Piece('white'))
    board.place(4, 3, Piece('white'))
    board.place(4, 5, Piece('white'))
    board.place(6, 1, Piece('white'))
    board.place(6, 3, Piece('white'))
    board.place(6, 5, Piece('white'))
    return board


def board_capture_blacks2():
    """
    A board where a white captures a series of blacks.
    Version 2
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    board = Board()
    board.place(7, 0, Piece('white'))
    board.place(7, 6, Piece('white'))
    board.place(1, 6, Piece('white', is_king=True))
    board.place(1, 0, Piece('white', is_king=True))
    board.place(2, 1, Piece())
    board.place(2, 3, Piece())
    board.place(2, 5, Piece())
    board.place(4, 1, Piece())
    board.place(4, 3, Piece())
    board.place(4, 5, Piece())
    board.place(6, 1, Piece())
    board.place(6, 3, Piece())
    board.place(6, 5, Piece())
    return board


def board_capture_whites2():
    """
    A board where a black captures a series of white.
    Version 2
    """
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']
    board = Board()
    board.place(1, 6, Piece())
    board.place(1, 0, Piece())
    board.place(7, 0, Piece(is_king=True))
    board.place(7, 6, Piece(is_king=True))
    board.place(2, 1, Piece('white'))
    board.place(2, 3, Piece('white'))
    board.place(2, 5, Piece('white'))
    board.place(4, 1, Piece('white'))
    board.place(4, 3, Piece('white'))
    board.place(4, 5, Piece('white'))
    board.place(6, 1, Piece('white'))
    board.place(6, 3, Piece('white'))
    board.place(6, 5, Piece('white'))
    return board


def board_capture_transition():
    board = Board()
    board.place(1, 0, Piece())
    board.place(1, 2, Piece())
    board.place(1, 4, Piece())
    board.place(1, 6, Piece())
    board.place(2, 1, Piece())
    board.place(2, 5, Piece())
    board.place(3, 0, Piece('white'))
    board.place(3, 2, Piece())
    board.place(3, 6, Piece())
    board.place(4, 1, Piece('white'))
    board.place(4, 7, Piece('white'))
    board.place(5, 0, Piece('white'))
    board.place(5, 2, Piece('white'))
    board.place(5, 6, Piece())
    board.place(6, 1, Piece('white'))
    board.place(6, 3, Piece())
    board.place(7, 4, Piece('black', True))
    board.place(7, 6, Piece('black', True))
    return board


if __name__ == "__main__":
    board = board_initial()
    board.display()

    board = board_figure1()
    board.display()

    board = board_capture_blacks()
    board.display()

    board = board_capture_whites()
    board.display()

    board = board_capture_blacks2()
    board.display()

    board = board_capture_whites2()
    board.display()

    board = board_capture_transition()
    board.display()