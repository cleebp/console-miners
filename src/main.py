# standard imports
import time

# package imports

# local imports
from src.game_board import Gameboard
from src.game_state import Gamestate

# Globals are bad m'kay
FPS = 1  # lol


def game_logic(board, state):
    Gameboard.print_board(board)
    state.iteration += 1


def loop(board, state):
    while True:
        t1 = time.time()
        game_logic(board, state)
        sleep_time = 1.0/FPS - (time.time()-t1)
        time.sleep(sleep_time)


def run(platform):
    state = Gamestate(0, 0, 0)
    board = Gameboard(platform, state)
    loop(board, state)
