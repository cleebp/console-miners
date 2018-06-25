# standard imports
import time

# package imports

# local imports
from src.gameboard import Gameboard

# Globals are bad m'kay
FPS = 1  # lol


def game_logic(board):
    Gameboard.print_board(board)


def loop(board):
    while True:
        t1 = time.time()
        game_logic(board)
        sleep_time = 1.0/FPS - (time.time()-t1)
        time.sleep(sleep_time)


def run(platform):
    board = Gameboard(platform)
    loop(board)
