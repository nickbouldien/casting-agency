from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_moment import Moment
import json
from .database import setup_db
from .database.models import Actor, Movie


# def create_app(config_class=Config):  # TODO - check into the config for the app
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    # CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    moment = Moment(app)

    return app


APP = create_app()


@APP.route('/', methods=['GET'])
def index():
    return 'index route'


"""
    movie routes
"""


@APP.route('/api/movies', methods=['GET'])
# @requires_auth('get:movies')
def movies():
    # sample_movies = [
    #     {
    #         "id": 1,
    #         "title": "movie1"
    #     },
    #     {
    #         "id": 2,
    #         "title": "movie2"
    #     }
    # ]

    all_movies = Movie.query.order_by(Movie.release_date.desc()).all()

    print("all_movies: ", all_movies)

    return jsonify({
        "success": True,
        "movies": [m.short() for m in all_movies]
    })


@APP.route('/api/movies/<int:id>/details', methods=['GET'])
# @requires_auth('get:movies')
def movie_details(id):
    # TODO - implement
    # sample_movie = {
    #     "id": 2,
    #     "title": "movie2",
    #     "release_date": "now",  # FIXME
    #     # other fields ...
    # }

    m = Movie.query.get_or_404(id)

    print("found movie: ", m)

    return jsonify({
        "success": True,
        "movie": m.long()
    })


@APP.route('/api/movies', methods=['POST'])
# @requires_auth('post:movies')
def create_movie():
    body = request.get_json()

    req_title = body.get('title', None)
    req_release_date = body.get('releaseDate', None)

    if req_title is None:
        print('req_title is None')
        abort(422)

    if req_release_date is None:
        print('req_release_date is None')
        abort(422)

    website = body.get('website', "")
    image_link = body.get('imageLink', "")

    try:
        movie = Movie(
            title=req_title,
            release_date=req_release_date,
            image_link=image_link,
            website=website
        )
        movie.insert()
        return jsonify({
            "success": True,
            "movie_id": movie.id
        })
    except Exception as e:
        print("POST /movies error => ", e)

        return jsonify({
            'success': False,
            'message': "The movie is not formatted correctly. Please try again."
        }), 422


@APP.route('/api/movies/<int:id>', methods=["PATCH"])
# @requires_auth('patch:movies')
def update_movie(id):
    # m = Movie.query.filter(Movie.id == id).one_or_none()
    m = Movie.query.get_or_404(id)

    # if m is None:
    #     abort(404)

    try:
        # update the fields of the desired movie
        body = request.get_json()
        print("PATCH /movies: ", body)

        m.title = body.get('title', m.title)
        m.release_date = body.get('releaseDate', m.release_date)
        m.image_link = body.get('imageLink', m.image_link)
        m.website = body.get('website', m.website)

        m.update()

        return jsonify({
            "success": True,
            "movie": m.long()
        })
    except Exception as e:
        print("PATCH /movies/<id> error => ", e)
        abort(422)


@APP.route('/api/movies/<int:id>', methods=["DELETE"])
# @requires_auth('delete:movies')
def delete_movie(id):
    m = Movie.query.get_or_404(id)

    # m = Movie.query.filter(Movie.id == id).one_or_none()
    # if m is None:
    #     abort(404)

    try:
        m.delete()

        return jsonify({"success": True, "deleted_id": id})
    except Exception as e:
        print("DELETE /movies/<id> error => ", e)
        abort(500)


# @APP.route('/api/movies/search', methods=['POST'])
# # @requires_auth('get:movies')  # using the same permission as GET movies
# def search_movies():
#     search_term = request.form.get("search_term", "")  # .lower()
#
#     matching_movies = Movie.query.filter(Movie.title.ilike("%" + search_term + "%")).all()
#
#     print("matching movies: ", matching_movies)
#
#     if matching_movies is None:
#         abort(404, f"no results found for search term '{search_term}'")
#
#     return jsonify({
#         "success": True,
#         "count": len(matching_movies),
#         "data": [m.short() for m in matching_movies]
#     })


"""
    actor routes
"""


@APP.route('/api/actors', methods=['GET'])
# @requires_auth('get:actors')
def actors():
    all_actors = Actor.query.order_by(Actor.name.desc()).all()

    print("all_actors: ", all_actors)

    return jsonify({
        "success": True,
        "actors": [a.short() for a in all_actors]
    })


@APP.route('/api/actors/<int:id>/details', methods=['GET'])
# @requires_auth('get:actors')
def actor_details(id):
    a = Actor.query.get_or_404(id)

    print("found actor: ", a)

    return jsonify({
        "success": True,
        "actor": a.long()
    })


@APP.route('/api/actors', methods=['POST'])
# @requires_auth('post:actors')
def create_actor():
    body = request.get_json()

    req_name = body.get('name', None)
    req_age = body.get('age', None)
    req_gender = body.get('gender', None)

    if req_name is None:
        print('req_name is required')
        abort(422, 'req_name is required')

    if req_age is None:
        print('req_age is required')
        abort(422, 'req_age is required')
    else:
        if type(req_age) is str:
            try:
                req_age = int(req_age)
                print("req_age after casting to int: ", req_age)
            except Exception as e:
                print('req_gender error ', e)
                abort(422, 'req_age must be an integer larger than 0')
        if req_age < 0:
            abort(422, 'req_age must be an integer larger than 0')

    if req_gender is None or req_gender == "":
        print('req_gender is required')
        abort(422, "req_gender is required")

    website = body.get('website', "")
    image_link = body.get('imageLink', "")
    phone = body.get('phone', "")

    try:
        actor = Actor(
            name=req_name,
            age=req_age,
            gender=req_gender,
            image_link=image_link,
            website=website,
            phone=phone,
        )
        actor.insert()
        return jsonify({
            "success": True,
            "actor_id": actor.id
        })
    except Exception as e:
        print("POST /actors error => ", e)

        return jsonify({
            'success': False,
            'message': "The actor is not formatted correctly. Please try again."
        }), 422


@APP.route('/api/actors/<int:id>', methods=["PATCH"])
# @requires_auth('patch:actors')
def update_actor(id):
    a = Actor.query.get_or_404(id)

    try:
        # update the fields of the desired actor
        body = request.get_json()
        print("PATCH /actors: ", body)

        a.name = body.get('name', a.name)
        a.age = body.get('age', a.age)
        a.gender = body.get('gender', a.gender)
        a.image_link = body.get('imageLink', a.image_link)
        a.website = body.get('website', a.website)
        a.phone = body.get('phone', a.phone)

        a.update()

        return jsonify({
            "success": True,
            "actor": a.long()
        })
    except Exception as e:
        print("PATCH /actors/<id> error => ", e)
        abort(422)


@APP.route('/api/actors/<int:id>', methods=["DELETE"])
# @requires_auth('delete:actors')
def delete_actors(id):
    a = Actor.query.get_or_404(id)

    try:
        a.delete()

        return jsonify({"success": True, "deleted_id": id})
    except Exception as e:
        print("DELETE /actors/<id> error => ", e)
        abort(500)


# @APP.route('/api/actors/search', methods=['POST'])
# # @requires_auth('get:actors')  # using the same permission as GET actors
# def search_actors():
#     search_term = request.form.get("search_term", "")  # .lower()
#
#     matching_actors = Actor.query.filter(Actor.title.ilike("%" + search_term + "%")).all()
#
#     print("matching actors: ", matching_actors)
#
#     if matching_actors is None:
#         abort(404, f"no results found for search term '{search_term}'")
#
#     return jsonify({
#         "success": True,
#         "count": len(matching_actors),
#         "data": [a.short() for a in matching_actors]
#     })


if __name__ == '__main__':
    # TODO
    # APP.run()
    APP.run(host='0.0.0.0', port=8080, debug=True)
