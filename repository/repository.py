from domain.board import Board
from domain.ship import Ship

from repository.repo_exception import RepositoryException
from domain.domain_exception import DomainException


class Repository:

    def __init__(self):
        self._player_board = Board("player")
        self._computer_board = Board("computer")

    def get_value_of_the_players_board(self, row, column):
        return self._player_board.get_board_cell(row, column)

    def generate_board(self):
        values_based_on_ship_types = {5:'carrier', 4:'battleship', 3:'destroyer', 2:'submarine', 1:'patrol boat'}
        ship_code = {'carrier', 'battleship', 'destroyer', 'submarine', 'patrol boat', 'hit_carrier', 'hit_battleship',
                     'hit_destroyer', 'hit_submarine', 'hit_patrol boat', 'X', 'unmarked'}
        for i in [5, 4, 3, 2, 1]:
            variable = 0
            while variable == 0:
                try:
                    new_ship = Ship(values_based_on_ship_types[i], None, None, None)
                    new_ship.generate_ship()
                    self.adding_a_ship("computer", new_ship)
                except DomainException:
                    variable = 0
                except RepositoryException:
                    variable = 0
                else:
                    variable = 1

    def adding_a_ship(self, player: str, new_ship: Ship):
        if player == "player":
            self._player_board.adding_a_ship_to_board(new_ship)
        else:
            self._computer_board.adding_a_ship_to_board(new_ship)

    def attacking_the_board(self, player, row, column):
        key = f"row:{str(row)},column:{str(column)}"
        if player == "player":
            result_of_attack = self._player_board.attacking_a_cell(key)
        else:
            result_of_attack = self._computer_board.attacking_a_cell(key)
        return result_of_attack

    def __str__(self):
        formatting_the_result = ""
        formatting_the_result += "Player's Board:\n"
        formatting_the_result += str(self._player_board)
        formatting_the_result += "\nComputer's Board:\n"
        formatting_the_result += str(self._computer_board)
        return formatting_the_result
