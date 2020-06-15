from flask import Blueprint, jsonify
from .auth.auth import AuthError

errors_blueprint = Blueprint('errors', __name__)


@errors_blueprint.app_errorhandler(404)
def not_found(error_message):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@errors_blueprint.app_errorhandler(405)
def not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed.'
    }), 405


@errors_blueprint.app_errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@errors_blueprint.app_errorhandler(500)
def server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'internal server error.'
    }), 500


'''
    error handler for AuthErrors 
'''


@errors_blueprint.app_errorhandler(AuthError)
def auth_error(exception):
    print("--> auth_error error", exception.error)
    print("--> auth_error status_code", exception.status_code)

    return jsonify({
        "success": False,
        'error': exception.error,
        'status': exception.status_code
    }), exception.status_code
