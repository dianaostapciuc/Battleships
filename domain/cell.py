class Cell:
    def __init__(self, row: int, column: int, value: str):
        self._row = row
        self._column = column
        self._value = value

    @property
    def get_row(self):
        return self._row

    @property
    def get_column(self):
        return self._column

    @property
    def get_value(self):
        return self._value

    @get_value.setter
    def set_value(self, new_value):
        self._value = new_value

    def __str__(self):
        return self._value



if __name__ == "__main__":
    cell = Cell(2, 7, "battleship")
    print(cell)
