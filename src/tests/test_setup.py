import unittest
from flask_sqlalchemy import SQLAlchemy
from src.app import create_app
from src.database import setup_db
import json

from .config import assistant_header, director_header, producer_header
from ..error_handlers import errors_blueprint
from ..api.actor_routes import actor_blueprint
from ..api.movie_routes import movie_blueprint


class SetupTestCase(unittest.TestCase):
    """This class represents the base/setup test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()

        self.client = self.app.test_client()

        self.app.testing = True
        self.app.config['TESTING'] = True

        setup_db(self.app)

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

        self.actor = {
            'name': 'monica santana',
            'age': 34,
            'gender': "F",
            'imageLink': "https://www.example.com/monica/image",
            'phone': "123456789",
            'website': "https://www.example.com/monica"
        }

        self.actor_2 = {
            'name': 'joe rodriguez',
            'age': 39,
            'gender': "M",
            'imageLink': "https://www.example.com/joe/image",
            'phone': "987654321",
            'website': "https://www.example.com/joe"
        }

        self.assistant_header = assistant_header
        self.director_header = director_header
        self.producer_header = producer_header

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
