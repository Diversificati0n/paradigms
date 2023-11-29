
class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for i, row in enumerate(self.board):
            print(" " + " | ".join(row) + " ")
            if i < 2:
                print("-----------")
        print("*****************************")

    def is_cell_empty(self, row, col):
        return self.board[row][col] == ' '

    def set_cell(self, row, col, player):
        self.board[row][col] = player

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
