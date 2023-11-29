# Крестики-нолики
# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

from board import Board
from player import Player
from computer_player import ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Игрок X", "X"), ComputerPlayer("Компьютер O", "O")]
        self.current_player = self.players[0]

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play_game(self):
        while True:
            self.board.print_board()

            row, col = self.current_player.make_move()

            if 0 <= row < 3 and 0 <= col < 3 and self.board.is_cell_empty(row, col):
                self.board.set_cell(row, col, self.current_player.symbol)

                if self.check_winner():
                    self.board.print_board()
                    print(f"{self.current_player.name} победил!")
                    break
                elif self.board.is_board_full():
                    self.board.print_board()
                    print("Ничья!")
                    break

                self.switch_player()
            else:
                print("Некорректный ход. Внимательнее смотри поле 3 на 3!.")

    def check_winner(self):
        player_symbol = self.current_player.symbol

        for i in range(3):
            if all(self.board.board[i][j] == player_symbol for j in range(3)) or \
               all(self.board.board[j][i] == player_symbol for j in range(3)):
                return True

        if all(self.board.board[i][i] == player_symbol for i in range(3)) or \
           all(self.board.board[i][2 - i] == player_symbol for i in range(3)):
            return True

        return False

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
