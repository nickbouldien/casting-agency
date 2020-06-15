import json
import unittest
from flask_sqlalchemy import SQLAlchemy
from src.app import create_app
from src.database import setup_db
from src.database.models import Actor, Movie
from src.tests.test_setup import SetupTestCase


class MoviesTestCase(SetupTestCase):
    """This class represents the casting agency test case"""

    # def setUp(self):
    #     """Define test variables and initialize app."""
    #     self.app = create_app()
    #     self.client = self.app.test_client
    #     self.database_name = "casting_agency_test"
    #     self.database_path = f"postgres://localhost:5432/{self.database_name}"
    #     setup_db(self.app, self.database_path)
    #
    #     # binds the app to the current context
    #     with self.app.app_context():
    #         self.db = SQLAlchemy()
    #         self.db.init_app(self.app)
    #         # create all tables
    #         self.db.create_all()
    #
    #     # self.new_movie = {
    #     #     'question': 'Who was the first president of the US?',
    #     #     'answer': 'George Washington',
    #     # }
    #
    # def tearDown(self):
    #     """Executed after each test"""
    #     pass

    # GET '/api/movies'
    def test_get_paginated_movies(self):
        """Tests movies success"""
        response = self.client.get('/api/movies')
        print("response: ", response)

        data = json.loads(response.data)
        print("data: ", data)

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
    #     response = self.client().get(f'/api/movies?page={invalid_page_number}')
    #
    #     data = json.loads(response.data)
    #
    #     # check status code and message
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['message'], 'Not found')
    #     self.assertEqual(data['success'], False)

    # GET '/api/movies/<id>/details'
    # def test_404_invalid_page(self):
    #     """Tests the movie details endpoint success"""
    #     movie_id = 1
    #
    #     response = self.client().get(f'/api/movies/{movie_id}/details')
    #
    #     data = json.loads(response.data)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['message'], 'Not found')
    #     self.assertEqual(data['success'], False)
    #

    # # POST '/api/questions'
    # def test_create_question(self):
    #     """Tests that a new question can be created"""
    #
    #     # get number of questions before question creation
    #     num_questions = Question.query.all()
    #
    #     # create new question and load the response data
    #     response = self.client().post('/api/questions', json=self.new_question)
    #     data = json.loads(response.data)
    #
    #     # check status code / message
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)
    #
    #     # get number of questions after the api call
    #     questions_after_creation = Question.query.all()
    #
    #     question = Question.query.filter_by(id=data['id']).one_or_none()
    #
    #     # check that the created question is not None
    #     self.assertIsNotNone(question)
    #
    #     # check if the number of questions increased by one
    #     self.assertTrue(len(questions_after_creation) - len(num_questions) == 1)
    #
    # # POST '/api/questions'
    # def test_question_creation_failure(self):
    #     """Tests question creation failure"""
    #
    #     # get number of questions before post
    #     questions_prior = Question.query.all()
    #
    #     invalid_data = {}
    #
    #     response = self.client().post('/api/questions', json=invalid_data)
    #     data = json.loads(response.data)
    #
    #     # get number of questions after api call
    #     questions_after_creation = Question.query.all()
    #
    #     # check status code / success message
    #     self.assertEqual(response.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #
    #     # check if the number of questions before and after the failed creation are the same
    #     self.assertTrue(len(questions_after_creation) == len(questions_prior))
    #
    # # GET '/api/categories/<int:category_id>/questions'
    # def test_questions_for_category(self):
    #     """Tests getting questions by category"""
    #
    #     science_category_id = 1
    #
    #     response = self.client().get(f'/api/categories/{science_category_id}/questions')
    #
    #     data = json.loads(response.data)
    #
    #     # check response status code / message
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)
    #
    #     # check that current category returned is science
    #     self.assertEqual(data['current_category'], 'Science')
    #
    #     # check that the amount of questions in the returned data is not 0
    #     self.assertNotEqual(len(data['questions']), 0)
    #
    # # GET '/api/categories/<int:category_id>/questions'
    # def test_questions_for_category_failure(self):
    #     """Tests get questions by category failure"""
    #
    #     # send request with bad category id
    #     bad_category_id = 1000
    #     response = self.client().get(f'/api/categories/{bad_category_id}/questions')
    #
    #     # load response data
    #     data = json.loads(response.data)
    #
    #     # check response status code / message
    #     self.assertEqual(data['message'], 'bad request')
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #
    # # DELETE '/api/questions/<int:question_id>'
    # def test_delete_question(self):
    #     """Tests delete a question"""
    #
    #     question = Question(
    #         question=self.new_question['question'],
    #         category=self.new_question['category'],
    #         difficulty=self.new_question['difficulty'],
    #         answer=self.new_question['answer'],
    #     )
    #
    #     question.insert()
    #
    #     question_id = question.id
    #
    #     # try to delete the question
    #     response = self.client().delete(f'/api/questions/{question_id}')
    #     data = json.loads(response.data)
    #
    #     # check the status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    #     # check if the question id matches the deleted_question_id field
    #     self.assertEqual(data['deleted_question_id'], question_id)
    #
    #     # check if the question has been deleted
    #     question = Question.query.filter(Question.id == question_id).one_or_none()
    #
    #     # see if the question is now None after it has been deleted
    #     self.assertEqual(question, None)
    #
    # # DELETE '/api/questions/<int:question_id>'
    # def test_delete_question_failure(self):
    #     """Tests delete a question failure"""
    #
    #     random_question_id = 200000
    #
    #     # try to delete the question
    #     response = self.client().delete(f'/api/questions/{random_question_id}')
    #     data = json.loads(response.data)
    #
    #     # check the status code / message
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #
    # # POST '/api/questions/search'
    # def test_search_questions(self):
    #     """Tests the search questions endpoint"""
    #
    #     search_term = "autobiography"
    #
    #     # send the request with the search term
    #     response = self.client().post('/api/questions/search', json={'searchTerm': search_term})
    #     data = json.loads(response.data)
    #
    #     # check the response status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    #     # check that the number of results for the search is equal to 1
    #     self.assertEqual(len(data['questions']), 1)
    #
    #     # get the question from the response object
    #     first_question_in_response = data['questions'][0]
    #
    #     # check that id of question is correct
    #     self.assertEqual(first_question_in_response['id'], 5)
    #
    # # POST '/api/questions/search'
    # def test_search_questions_failure(self):
    #     """Tests the search questions endpoint (failure)"""
    #
    #     # test with a search term that has no results
    #     search_term = "does not exist"
    #
    #     # send the request with the search term
    #     response = self.client().post('/api/questions/search', json={'searchTerm': search_term})
    #     data = json.loads(response.data)
    #
    #     # check the response status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    #     # check that the number of results for the search is equal to 0
    #     self.assertEqual(len(data['questions']), 0)
    #
    #     # test with a search term that is None (or null/undefined from javascript)
    #     search_term = None
    #
    #     # send the request with the empty search term
    #     response = self.client().post('/api/questions/search', json={'searchTerm': search_term})
    #     data = json.loads(response.data)
    #
    #     # check the response status code / message
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #
    # # GET '/api/categories/<int:category_id>/questions'
    # def test_get_questions_by_category(self):
    #     """Tests getting questions by category"""
    #
    #     # cat id 1 is for science
    #     category_id = 1
    #
    #     # send request with the selected category id
    #     response = self.client().get(f'/api/categories/{category_id}/questions')
    #     data = json.loads(response.data)
    #
    #     # check response status code and message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    #     # check that the current category returned is science in the data object
    #     self.assertEqual(data['current_category'], 'Science')
    #
    #     # check that there are questions returned
    #     self.assertNotEqual(len(data['questions']), 0)
    #
    # # GET '/api/categories/<int:category_id>/questions'
    # def test_get_questions_by_category_failure(self):
    #     """Tests getting questions by category (failure)"""
    #
    #     # use a category id that doesn't exist
    #     category_id = 10000
    #
    #     # send request with the selected category id
    #     response = self.client().get(f'/api/categories/{category_id}/questions')
    #     data = json.loads(response.data)
    #
    #     # check response status code and message
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #
    # # POST "/api/quizzes"
    # def test_play_quiz_game(self):
    #     """Tests the quiz endpoint"""
    #
    #     science_id = 1
    #
    #     # questions with ids 21 and 22 are two other science questions
    #     json_data = {'previous_questions': [21, 22], 'quiz_category': {'type': 'Science', 'id': science_id}}
    #
    #     # send post request with category and previous questions
    #     response = self.client().post('/api/quizzes', json=json_data)
    #     data = json.loads(response.data)
    #
    #     # check response status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #
    #     # check that a question is returned
    #     self.assertIsNotNone(data['question'])
    #
    #     # check that the question returned is in the science category
    #     self.assertEqual(data['question']['category'], science_id)
    #
    #     # check that the question returned is not one of the previous questions
    #     self.assertNotEqual(data['question']['id'], 21)
    #     self.assertNotEqual(data['question']['id'], 22)
    #
    # # POST "/api/quizzes"
    # def test_play_quiz_game_failure_bad_category_id(self):
    #     """Tests the quiz endpoint failure due to a bad category id"""
    #
    #     bad_category_id = 1000000
    #
    #     # questions with ids 21 and 22 are two other science questions
    #     json_data = {'previous_questions': [21, 22], 'quiz_category': {'type': 'Science', 'id': bad_category_id}}
    #
    #     # send post request with category and previous questions
    #     response = self.client().post('/api/quizzes', json=json_data)
    #     data = json.loads(response.data)
    #
    #     # check response status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['question'], None)
    #
    # def test_play_quiz_game_failure_category_id_zero(self):
    #     """Tests the quiz endpoint responds correctly when the category id is 0"""
    #
    #     category_id = 0
    #
    #     # questions with ids 21 and 22 are two other science questions
    #     json_data = {'previous_questions': [21, 22], 'quiz_category': {'type': 'Science', 'id': category_id}}
    #
    #     # send post request with category and previous questions
    #     response = self.client().post('/api/quizzes', json=json_data)
    #     data = json.loads(response.data)
    #
    #     # check response status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['question'], None)
    #
    # # POST "/api/quizzes"
    # def test_play_quiz_game_failure_no_unused_questions(self):
    #     """Tests the quiz endpoint for the situation when there are no unused questions for a given category"""
    #
    #     science_id = 1
    #
    #     # questions with ids 20, 21, and 22 are two other science questions
    #     json_data = {'previous_questions': [20, 21, 22], 'quiz_category': {'type': 'Science', 'id': science_id}}
    #
    #     # send post request with category and previous questions
    #     response = self.client().post('/api/quizzes', json=json_data)
    #     data = json.loads(response.data)
    #
    #     # check response status code / message
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['question'], None)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
