"""
Modules import pytest library for testing purposes and create_app to create app version reusable across tests.
"""
import pytest
from flaskr import create_app
import json
import os


@pytest.fixture
def client():
    """
    Method creates app "version" configured for testing purposes.
    This client fixture will be called by each individual test.
    It gives a simple interface to the application, where  test requests to the application can be triggered.
    During setup, the TESTING config flag is activated which disables error catching during request handling.
    """
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_data():
    """
    Method creates fixture which enables using test data from the json file across all tests.
    """
    script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
    rel_path = "figure_moves.json"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as m:
        return json.load(m)
