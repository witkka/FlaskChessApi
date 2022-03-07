from flaskr.chess.CONSTANTS import FIGURE_NAMES, SQUARE_NAMES, FILE_NAMES


""" Testing response of the list_available_moves function 
test status codes"""


def test_list_available_moves_valid_input_returns_code_200(client):
    for n in range(6):
        response = client.get(f"/api/v1/{FIGURE_NAMES[n]}/{SQUARE_NAMES[n]}")
        assert response.status_code == 200


def test_list_available_moves_invalid_figure_returns_code_404(client):
    for n in range(6):
        response = client.get(f"/api/v1/{FIGURE_NAMES[n][:-1]}/h5")
        assert response.status_code == 404


def test_list_available_moves_invalid_field_number_returns_code_409(client):
    for n in range(5):
        response = client.get(f"/api/v1/bishop/h5{n}")
        assert response.status_code == 409


def test_list_available_moves_invalid_field_letter_returns_code_409(client):
    for n in range(5):
        response = client.get(f"/api/v1/bishop/h{FILE_NAMES[n]}5")
        assert response.status_code == 409


""" Testing messages for all figures """


def test_list_available_moves_returns_correct_message(client, test_data):
    for figure in FIGURE_NAMES:
        data = test_data.get(figure)
        for d in data:
            response = client.get(f'/api/v1/{figure}/{d.get("current_field")}')
            message = {
                "availableMoves": sorted(d.get("available_moves")),
                "error": None,
                "figure": figure,
                "currentField": d.get("current_field"),
            }
            assert response.get_json() == message
