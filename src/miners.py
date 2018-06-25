# standard imports

# package imports

# local imports
from src import gameboard

# notes:
# log file for each run, log method that easily lets you log a print statement
# board ascii pieces file(s)


def loop(board):
    board.print_board()


def run():
    board = gameboard()
    loop(board)


if __name__ == "__main__":
    run()
    print("Miners main just got called?")
