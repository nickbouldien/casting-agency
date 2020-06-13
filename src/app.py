from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from .database import setup_db
from .database.models import Actor, Movie


def create_app(test_config=None):
    app = Flask(__name__)
    # setup_db(app)
    # CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app


APP = create_app()


@APP.route('/', methods=['GET'])
def index():
    return 'index route'


@APP.route('/api/movies', methods=['GET'])
def movies():
    sample_movies = [
        {
            "id": 1,
            "title": "movie1"
        },
        {
            "id": 2,
            "title": "movie2"
        }
    ]

    # TODO - implement
    # all_movies = Movie.query.all()
    # print("all_movies: ", all_movies)

    # ms = [m.short() for m in all_movies]

    return jsonify({
        "success": True,
        "movies": sample_movies
    })


@APP.route('/api/movies', methods=['POST'])
# @requires_auth('post:drinks')
def create_movie(payload):
    # TODO - implement
    body = request.get_json()

    req_title = body.get('title', None)
    req_release_date = body.get('releaseDate', None)

    if req_title is None:
        print('req_title is None')
        abort(422)

    if req_release_date is None:
        print('req_release_date is None')
        abort(422)

    try:
        movie = Movie(title=req_title, release_date=req_release_date)
        movie.insert()
        return jsonify({
            "success": True,
            "movies": movie
        })
    except Exception as e:
        print("POST /movies error => ", e)

        return jsonify({
            'success': False,
            'message': "The movie is not formatted correctly. Please try again."
        })


@APP.route('/api/movies/<int:id>', methods=["PATCH"])
# @requires_auth('patch:movies')
def update_movie(payload, id):
    # TODO - use the normal query (get_or_404 ??)
    m = Movie.query.filter(Movie.id == id).one_or_none()

    if m is None:
        abort(404)

    try:
        # update the fields of the desired movie
        body = request.get_json()
        print("PATCH /movies: ", body)

        m.title = body.get('title', m.title)

        # TODO
        # m.update()

        return jsonify({
            "success": True,
            "movies": [],
            # "movies": [m.long()]
        })
    except Exception as e:
        print("PATCH /movies/<id> error => ", e)

        abort(422)


@APP.route('/api/movies/<int:id>', methods=["DELETE"])
# @requires_auth('delete:movies')
def delete_drink(payload, id):
    m = Movie.query.filter(Movie.id == id).one_or_none()

    if m is None:
        abort(404)

    try:
        m.delete()

        return jsonify({"success": True, "delete_id": id})
    except Exception as e:
        print("error: could not delete the movie => ", e)

        abort(500)


if __name__ == '__main__':
    # TODO
    # APP.run()
    APP.run(host='0.0.0.0', port=8080, debug=True)
