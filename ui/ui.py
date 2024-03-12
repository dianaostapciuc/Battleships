from services.services import Services

from domain.ship import Ship

from random import choice, randint

from ui.ui_exception import UIException
from repository.repo_exception import RepositoryException
from domain.domain_exception import DomainException


class UI:

    def __init__(self):
        self._services = Services()
        self._player_hits = 0
        self._computer_hits = 0
        self._computer_next_moves = []

    def reading_the_players_board(self):
        ship_types = {5: 'carrier', 4: 'battleship', 3: 'destroyer', 2: 'submarine', 1: 'patrol boat'}
        for i in range(1, 6):
            variable = 0
            while variable == 0:
                try:
                    print("The coordinates for the ship are: ")
                    row = input("The row: ")
                    self.validating_the_input(row)
                    column = input("The column: ")
                    self.validating_the_input(column)
                    orientation = input("orientation (v for vertical and h for horizontal): ")
                    orientation = self.validate_input_orientation(orientation)
                    code = ship_types[i]
                    new_ship = Ship(code, int(row), int(column), orientation)
                    self._services.adding_a_ship("player", new_ship)
                except UIException:
                    print("There was an UI error.")
                except DomainException:
                    print("There was a domain error.")
                except RepositoryException:
                    print("There was a repository error.")
                else:
                    variable = 1

    def starting_the_game(self):
        self.reading_the_players_board()
        self._services.generating_board()
        print(self._services)

    def playing_the_game(self):
        print("-----------------------------")
        print("The player, as it lacks AI, gets to start.")
        choice = "player"

        while self._player_hits < 17 and self._computer_hits < 17:
            print(f"{choice}'s turn.")
            if choice == "player":
                self.the_player_is_attacking()
                choice = "computer"
            else:
                self.the_computer_is_attacking()
                choice = "player"
            if choice == "player":
                print("---------------------------------------------------------------------------------------")
                print(self._services)
                print("---------------------------------------------------------------------------------------")
        if self._player_hits == 17:
            print("Congrats, you won!!")
        else:
            print("You lost... upsetting a computer beat you.")

    def the_player_is_attacking(self):
        variable = 0
        while variable == 0:
            try:
                print("How are you attacking? ")
                row = input("The row: ")
                self.validating_the_input(row)
                column = input("The column: ")
                self.validating_the_input(column)
                result = self._services.attacking_a_cell("computer", int(row), int(column))
            except UIException:
                print("There was an UI error.")
            except DomainException:
                print("There was a domain error.")
            except RepositoryException:
                print("There was a repository error.")
            else:
                variable = 1
                if result != "miss":
                    self._player_hits += 1
                print(result)

    def the_computer_is_attacking(self):
        variable = 0
        while variable == 0:
            try:
                computer_move = self.generating_the_computer_move()
                row = computer_move[0]
                column = computer_move[1]
                print(f"Computer's move is: row {str(row)}, column {str(column)}")
                outcome = self._services.attacking_a_cell("player", int(row), int(column))
            except UIException:
                print("There was an UI error.")
            except DomainException:
                print("There was a domain error.")
            except RepositoryException:
                print("There was a repository error.")
            else:
                variable = 1
                if outcome != "miss":
                    self._computer_hits += 1
                    self.adding_the_next_move(row, column)
                print(outcome)

    def generating_the_computer_move(self):
        if len(self._computer_next_moves) != 0:
            check = len(self._computer_next_moves) - 1
            computer_move = self._computer_next_moves[check]
            row = computer_move[0]
            column = computer_move[1]
            self._computer_next_moves.pop(check)
            return [row, column]
        else:
            row = randint(1, 10)
            column = randint(1, 10)
        return [row, column]

    def checking_if_move_is_valid(self, row, column):
        if row > 10 or row < 1 or column > 10 or column < 1:
            return False
        return True

    def adding_the_next_move(self, row, column):
        direction_row = [-1, 0, 1, 0]
        direction_column = [0, 1, 0, -1]
        for i in range(4):
            new_row = row + direction_row[i]
            new_column = column + direction_column[i]
            if self.checking_if_move_is_valid(new_row, new_column) == True and self.checking_if_move_is_valid(
                    -1 * new_row, -1 * new_column) == True:
                if self._services.getting_player_boards_value(row, column) == self._services.getting_player_boards_value(new_row, new_column):
                    self._computer_next_moves.append([-1 * new_row, -1 * new_column])
        for i in range(4):
            new_row = row + direction_row[i]
            new_column = column + direction_column[i]
            if self.checking_if_move_is_valid(new_row, new_column):
                self._computer_next_moves.append([new_row, new_column])

    def validating_the_input(self, coordinate):
        if len(coordinate) > 1 and coordinate != '10':
            raise UIException("Invalid input.")
        if coordinate > "9" or coordinate < "1":
            raise UIException("Invalid input.")

    def validate_input_orientation(self, given_orientation):
        orientation = {"v": "vertical", 'h': "horizontal"}
        if given_orientation not in ["v", "h"]:
            raise UIException("Bad orientation.")
        return orientation[given_orientation]
