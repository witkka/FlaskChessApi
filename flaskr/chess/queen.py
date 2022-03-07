"""
Modules Rook and Bishop import moves of corresponding chess pieces.
"""
from flaskr.chess.rook import Rook
from flaskr.chess.bishop import Bishop


class Queen:
    """
    Queen is a chess piece that can move diagonally, vertically and horizontally in all directions.
    There is no limitation on the number of fields in one move, as long as it's in one line.
    Range of moves of this piece corresponds with combined range of bishop and rook.
    :param field: valid current field name of this chess piece
                :type field: str
                :param self.straight: moves in straight line: horizontal and vertical
                :type self.straight: list
                :param self.across: allowed diagonal moves in all directions
                :type self.across: list
    """

    def __init__(self, field):
        self.field = field
        self.straight = Rook(self.field).get_available_moves()
        self.across = Bishop(self.field).get_available_moves

    def get_available_moves(self):
        """
        Method returns a list of allowed moves from a given field.
                :return: List
        """
        return self.straight + self.across
