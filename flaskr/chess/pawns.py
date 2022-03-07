class Pawn:
    """
    Class containing moves of a pawn figure on a standard chessboard.
    Pawns can move one field vertically in the direction of the opponent.
    In this script there is no distinguishing between white and black pawns.
    Bishop moves diagonally in straight lines in all directions and there is no limit on the number of fields in one
    move.
            :param field: valid current field name of this chess piece
            :type field: str
    """

    def __init__(self, field):
        self.field = field

    def get_available_moves(self):
        """
        Method returns two-element list of two moves a pawn can make, first move assuming it's a white chess figure,
        second assuming it's a black figure.
        :return: List
        """
        return [
            self.field[0] + str(int(self.field[1]) + n)
            for n in range(-1, 2, 2)
            if 0 < int(self.field[1]) + n < 9
        ]
