"""
Module imports valid square names of a standard chess board.
"""
from flaskr.chess.CONSTANTS import SQUARE_NAMES


class King:
    """
    Class containing moves of bishop figure on a standard chessboard.
            :param field: valid current field name of this chess piece
            :type field: str
    """

    def __init__(self, field):
        self.field = field

    def get_available_moves(self):
        """
        King moves one field at a time in all directions: vertical, horizontal and diagonal.
        Method returns all allowed moves of this piece starting from the current field.
                :return: List
        """
        ranges = [-1, 0, 1]
        letters = [ord(self.field[0]) + ranges[n] for n in range(3)]
        numbers = [int(self.field[1]) + ranges[n] for n in range(3)]
        return [
            chr(letter) + str(number)
            for letter in letters
            for number in numbers
            if chr(letter) + str(number) in SQUARE_NAMES and chr(letter) + str(number) != self.field
        ]
