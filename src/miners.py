# standard imports

# package imports

# local imports
from src.gameboard import Gameboard

# notes:
# - log file for each run, log method that easily lets you log a print statement
#   board ascii pieces file(s)
# - loop needs to run x times per second on a while loop checking for game end conditions


def loop(board):
    Gameboard.print_board(board)


def run():
    board = Gameboard()
    loop(board)
