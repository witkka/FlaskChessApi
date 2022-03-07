"""
SECRET_KEY is imported from instances folder that will not be included in the github repo
"""
import os

from flask import Flask

from flaskr.api import v1


def create_app(test_config=None):
    """
    Method creates app object based on given parameters and configuration.
    The argument that this method takes indicates the name of the configuration script and the class from which the
    configuration data should be loaded.

    Registers blueprint for the api part of application.
    A blueprint is a package that encapsulates one specific piece of functionality.
        :param test_config: app  configuration
        :return: application object
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(v1)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
