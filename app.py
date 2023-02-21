from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns




def create_app(config_object):
    """ Create Flask app"""
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)
    register_extensions(flask_app)
    return flask_app


def register_extensions(flask_app):
    """ Initialize DB, RESTX API and add namespaces """
    db.init_app(flask_app)
    api = Api(flask_app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(flask_app, db)


def create_data(flask_app, db):
    """ Fill the database """
    with flask_app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    app = create_app(Config())
    app.run()