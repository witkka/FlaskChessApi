from flaskr.chess.CONSTANTS import FIGURE_NAMES, SQUARE_NAMES


""" Testing response code for valid/invalid moves"""


def test_validate_move_invalid_figure_name_returns_code_404(client):
    for n in range(6):
        response = client.get(
            f"/api/v1/{FIGURE_NAMES[n][:-1]}/{SQUARE_NAMES[n]}/{SQUARE_NAMES[::-1][n]}"
        )
        assert response.status_code == 404


def test_validate_move_valid_input_returns_code_200(client):
    for n in range(6):
        response = client.get(
            f"/api/v1/{FIGURE_NAMES[n]}/{SQUARE_NAMES[n]}/{SQUARE_NAMES[::-1][n]}"
        )
        assert response.status_code == 200


def test_validate_move_invalid_field_number_returns_code_409(client):
    for n in range(5):
        response = client.get(
            f"/api/v1/{FIGURE_NAMES[n]}/{SQUARE_NAMES[n]}{n}/{SQUARE_NAMES[::-1][n]}"
        )
        assert response.status_code == 409


""" Testing message for valid/invalid moves"""


def test_validate_move_valid_input_returns_message_valid_move(client, test_data):
    for n in range(5):
        data = test_data.get(FIGURE_NAMES[n])
        for d in data:
            chess_figure = FIGURE_NAMES[n]
            current_field = d.get("current_field")
            dest_field = d.get("available_moves")[0]

            response = client.get(
                f"/api/v1/{chess_figure}/{current_field}/{dest_field}"
            )
            message = {
                "move": "valid",
                "figure": chess_figure,
                "error": None,
                "currentField": current_field,
                "destField": dest_field,
            }
            assert response.get_json() == message


def test_validate_move_valid_input_returns_message_invalid_move(client, test_data):
    for n in range(5):
        data = test_data.get(FIGURE_NAMES[n])
        for d in data:
            chess_figure = FIGURE_NAMES[n]
            current_field = d.get("current_field")
            dest_field = f"{current_field}{n}"

            response = client.get(
                f"/api/v1/{chess_figure}/{current_field}/{dest_field}"
            )
            message = {
                "move": "invalid",
                "figure": chess_figure,
                "error": None,
                "currentField": current_field,
                "destField": dest_field,
            }
            assert response.get_json() == message
