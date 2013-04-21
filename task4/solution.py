class TicTacToeBoard:

    def __init__(self):
        self.board = {"A1": " ", "A2": " ", "A3": " ",
                      "B1": " ", "B2": " ", "B3": " ",
                      "C1": " ", "C2": " ", "C3": " "}
        self.previous = None

    def __setitem__(self, coord, item):

        cell = list(self.board.keys())
        if isinstance(coord, str):
            if coord not in cell:
                raise InvalidKey

        letter = ["X", "O"]
        if item not in letter:
            raise InvalidValue

        if self.board[coord] != " ":
            raise InvalidMove

        if self.previous == item:
            raise NotYourTurn

        self.board[coord] = item
        self.previous = item

    def __getitem__(self, coord):

        return self.board[coord]

    def __str__(self):
        game_board = '\n  -------------\n' +\
                     '3 | ' + self.board['A3'] + ' | ' +\
                     self.board['B3'] + ' | ' +\
                     self.board['C3'] + ' |\n' +\
                     '  -------------\n' +\
                     '2 | ' + self.board['A2'] + ' | ' +\
                     self.board['B2'] + ' | ' +\
                     self.board['C2'] + ' |\n' +\
                     '  -------------\n' +\
                     '1 | ' + self.board['A1'] + ' | ' +\
                     self.board['B1'] + ' | ' +\
                     self.board['C1'] + ' |\n' +\
                     '  -------------\n' +\
                     '    A   B   C  \n'

        return game_board

    def check_line(self, character, s1, s2, s3):
        if (self.board[s1] == self.board[s2] == self.board[s3] == character):
            return True

    def check_all(self, character):
        # horizontal Lines
        if self.check_line(character, "A1", "A2", "A3"):
            return True
        if self.check_line(character, "B1", "B2", "B3"):
            return True
        if self.check_line(character, "C1", "C2", "C3"):
            return True

        # vertical lines
        if self.check_line(character, "A1", "B1", "C1"):
            return True
        if self.check_line(character, "A2", "B2", "C2"):
            return True
        if self.check_line(character, "A3", "B3", "C3"):
            return True

        # diagonal lines
        if self.check_line(character, "A1", "B2", "C3"):
            return True
        if self.check_line(character, "A3", "B2", "C1"):
            return True

    def game_status(self):

        if self.check_all("X") is True:
            return "X wins!"

        elif self.check_all("O") is True:
            return "O wins!"

        elif self.check_all(" ") is not True:
            return "Draw!"

        else:
            return "Game in progress."


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
