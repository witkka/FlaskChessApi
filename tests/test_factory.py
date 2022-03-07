"""
Modules responsible for instantiating the app object.
"""
from flaskr import create_app


""" Testing configuration"""


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
