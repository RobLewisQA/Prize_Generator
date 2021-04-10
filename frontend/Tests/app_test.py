from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from flask import Flask, redirect, request, url_for,render_template


class TestBase(TestCase):
    def create_app(self):
        return app

 class TestResponse(TestBase):

#     def test_num_generator(self):
#         response = self.client.get('http://frontend:5003/')
#         assert response.status_code == 200
#         output = response.data 
#         assertIn() 
    def test_backend_config(self):
        with requests_mock.mock() as m:
            m.get("http://back-end:5000/prizegen", text = '{"prize":"no prize","rand_number":"401e","win_lose":"lose"}')
            response = self.client.get(url_for('frontend'))
            assert response.status_code == 200
            self.assertIn(b'lose', response.data)
            self.assertIn(b'no prize', response.data)