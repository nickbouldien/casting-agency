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

        # for rule in self.app.url_map.iter_rules():
        #     print("rule: ", rule)

        # binds the app to the current context
        # ctx = self.app.app_context()
        # ctx.push()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # basic setup for use in other tests
        # self.new_movie = {
        #     'question': 'Who was the first president of the US?',
        #     'answer': 'George Washington',
        # }

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
