from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_rand_numbers(self):
        with patch('requests.get') as g:
            g.return_value.text = "jim"
            response = self.client.get('http://frontend:5003')
            self.assertIn(b'jim', response.data)