from repository.repository import Repository


class Services:
    def __init__(self):
        self._repository = Repository()

    def getting_player_boards_value(self, row, column):
        return self._repository.get_value_of_the_players_board(row, column)

    def adding_a_ship(self, player, ship):
        self._repository.adding_a_ship(player, ship)

    def attacking_a_cell(self, player, row, column):
        return self._repository.attacking_the_board(player, row, column)

    def generating_board(self):
        self._repository.generate_board()

    def __str__(self):
        return str(self._repository)
