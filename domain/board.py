from domain.cell import Cell
from domain.domain_exception import DomainException
from domain.ship import Ship


class Board:
    def __init__(self, name):
        self._name = name
        self._data = {}
        # the dict will hold all the cells needed for the board

        for i in range(1, 11):
            for j in range(1, 11):
                key = f"row:{str(i)},column:{str(j)}"
                self._data[key] = Cell(i, j, "unmarked")

    def get_name(self):
        return self._name

    def get_board_cell(self, key):
        return self._data[key].get_value

    def get_board_cell_type(self, row, column):
        key = f"row:{str(row)},column:{str(column)}"
        ship_types = ['hit_carrier', 'hit_battleship', 'hit_patrol boat', 'hit_submarine', 'hit_destroyer']
        for ship in ship_types:
            if ship in self.get_board_cell(key):
                return ship
        return "none"

    def set_board_cell_value(self, key, new_value):
        self._data[key].set_value = new_value

    def checking_for_space(self, new_ship: Ship):
        new_row = new_ship.get_row
        new_column = new_ship.get_column
        if new_ship.get_orientation == "vertical":
            direction_row = 1
            direction_column = 0
        else:
            direction_row = 0
            direction_column = 1
        length = new_ship.get_length_of_ship()
        for i in range(length):
            if new_row > 10 or new_row < 1 or new_column > 10 or new_column < 1:
                raise DomainException("Wrong integer.")
            if self.get_board_cell_type(new_column, new_row) != "unmarked" and self.get_board_cell_type(new_column, new_row) != "none":
                raise DomainException("No space left to add here.")
            else:
                new_row = new_row + direction_row
                new_column = new_column + direction_column

    def board_not_concealed(self):
        empty_start_board = ""
        heading = " 0|   "
        for i in range(1, 10):
            heading += str(i) + "  |  "
            empty_start_board += "----"
        empty_start_board += "---"
        new_row = f"\n"
        heading += f'10    |{new_row} 1| '
        previous_row = 1
        for key in self._data:
            cell = self._data[key]
            if cell.get_row != previous_row:
                previous_row += 1
                if cell.get_row != 10:
                    heading += f'{new_row} {str(cell.get_row)}| '
                else:
                    heading += f'{new_row}{str(cell.get_row)}| '
            heading += str(cell) + " | "
        return heading

    def board_concealed(self):
        empty_start_board = ""
        heading = " 0|"
        for i in range(1, 10):
            heading += str(i) + " | "
            empty_start_board += "----"
        empty_start_board += "---"
        new_row = f"\n"
        heading += f'10|{new_row} 1| '
        previous_row = 1
        for key in self._data:
            cell = self._data[key]
            if cell.get_row != previous_row:
                previous_row += 1
                if cell.get_row != 10:
                    heading += f'{new_row} {str(cell.get_row)}| '
                else:
                    heading += f'{new_row}{str(cell.get_row)}| '
            if cell.get_value not in ['hit_carrier', 'hit_battleship', 'hit_destroyer', 'hit_submarine',
                                      'hit_patrol boat', 'X']:
                x = '?'
            else:
                x = str(cell.get_value)

            heading += x + " | "
        return heading

    def attacking_a_cell(self, key):
        values = {'carrier', 'battleship', 'destroyer', 'submarine', 'patrol boat'}
        hit_ships = {'carrier': 'hit_carrier', 'battleship': ' hit_battleship', 'destroyer': ' hit_destroyer ',
                     'submarine': ' hit_submarine ', 'patrol boat': 'hit_patrol boat'}
        value = self.get_board_cell(key)
        if value in values:
            self.set_board_cell_value(key, hit_ships[value])
            return f"hit {value}"
        elif value != 'unmarked':
            raise DomainException("Spot has already been hit.")
        else:
            self.set_board_cell_value(key, 'X')
            return "miss"

    def adding_a_ship_to_board(self, new_ship: Ship):
        self.checking_for_space(new_ship)
        new_row = new_ship.get_row
        new_column = new_ship.get_column
        if new_ship.get_orientation == "vertical":
            direction_row = 1
            direction_column = 0
        else:
            direction_row = 0
            direction_column = 1

        length = new_ship.get_length_of_ship()
        for i in range(length):
            key = f"row:{str(new_row)},column:{str(new_column)}"
            new_row = new_row + direction_row
            new_column = new_column + direction_column
            self.set_board_cell_value(key, new_ship.get_name)

    def __str__(self):
        if self._name == "player":
            return self.board_not_concealed()
        else:
            return self.board_concealed()


if __name__ == "__main__":
    b = Board("player")
    print(b)
