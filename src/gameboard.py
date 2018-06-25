# imports
import os

BOARD_TOP = ['''
   |/     \|/  \|                         |/  |/   | |/     
   |   \| \|/  \|                         |/ \|/  \|\|/  |/ 
   |    |  |    |                         |   |    | |   |  
^^^^^^^^^^^^^^^^^^^|                    |^^^^^^^^^^^^^^^^^^^''']

BOARD_LEVELS = ['''~~~~~~~~~~~~~~~~~~~|____________________|~~~~~~~~~~~~~~~~~~~''']

TOP_BAR = ['GOLD: ', 'GPS: ', 'ITERATION: ']

class Gameboard(object):
    """Contains all properties needed to draw the game board.
    """

    current_board = []
    total_gold = 0.0
    gps = 0.0
    iteration = 0
    platform = ''

    def __init__(self, platform):
        self.platform = platform
        self.current_board = [BOARD_TOP[0]]
        for i in range(10):
            self.current_board.append(BOARD_LEVELS[0])

    def print_board(self):
        if self.platform is 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        self.print_top_bar()
        for i in range(len(self.current_board)):
            print(self.current_board[i])
        self.iteration += 1

    def print_top_bar(self):
        to_print = str(TOP_BAR[0]) + str(self.total_gold) + '\t' + \
                   str(TOP_BAR[1]) + str(self.gps) + '\t' + \
                   str(TOP_BAR[2]) + str(self.iteration)
        print(to_print)
