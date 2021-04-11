from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_num_generator(self):
        response = self.client.get('http://random_numbers:5001/rnum')
        assert response.status_code == 200
        output = response.data 
        assert int(output) > 99 & int(output)<1001

    def test_rand_numbers(self):
        with patch('requests.get') as g:
            g.return_value.text = "500"

            response = self.client.get('http://back-end:5000/add')
            self.assertIn(b'q', response.data)
            self.assertIn(b'500', response.data)