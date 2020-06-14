from flask import jsonify
from .app import APP


# TODO - move to the auth dir
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@APP.errorhandler(404)
def not_found(error_message):
    return jsonify({
        "success": False,
        "error": 404,
        "message": error_message if error_message else "resource not found"
    }), 404


@APP.errorhandler(405)
def not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'Method not allowed.'
    }), 405


@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@APP.errorhandler(500)
def server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal server error.'
    }), 500


'''
    error handler for AuthErrors 
'''


@APP.errorhandler(AuthError)
def auth_error(exception):
    print("--> auth_error error", exception.error)
    print("--> auth_error status_code", exception.status_code)

    return jsonify({
        "success": False,
        'error': exception.error,
        'status': exception.status_code
    }), exception.status_code
