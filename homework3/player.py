
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        row = int(input(f"{self.name}, выберите строку (1-3): ")) - 1
        col = int(input(f"{self.name}, выберите столбец (1-3): ")) - 1
        return row, col
