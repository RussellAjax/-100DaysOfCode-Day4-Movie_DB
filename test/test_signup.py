import unittest
import json

from app import app
from database.db import db

#SignupTest class extends unittest.TestCase
#TestCase provides us with powerful methods such as SetUp and tearDown
class SignupTest(unittest.TestCase):

    #setUp() method runs each time before running each method
    #defined on the SignupTest class. setUp() as the name
    #suggests this method is used to set up our test infrastracture before
    #running the test
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    #test_successful_signup() is the method that is actually testing the
    #Signup feautre. Here we have defined a payload which should be a JSON value
    #And we send a POST request to /api/auth/signup
    def test_successful_signup(self):
        #Given
        payload = json.dumps({
            'email' : 'paurakh011@gmail.com',
            'password': 'mycoolpassword'
            })

        #When
        response = self.app.post('/api/auth/signup', headers={'Content-Type:' 'application/json'}, data=payload)

        #Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    #After each test methods, the tearDown() method runs each time
    #This method is responsible for clearing our infrastructure setup
    #This includes deleting our database collection for test isolation.
    def tearDown(self):
        #Delete Database collection after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
