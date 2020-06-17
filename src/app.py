from flask import Flask, jsonify
from flask_cors import CORS
from flask_moment import Moment

from .api.actor_routes import actor_blueprint
from .api.movie_routes import movie_blueprint
from .database import setup_db
from .database.config import environment
from .error_handlers import errors_blueprint


# def create_app(config_class=Config):  # TODO - check into the config for the app
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    # CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    moment = Moment(app)

    return app


APP = create_app()

# attach the routes/endpoints to the app
APP.register_blueprint(actor_blueprint)
APP.register_blueprint(movie_blueprint)

# register the custom error handlers
APP.register_blueprint(errors_blueprint)


# /ping route to check if the api is running
@APP.route('/ping', methods=['GET'])
def index():
    return jsonify({
        'success': True,
        'message': "pong"
    })


if __name__ == '__main__':
    if environment in ["development", "test"]:
        # run on port 8080 and turn on debug mode
        print(f"app.py - running in {environment} mode on port 8080")
        APP.run(host='0.0.0.0', port=8080, debug=True)
    else:
        print("app.py - running in production mode")
        APP.run()

