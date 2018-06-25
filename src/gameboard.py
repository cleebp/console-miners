# imports

BOARD_TOP = ['''
   |/     \|/  \|                         |/  |/   | |/     
   |   \| \|/  \|                         |/ \|/  \|\|/  |/ 
   |    |  |    |                         |   |    | |   |  
^^^^^^^^^^^^^^^^^^^|                    |^^^^^^^^^^^^^^^^^^^''']

BOARD_LEVELS = ['''~~~~~~~~~~~~~~~~~~~|____________________|~~~~~~~~~~~~~~~~~~~''']


class Gameboard(object):
    """Contains all properties needed to draw the game board.
    """

    current_board = []

    def __init__(self):
        self.current_board = [BOARD_TOP[0]]
        for i in range(10):
            self.current_board.append(BOARD_LEVELS[0])


    @staticmethod
    def print_board(self):
        for i in range(len(self.current_board)):
            print(self.current_board[i])
