import unittest
from flask_sqlalchemy import SQLAlchemy
from src.app import create_app
from src.database import setup_db
import json

from ..error_handlers import errors_blueprint
from ..api.actor_routes import actor_blueprint
from ..api.movie_routes import movie_blueprint


class SetupTestCase(unittest.TestCase):
    """This class represents the base/setup test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()

        # register the routes/endpoints and error handlers
        self.app.register_blueprint(actor_blueprint)
        self.app.register_blueprint(movie_blueprint)
        self.app.register_blueprint(errors_blueprint)

        self.client = self.app.test_client()

        # TODO - which config settings are needed for testing??
        self.app.testing = True
        self.app.config['TESTING'] = True

        setup_db(self.app)

        # binds the app to the current context
        # ctx = self.app.app_context()
        # ctx.push()

        # basic setup for use in other tests
        self.movie = {
            'title': 'star wars',
            'releaseDate': '1977-05-25T21:45:23Z',
            'imageLink': "https://www.example.com/starwars/image",
            'website': "https://www.example.com/starwars"
        }

        self.movie_2 = {
            'title': 'star wars episode 5',
            'releaseDate': '1980-05-17T21:45:23Z',
            'imageLink': "https://www.example.com/starwars2/image",
            'website': "https://www.example.com/starwars2"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_setup_sanity_check(self):
        """sanity check making sure the test setup is successful"""
        self.assertEqual(2, 2)

        self.assertTrue(True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
