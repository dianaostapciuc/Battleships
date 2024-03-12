from random import randint, choice

class Ship:

    def __init__(self, name: str, row: int, column:int, orientation: str):
        self._name = name
        self._row = row
        self._column = column
        self._orientation = orientation

    @property
    def get_name(self):
        return self._name

    @property
    def get_row(self):
        return self._row

    @property
    def get_column(self):
        return self._column

    @property
    def get_orientation(self):
        return self._orientation

    def get_length_of_ship (self):
        values_based_on_ship_types = {'carrier':5, 'battleship':4, 'destroyer':3, 'submarine':3, 'patrol boat':2}
        return values_based_on_ship_types[self._name]

    def __str__(self):
        return self._name + " " + str(self._row) + " " + str(self._column) + " " + self._orientation

    def generate_ship (self):
        self._row = randint(1,10)
        self._column = randint(1,10)
        self._orientation = choice(["horizontally", "vertically"])


if __name__ == "__main__":
    ship = Ship("battleship", 2, 3, "down")
    print(ship)
