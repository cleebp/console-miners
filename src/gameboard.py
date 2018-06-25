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
	#def __init__(self):

	@staticmethod
	def print_board(self):
		print(BOARD_TOP)
		for i in range(10):
			print(BOARD_LEVELS[0])
