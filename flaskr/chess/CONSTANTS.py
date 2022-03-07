"""
Constant values for creating standard chess board, chess pieces names
"""

FIGURE_NAMES = ["king", "queen", "bishop", "pawn", "rook", "knight"]
FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
SQUARE_NAMES = [r + f for r in FILE_NAMES for f in RANK_NAMES]
