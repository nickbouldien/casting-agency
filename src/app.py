# import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .database import setup_db
from .database.models import Actor, Movie


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app


APP = create_app()


@APP.route('/')
def index():
    return 'index route'


if __name__ == '__main__':
    # TODO
    APP.run()
    # APP.run(host='0.0.0.0', port=8080, debug=True)
