import pytest
from OnitamaGame import OnitamaGame
from typing import List
from pieces import Pieces

# Helpers for testing
def move(board: List[List[str]], row_o: int, col_o: int, row_d: int, col_d: int):
    """
    Move a token on the board.
    Assume all moves are valid.
    """
    token = board[row_o][col_o]
    board[row_o][col_o] = Pieces.EMPTY
    board[row_d][col_d] = token


def assert_deeply(expected, actual):
    """
    Checking that the 2 boards or in general, two 2D lists are equal.
    """
    for i in range(len(expected)):
        assert expected[i] == actual[i]



# Test cases 
# Constatns for board states
state1 = [['x', ' ', 'X', 'x', 'x'],
    [' ', ' ',' ',' ',' ',],
    [' ', ' ',' ','x',' ',],
    [' ', 'y',' ',' ',' ',],
    ['y', ' ', 'Y', 'y', 'y']]
state2 = [['x', ' ', 'X', 'x', 'x'],
    [' ', ' ',' ',' ',' ',],
    [' ', ' ',' ','x',' ',],
    [' ', 'y',' ',' ',' ',],
    ['y', ' ', ' ', 'y', 'y']]
state3 = []
state4 = []
state5 = []
state6 = []
def test_something_else():
    onitama = OnitamaGame()
    onitama.set_board(state1)

def test_move():
    onitama = OnitamaGame()
    onitama.set_board(state1)
    # Initial state of the board.
    # [x, x, X, x, x]
    # [' ', ' ',' ',' ',' ',]
    # [' ', ' ',' ',' ',' ',]
    # [' ', ' ',' ',' ',' ',]
    # [y, y, Y, y, y]

    board = onitama.get_board()

    # Make some moves 
    # Currently it is P1s turn
    # Invalid moves
    # Bad style
    assert onitama.move(0, 0, 1, 0, 'dragon') == False
    # og position does not contain a token
    assert onitama.move(1, 0, 2, 0, 'crab') == False
    # destination position is not reachable
    assert onitama.move(0, 0, 2, 0, 'crab') == False

    assert onitama.move(0, 0, 1, 0, 'crab') == True
    # [' ', x, X, x, x]
    # [x, ' ',' ',' ',' ',]
    # [' ', ' ',' ',' ',' ',]
    # [' ', ' ',' ',' ',' ',]
    # [y, y, Y, y, y]

    # Checxk that the token actually moved properly.
    move(board,0, 0, 1, 0 )
    assert board == onitama.get_board()
    # alternative
    assert str(board) == str(onitama.get_board())
    # Check styles were exchanged properly.
    # Check its other players turn
