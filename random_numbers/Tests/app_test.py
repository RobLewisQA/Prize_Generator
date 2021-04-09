from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_num_generator(self):
        response = self.client.get('http://random_numbers:5001/rnum')
        assert response.status_code == 200
        output = response.data 
        assert int(output) > 99 & int(output)<1001

    def test_num_generator(self):
        response = self.client.get('http://random_numbers:5001/rnum')
        assert response.status_code == 200
        output = response.data 
        assert int(output) > 99 & int(output)<1001

    def test_rand_numbers(self):
        # with patch('requests.get') as g:
        #     g.return_value.text = "700"
        
        # response = self.client.get('http://back-end:5000/')
        # assert response.status_code == 200
        # #self.assertIn(b'700', response.data)
