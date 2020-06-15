from flask import Flask, jsonify
from flask_cors import CORS
from flask_moment import Moment
from .database import setup_db

from .api.actor_routes import actor_blueprint
from .api.movie_routes import movie_blueprint


# def create_app(config_class=Config):  # TODO - check into the config for the app
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    # CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    moment = Moment(app)

    print(app.error_handler_spec)

    return app


APP = create_app()

# attach the routes/endpoints to the app
APP.register_blueprint(actor_blueprint)
APP.register_blueprint(movie_blueprint)


@APP.route('/', methods=['GET'])
def index():
    return jsonify({
        'success': True,
        'message': "GET - app index route"
    })


for rule in APP.url_map.iter_rules():
    print("rule: ", rule)

if __name__ == '__main__':
    # TODO
    # APP.run()
    APP.run(host='0.0.0.0', port=8080, debug=True)
