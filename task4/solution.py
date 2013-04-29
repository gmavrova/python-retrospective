class TicTacToeBoard:

    GAME_BOARD = '\n  -------------\n' +\
                 '3 | {A3} | {B3} | {C3} |\n' +\
                 '  -------------\n' +\
                 '2 | {A2} | {B2} | {C2} |\n' +\
                 '  -------------\n' +\
                 '1 | {A1} | {B1} | {C1} |\n' +\
                 '  -------------\n' +\
                 '    A   B   C  \n'

    WINNING_LINES = (["A1", "A2", "A3"],
                     ["B1", "B2", "B3"],
                     ["C1", "C2", "C3"],
                     ["A1", "B1", "C1"],
                     ["A2", "B2", "C2"],
                     ["A3", "B3", "C3"],
                     ["A1", "B2", "C3"],
                     ["A3", "B2", "C1"])

    COLUMN_NUMBERS = [1, 2, 3]
    ROW_LETTERS = ["A", "B", "C"]
    EMPTY = " "
    STATUS_GAME_IN_PROGRESS = "Game in progress."
    STATUS_DRAW = "Draw!"
    STATUS_X_WINS = "X wins!"
    STATUS_O_WINS = "O wins!"

    def __init__(self):
        self.coordinates = [row + str(column) for column in self.COLUMN_NUMBERS
                            for row in self.ROW_LETTERS]
        self.board = {position: self.EMPTY for position in self.coordinates}
        self.previous = None

    def __setitem__(self, index, item):
        if index not in self.board.keys():
            raise InvalidKey

        if item not in ["X", "O"]:
            raise InvalidValue

        if self.board[index] != self.EMPTY:
            raise InvalidMove

        if self.previous == item:
            raise NotYourTurn

        self.board[index] = item
        self.previous = item

    def __getitem__(self, index):
        return self.board[index]

    def __str__(self):
        return self.GAME_BOARD.format(**self.board)

    def check_line(self, character, s1, s2, s3):
        if (self.board[s1] == self.board[s2] == self.board[s3] == character):
            return True

    def check_all(self, character):
        for win_line in self.WINNING_LINES:
            check_result = self.check_line(character, *win_line)
            if check_result:
                return True

    def game_status(self):
        if self.check_all("X") is True:
            return self.STATUS_X_WINS

        elif self.check_all("O") is True:
            return self.STATUS_O_WINS

        elif self.EMPTY not in self.board.values():
            return self.STATUS_DRAW

        return self.STATUS_GAME_IN_PROGRESS


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
