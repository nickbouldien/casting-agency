import json
import unittest
from src.database.models import Movie
from src.tests.test_setup import SetupTestCase


class MoviesTestCase(SetupTestCase):
    """This class represents the casting agency test case"""

    # GET '/api/movies'
    def test_get_paginated_movies(self):
        """Tests movies success"""
        response = self.client.get('/api/movies')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that movies and total_movies both return data
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    # TODO - implement once pagination is added
    # GET '/api/movies'
    # def test_404_invalid_page(self):
    #     """Tests that the movies endpoint pagination failure results in a 404"""
    #
    #     invalid_page_number = 1000
    #
    #     response = self.client.get(f'/api/movies?page={invalid_page_number}')
    #
    #     data = json.loads(response.data)
    #
    #     # check status code and message
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['message'], 'Not found')
    #     self.assertEqual(data['success'], False)

    # GET '/api/movies/<id>/details'
    def test_movie_details_success(self):
        """Tests the movie details endpoint success"""
        movie_id = 1

        response = self.client.get(f'/api/movies/{movie_id}/details')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # GET '/api/movies/<id>/details'
    def test_movie_details_404(self):
        """Tests the movie details endpoint 404"""
        movie_id = 10000

        response = self.client.get(f'/api/movies/{movie_id}/details')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    # POST '/api/movies'
    def test_create_movie(self):
        """Tests that a new movie can be created"""

        # get all movies before new movie creation
        all_movies = Movie.query.all()

        response = self.client.post('/api/movies', json=self.movie)
        data = json.loads(response.data)

        # check status code / message
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

        # get number of movies after the api call
        movies_after_creation = Movie.query.all()

        movie = Movie.query.filter_by(id=data['movie_id']).one_or_none()

        # check that the created movie is not None
        self.assertIsNotNone(movie)

        # check if the number of movies increased by one
        self.assertTrue(len(movies_after_creation) - len(all_movies) == 1)

    # POST '/api/movies'
    def test_create_movie_failure(self):
        """Tests movie creation failure"""

        # get number of movies before post
        movies_prior = Movie.query.all()

        invalid_data = {}

        response = self.client.post('/api/movies', json=invalid_data)
        data = json.loads(response.data)

        # get number of movies after api call
        movies_after_creation = Movie.query.all()

        # check status code / success message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

        # check if the number of movies before and after the failed creation are the same
        self.assertTrue(len(movies_after_creation) == len(movies_prior))

    # DELETE '/api/movie/<int:movie_id>'
    def test_delete_movie(self):
        """Tests delete a movie success"""

        movie = Movie(
            title=self.movie_2['title'],
            release_date=self.movie_2['releaseDate'],
            image_link=self.movie_2['imageLink'],
            website=self.movie_2['website'],
        )

        movie.insert()

        movie_id = movie.id

        # try to delete the movie
        response = self.client.delete(f'/api/movies/{movie_id}')
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check if the movie id matches the deleted_id field
        self.assertEqual(data['deleted_id'], movie_id)

        # check if the movie has been deleted
        m = Movie.query.filter(Movie.id == movie_id).one_or_none()

        # see if the movie is now None after it has been deleted
        self.assertEqual(m, None)

    # DELETE '/api/movies/<int:movie_id>'
    def test_delete_movie_failure(self):
        """Tests delete a movie failure"""

        random_movie_id = 200000

        # try to delete the movie
        response = self.client.delete(f'/api/movies/{random_movie_id}')
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 404)
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

        response = self.client.patch(f'/api/movies/{movie_id}', json=update_data)
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

        response = self.client.patch(f'/api/movies/{movie_id}', json=update_data)
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
