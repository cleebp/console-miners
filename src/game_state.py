

class Gamestate(object):
    """Holds all logical items related to the current game state.
    """

    total_gold = 0.0
    gps = 0.0
    iteration = 0

    def __init__(self, total_gold, gps, iteration):
        self.total_gold = total_gold
        self.gps = gps
        self.iteration = iteration
