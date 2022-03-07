"""
FILE_NAMES, RANK_NAMES create names of fields of a standard chess board
"""
from flaskr.chess.CONSTANTS import FILE_NAMES, RANK_NAMES


class Rook:
    """
    Class containing moves of a rook figure on a standard chessboard.
    Rooks can move vertically and horizontally.
    There is no limitation of the number of fields in one move, as long as it's in one direction.
            :param field: valid current field name of this chess piece
            :type field: str
    """

    def __init__(self, field):
        self.field = field

    def get_available_moves(self):
        """
        Method returns list of available moves starting from the current field,
        :return: List
        """
        diagonal = [
            FILE_NAMES[n] + self.field[1]
            for n in range(8)
            if FILE_NAMES[n] + self.field[1] != self.field
        ]
        horizontal = [
            self.field[0] + RANK_NAMES[n]
            for n in range(8)
            if self.field[0] + RANK_NAMES[n] != self.field
        ]
        return diagonal + horizontal
