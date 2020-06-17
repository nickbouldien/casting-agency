import json
import unittest
from src.database.models import Actor
from src.tests.test_setup import SetupTestCase


class ActorsTestCaseAssistant(SetupTestCase):
    """This class represents the actors test cases for the assistant role"""

    # GET '/api/actors'
    def test_get_paginated_actors(self):
        """Tests actors success"""
        response = self.client.get('/api/actors', headers=self.assistant_header)

        print("self.assistant_header", self.assistant_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that actors and total_actors both return data
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    # GET '/api/actors/<id>/details'
    def test_actor_details_success(self):
        """Tests the actor details endpoint success"""
        actor_id = 1

        response = self.client.get(f'/api/actors/{actor_id}/details', headers=self.assistant_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # GET '/api/actors/<id>/details'
    def test_actor_details_404(self):
        """Tests the actor details endpoint 404"""
        actor_id = 10000

        response = self.client.get(f'/api/actors/{actor_id}/details', headers=self.assistant_header)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    # POST '/api/actors'
    def test_create_actor_403(self):
        """Tests that a new actor cannot be created by an assistant"""

        response = self.client.post('/api/actors', json=self.actor, headers=self.assistant_header)
        data = json.loads(response.data)

        # check status code / message
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 403)

    # DELETE '/api/actors/<int:actor_id>'
    def test_delete_actor_403(self):
        """Tests delete an actor cannot be created by an assistant"""
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
        response = self.client.delete(f'/api/actors/{actor_id}', headers=self.assistant_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)

    # PATCH '/api/actors/<int:actor_id>'
    def test_patch_actor_403(self):
        """Tests update an actor cannot be updated by an assistant"""
        actor_id = 1

        # try to update the actor
        update_data = {
            'name': "updated actor name",
            'website': "http://www.updated-website-link.com/actor"
        }

        response = self.client.patch(f'/api/actors/{actor_id}', json=update_data, headers=self.assistant_header)
        data = json.loads(response.data)

        # check the status code / message
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
