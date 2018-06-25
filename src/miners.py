# standard imports

# package imports

# local imports
import gameboard

# notes:
# log file for each run, log method that easily lets you log a print statement
# board ascii pieces file(s)


def loop():
    board.print_board()


if __name__ == "__main__":
    board = gameboard()
    print(board)
