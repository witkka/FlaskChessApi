"""
Module Figure contains methods for computing list of available moves for a given figure, standing on a given field and
move validation.
FIGURE_NAMES are the names of standard chess figures.
SQUARE_NAMES are the names of fields in a standard chess board.
"""

from flask import Blueprint, jsonify, make_response
from werkzeug.exceptions import abort

from flaskr.chess.figure import Figure
from flaskr.chess.CONSTANTS import FIGURE_NAMES, SQUARE_NAMES


def clean_input_field(field):
    """
    Method returns false if input is invalid.
    It also switches places of the digit and letter if input parameters are inverted.
    It input is valid, it returns its value.
        :param field: string
        :return: bool, string
    """
    if len(field) == 2:
        f = field.lower()
        if f in SQUARE_NAMES:
            return f
        elif f[1] + f[0] in SQUARE_NAMES:
            return f[1] + f[0]
    return False


"""
Assigning the 'v1' blueprint.
"""
v1 = Blueprint("chess", __name__, url_prefix="/api/v1")


class CustomException(Exception):
    """
    Class for handling custom exception when figure is not in standard chess pieces names.
     Receives figure name, field name that this figure is standing on and status code 409.
    Returns json message with collected data.
    """

    def __init__(self, figure, field_name, status_code):
        Exception.__init__(self)
        self.field_name = field_name
        self.status_code = status_code
        self.message = jsonify(
            {
                "availableMoves": [],
                "error": "Field does not exist.",
                "figure": figure,
                "currentField": field_name,
            }
        )


@v1.errorhandler(CustomException)
def handle_custom(error):
    """
    Method for handling 409 error when chess piece is not found in the FIGURE_NAMES.
        :param error: raised by custom exception
        :return: response with error status and message about error
    """
    return make_response(error.message, error.status_code)


@v1.errorhandler(500)
def server_error(error):
    """
    Method for handling sever errors, status code 500.
        :param error:
        :return: response
    """
    return error


@v1.route("<string:chess_figure>/<string:current_field>", methods=["GET"])
def list_available_moves(chess_figure, current_field):
    """
    Method returns list of available valid moves for given figure, standing on a given field or an empty list when there
    are no valid moves. returned json includes information about error, figure name, and current field.
    Raises error 409 when figure is not a valid figure name.
    Raises 404 error when current_field is not a valid chess square name.

        :param chess_figure: figure name
        :type chess_figure: str
        :param current_field: name of the field that given figure is standing on
        :type current_field: str
        :return: List
    """
    if chess_figure.lower() not in FIGURE_NAMES:
        abort(404)

    if not clean_input_field(current_field):
        status_code = 409
        raise CustomException(chess_figure, current_field, status_code)
    else:
        message = {
            "availableMoves": Figure(chess_figure, current_field).list_available_moves,
            "error": None,
            "figure": chess_figure,
            "currentField": current_field.upper(),
        }
        return make_response(jsonify(message), 200)


@v1.route(
    "<string:chess_figure>/<string:current_field>/<string:dest_field>", methods=["GET"]
)
def validate_move(chess_figure, current_field, dest_field):
    """
    Returns information if given move on the list of valid moves for chess figure standing in current field.
        :param chess_figure: figure name
        :type chess_figure: str
        :param current_field: name of the field that given figure is standing on
        :type current_field: str
        :param dest_field: name of the field that the figure is supposed to move to
        :type dest_field: str
        :return: bool
    """
    if chess_figure.lower() not in FIGURE_NAMES:
        abort(404)

    if not clean_input_field(current_field):
        status_code = 409
        raise CustomException(chess_figure, current_field, status_code)
    else:
        if Figure(chess_figure, current_field).validate_move(dest_field):
            move = "valid"
        else:
            move = "invalid"

    message = {
        "move": move,
        "figure": chess_figure,
        "error": None,
        "currentField": current_field.upper(),
        "destField": dest_field.upper(),
    }
    return jsonify(message), 200
