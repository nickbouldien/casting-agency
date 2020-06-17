import json
import unittest
from src.database.models import Actor
from src.tests.test_setup import SetupTestCase


class ActorsTestCaseDirector(SetupTestCase):
    """This class represents the actors test cases for the director role"""

    # GET '/api/actors'
    def test_get_paginated_actors(self):
        """Tests actors success"""
        response = self.client.get('/api/actors', headers=self.director_header)

        # print("self.assistant_header", self.assistant_header)
        print("self.director_header")
        # print("self.producer_header", self.producer_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that actors and total_actors both return data
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    # TODO - implement once pagination is added
    # GET '/api/actors'
    # def test_404_invalid_page(self):
    #     """Tests that the actors endpoint pagination failure results in a 404"""
    #
    #     invalid_page_number = 1000
    #
    #     response = self.client.get(f'/api/actors?page={invalid_page_number}')
    #
    #     data = json.loads(response.data)
    #
    #     # check status code and message
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['message'], 'Not found')
    #     self.assertEqual(data['success'], False)

    # GET '/api/actors/<id>/details'
    def test_actor_details_success(self):
        """Tests the actor details endpoint success"""
        actor_id = 1

        response = self.client.get(f'/api/actors/{actor_id}/details', headers=self.director_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # GET '/api/actors/<id>/details'
    def test_actor_details_404(self):
        """Tests the actor details endpoint 404"""
        actor_id = 10000

        response = self.client.get(f'/api/actors/{actor_id}/details', headers=self.director_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    # POST '/api/actors'
    def test_create_actor(self):
        """Tests that a new actor can be created"""

        # get all actors before new actor creation
        all_actors = Actor.query.all()

        response = self.client.post('/api/actors', json=self.actor, headers=self.director_header)
        data = json.loads(response.data)

        # check status code / message
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

        # get number of actors after the api call
        actors_after_creation = Actor.query.all()

        actor = Actor.query.filter_by(id=data['actor_id']).one_or_none()

        # check that the created actor is not None
        self.assertIsNotNone(actor)

        # check if the number of actors increased by one
        self.assertTrue(len(actors_after_creation) - len(all_actors) == 1)

    # POST '/api/actors'
    def test_create_actor_failure(self):
        """Tests actor creation failure"""

        # get the actors before the post request to create a new actor
        actors_prior = Actor.query.all()

        invalid_data = {}

        response = self.client.post('/api/actors', json=invalid_data, headers=self.director_header)
        data = json.loads(response.data)

        # get number of actors after api call
        actors_after_creation = Actor.query.all()

        # check status code / success message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

        # check if the number of actors before and after the failed creation are the same
        self.assertTrue(len(actors_after_creation) == len(actors_prior))

    # DELETE '/api/actors/<int:actor_id>'
    def test_delete_actor(self):
        """Tests delete an actor success"""
        actor = Actor(
            name=self.actor_2['name'],
            age=self.actor_2['age'],
            gender=self.actor_2['gender'],
            image_link=self.actor_2['imageLink'],
            phone=self.actor_2['phone'],
            website=self.actor_2['website'],
        )

        actor.insert()

        actor_id = actor.id

        # try to delete the actor
        response = self.client.delete(f'/api/actors/{actor_id}', headers=self.director_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check if the actor id matches the deleted_id field
        self.assertEqual(data['deleted_id'], actor_id)

        # check if the actor has been deleted
        a = Actor.query.filter(Actor.id == actor_id).one_or_none()

        # see if the actor is now None after it has been deleted
        self.assertEqual(a, None)

    # DELETE '/api/actors/<int:actor_id>'
    def test_delete_actor_failure(self):
        """Tests delete an actor failure"""

        random_actor_id = 200000

        # try to delete the actor
        response = self.client.delete(f'/api/actors/{random_actor_id}', headers=self.director_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    # PATCH '/api/actors/<int:actor_id>'
    def test_patch_actor_success(self):
        """Tests update an actor success"""
        actor_id = 1

        # try to update the actor
        update_data = {
            'name': "updated actor name",
            'website': "http://www.updated-website-link.com/actor"
        }

        response = self.client.patch(f'/api/actors/{actor_id}', json=update_data, headers=self.director_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that the values were updated in the database
        a = Actor.query.get(actor_id)

        self.assertEqual(a.name, update_data['name'])
        self.assertEqual(a.website, update_data['website'])

    # PATCH '/api/actors/<int:actor_id>'
    def test_patch_actor_failure(self):
        """Tests update an actor failure"""
        actor_id = 1

        # try to update the actor, but with invalid data
        update_data = {
            'age': -47
        }

        response = self.client.patch(f'/api/actors/{actor_id}', json=update_data, headers=self.director_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)

        # check that the values were not updated in the database
        a = Actor.query.get(actor_id)

        self.assertNotEqual(a.age, update_data['age'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
