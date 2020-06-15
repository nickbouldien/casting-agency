from flask import Blueprint, request, abort, jsonify

from ..database.models import Actor
from ..utils import check_valid_age

actor_blueprint = Blueprint('actor_blueprint', __name__)


"""
    actor routes
"""


@actor_blueprint.route('/api/actors', methods=['GET'])
# @requires_auth('get:actors')
def actors():
    all_actors = Actor.query.order_by(Actor.name.desc()).all()

    actors_array = [a.short() for a in all_actors]

    return jsonify({
        "success": True,
        "actors": actors_array,
        "total_actors": len(actors_array),
    })


@actor_blueprint.route('/api/actors/<int:id>/details', methods=['GET'])
# @requires_auth('get:actors')
def actor_details(id):
    a = Actor.query.get_or_404(id)

    print("found actor: ", a)

    return jsonify({
        "success": True,
        "actor": a.long()
    })


@actor_blueprint.route('/api/actors', methods=['POST'])
# @requires_auth('post:actors')
def create_actor():
    body = request.get_json()

    req_name = body.get('name', None)
    req_age = body.get('age', None)
    req_gender = body.get('gender', None)

    if req_name is None:
        print('req_name is required')
        abort(422, 'req_name is required')

    valid_age = check_valid_age(req_age)
    if not valid_age:
        abort(422, 'age must be an integer larger than 0')

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


@actor_blueprint.route('/api/actors/<int:id>', methods=["PATCH"])
# @requires_auth('patch:actors')
def update_actor(id):
    a = Actor.query.get_or_404(id)

    try:
        # update the fields of the desired actor
        body = request.get_json()
        print("PATCH /actors: ", body)

        req_age = body.get('age', a.age)

        valid_age = check_valid_age(req_age)
        if not valid_age:
            abort(422, 'age must be an integer larger than 0')

        a.name = body.get('name', a.name)
        a.age = req_age
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


@actor_blueprint.route('/api/actors/<int:id>', methods=["DELETE"])
# @requires_auth('delete:actors')
def delete_actors(id):
    a = Actor.query.get_or_404(id)

    try:
        a.delete()

        return jsonify({"success": True, "deleted_id": id})
    except Exception as e:
        print("DELETE /actors/<id> error => ", e)
        abort(500)


# @actor_blueprint.route('/api/actors/search', methods=['POST'])
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
