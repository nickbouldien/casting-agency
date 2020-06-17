import json
import unittest
from src.database.models import Movie
from src.tests.test_setup import SetupTestCase


class MoviesTestCaseDirector(SetupTestCase):
    """This class represents the movie test cases for the director role"""

    # GET '/api/movies'
    def test_get_paginated_movies(self):
        """Tests movies success"""
        response = self.client.get('/api/movies', headers=self.director_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that movies and total_movies both return data
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    # GET '/api/movies/<id>/details'
    def test_movie_details_success(self):
        """Tests the movie details endpoint success"""
        movie_id = 1

        response = self.client.get(f'/api/movies/{movie_id}/details', headers=self.director_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # GET '/api/movies/<id>/details'
    def test_movie_details_404(self):
        """Tests the movie details endpoint 404"""
        movie_id = 10000

        response = self.client.get(f'/api/movies/{movie_id}/details', headers=self.director_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    # POST '/api/movies'
    def test_create_movie_403(self):
        """Tests  a movie cannot be created by a director"""
        response = self.client.post('/api/movies', json=self.movie, headers=self.assistant_header)
        data = json.loads(response.data)

        # check status code / message
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 403)

    # DELETE '/api/movies/<int:movie_id>'
    def test_delete_movie_403(self):
        """Tests that a movie cannot be deleted by a director"""

        movie_id = 1

        # try to delete the movie
        response = self.client.delete(f'/api/movies/{movie_id}', headers=self.assistant_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)

    # PATCH '/api/movies/<int:movie_id>'
    def test_patch_movie_success(self):
        """Tests update a movie success"""

        movie_id = 1

        # try to update the movie
        update_data = {
            'title': "updated movie title",
            'website': "http://www.updated-website-link.com"
        }

        response = self.client.patch(f'/api/movies/{movie_id}', json=update_data, headers=self.director_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that the values were updated in the database
        m = Movie.query.get(movie_id)

        self.assertEqual(m.title, update_data['title'])
        self.assertEqual(m.website, update_data['website'])

    # PATCH '/api/movies/<int:movie_id>'
    def test_patch_movie_failure(self):
        """Tests update a movie failure"""

        movie_id = 1

        # try to update the movie, but with invalid data
        update_data = {
            'releaseDate': "invalid date"
        }

        response = self.client.patch(f'/api/movies/{movie_id}', json=update_data, headers=self.director_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

        # check that the values were not updated in the database
        m = Movie.query.get(movie_id)

        self.assertNotEqual(m.release_date, update_data['releaseDate'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
