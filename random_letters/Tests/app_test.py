from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_rand_letters(self):
        with patch('requests.get') as g:
            g.return_value.text = "c"
            response = self.client.get('http://back-end:5000')
            self.assertIn(b'c', response.data)

    def test_letter_generator(self):
        response = self.client.get('http://random_numbers:5002/rletters')
        assert response.status_code == 200
        output = response.data.decode('utf-8')
        assert output in ['a','b','c','d','e','v','w','x','y','z']