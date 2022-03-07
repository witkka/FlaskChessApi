"""
FILE_NAMES, RANK_NAMES create names of fields of a standard chess board
"""
from flaskr.chess.CONSTANTS import FILE_NAMES, RANK_NAMES


class Bishop:
    """
    Class containing moves of bishop figure on a standard chessboard.
    Bishop moves diagonally in straight lines in all directions and there is no limit on the number of fields in one
    move.
            :param field: valid current field name of this chess piece
            :type field: str
            :param self.letter_range: based on FILE_NAMES of the standard chess board, list of letters from letter 'a'
            until current_field and current_field+1 until letter 'h.
            :type letter_range: list
            :param self.number_range: based on RANK_NAMES of the standard chess board, list of numbers from number '1'
            until current_field and current_field+1 until number '8'.
            :type number_range: list
    """

    def __init__(self, field):
        self.field = field
        self.letter_range = "".join(FILE_NAMES).split(self.field[0])
        self.number_range = "".join(RANK_NAMES).split(self.field[1])

    @property
    def get_left_down(self):
        """
        Returns list of moves in the left-down-direction.
                :return: List
        """
        return [
            a + b
            for a, b in zip(self.letter_range[0][::-1], self.number_range[0][::-1])
        ]

    @property
    def get_left_up(self):
        """
        Returns list of moves in the left-up-direction.
                :return: List
        """
        return [a + b for a, b in zip(self.letter_range[0][::-1], self.number_range[1])]

    @property
    def get_right_up(self):
        """
        Returns list of moves in the right-up-direction
                :return: List
        """
        return [a + b for a, b in zip(self.letter_range[1], self.number_range[1])]

    @property
    def get_right_down(self):
        """
        Returns list of moves in the right-down-direction
                :return: List
        """
        return [a + b for a, b in zip(self.letter_range[1], self.number_range[0][::-1])]

    @property
    def get_available_moves(self):
        """
        Method collects all moves in all directions
                :return:List
        """
        moves = (
            self.get_left_down
            + self.get_right_up
            + self.get_left_up
            + self.get_right_down
        )
        return moves
