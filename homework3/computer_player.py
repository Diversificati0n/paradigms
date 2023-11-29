import random

class ComputerPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return row, col
