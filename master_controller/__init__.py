# https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way
from flask_api import FlaskAPI
# from instance.config import app_config


# db =  MongoClient('localhost', 27017).master_controller


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    # app.config.config_from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    return app
