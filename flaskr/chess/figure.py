"""
Modules Pawn, King, Rook, Bishop, Queen, Knight contain all available moves of this chess piece that can be made
starting from the current_field.

"""
from flaskr.chess.pawns import Pawn
from flaskr.chess.king import King
from flaskr.chess.rook import Rook
from flaskr.chess.bishop import Bishop
from flaskr.chess.queen import Queen
from flaskr.chess.knight import Knight


class Figure:
    """
    Class containing all allowed moves of certain chess piece standing on current field.
    :param chess_piece: name of chess piece
    :type chess_piece: str
    :param current_field: name of current field
    :type current_field: str
    """

    def __init__(self, chess_piece, current_field):
        self.chess_piece = chess_piece
        self.current_field = current_field

    @property
    def list_available_moves(self):
        """
        Method returning list of al available moves of a given chess piece from a given field.
                :return: List
        """
        if self.chess_piece == "pawn":
            return Pawn(self.current_field).get_available_moves()
        if self.chess_piece == "king":
            return King(self.current_field).get_available_moves()
        if self.chess_piece == "rook":
            return sorted(Rook(self.current_field).get_available_moves())
        if self.chess_piece == "bishop":
            return sorted(Bishop(self.current_field).get_available_moves)
        if self.chess_piece == "queen":
            return sorted(Queen(self.current_field).get_available_moves())
        if self.chess_piece == "knight":
            return sorted(Knight(self.current_field).get_available_moves())

    def validate_move(self, dest_field):
        """
        Method checks if given dest_field is in a list of valid moves of a given figure standing on current_field.
                :param dest_field: str
                :return: bool
        """
        if dest_field in self.list_available_moves:
            return True
        return False
