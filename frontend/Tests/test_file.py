from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app
from flask import Flask, redirect, request, url_for,render_template
import requests_mock


class TestBase(TestCase):
    def create_app(self):    # returning an instance of the frontend app for testing
        return app

class TestResponse(TestBase):

    def test_frontend_lose(self):    # testing the frotnend output given a losing output from the backend
        with requests_mock.mock() as m:
            m.get("http://back-end:5000/prizegen", text = '{"prize":"no prize","rand_number":"901e","win_lose":"lose"}')
            response = self.client.get(url_for('frontend'))
            assert response.status_code == 200
            self.assertIn(b'lost', response.data)

    def test_frontend_win(self):    # testing the frotnend output given a silver winning output from the backend
        with requests_mock.mock() as m:
            m.get("http://back-end:5000/prizegen", text = '{"prize":"Silver","rand_number":"105c","win_lose":"win"}')
            response = self.client.get(url_for('frontend'))
            # assert response.status_code == 200
            self.assertIn(b'Congratulations', response.data)
            self.assertIn(b'Silver', response.data)

    def test_frontend_home(self):    # testing frotnend
        response = self.client.get('http://frontend:5003/')
        assert response.status_code == 200