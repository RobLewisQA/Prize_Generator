from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_num_generator(self):    # testing that the output of the function is within the parameters
        response = self.client.get('http://random_numbers:5001/rnum')
        assert response.status_code == 200
        output = response.data 
        assert int(output) > 99 & int(output)<1001

    def test_rand_numbers(self):    # testing the response from the back-end when 500 is the output from random_numbers
        with patch('requests.get') as g:
            g.return_value.text = "500"
