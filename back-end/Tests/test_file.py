from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Outcomes
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TESTKEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        test_outcome = Outcomes(rand_number='345a',win_lose='lose',prize='no prize')
        db.session.add(test_outcome)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestBackend(TestBase):    # testing submission to the database
    def test_backend_engine(self):
        response = Outcomes.query.all()
        assert '345a' in response.text

    
    def test_backend_lose(self):    # testing the backend for output
        with requests_mock.mock() as m:    
            response = self.client.get("http://back-end:5000/prizegen")
            assert ('win' in response.data == True) or ('lose' in response.data == True)
    
    def test_backend_goldwin(self):    # testing the backend output given a gold-winning output from the two middle services
        with requests_mock.mock() as m:
            m.get("http://random_numbers:5001/rnum", text = "201")
            m.get("http://random_letters:5002/rletters", text = "e")
            response = self.client.get("http://back-end:5000/prizegen")
            self.assertIn(b'win', response.data)
            self.assertIn(b'Gold', response.data)
    
    def test_backend_silverwin(self):    # testing the backend output given a silver-winning output from the two middle services
        with requests_mock.mock() as m:
            m.get("http://random_numbers:5001/rnum", text = "207")
            m.get("http://random_letters:5002/rletters", text = "a")
            response = self.client.get("http://back-end:5000/prizegen")
            self.assertIn(b'win', response.data)
            self.assertIn(b'Silver', response.data)

    def test_backend_bronzerwin(self):    # testing the backend output given a bronze-winning output from the two middle services
        with requests_mock.mock() as m:
            m.get("http://random_numbers:5001/rnum", text = "131")
            m.get("http://random_letters:5002/rletters", text = "c")
            response = self.client.get("http://back-end:5000/prizegen")
            self.assertIn(b'win', response.data)
            self.assertIn(b'Bronze', response.data)
    
    def test_frontend_integration(self):    # testing the backend output given a losing output from the two middle services
        with requests_mock.mock() as m:
            m.get("http://random_numbers:5001/rnum", text = "500")
            m.get("http://random_letters:5002/rletters", text = "a")
            response = self.client.get("http://back-end:5000/prizegen")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'lose', response.data)

            #response1 = self.client.get("http://frontend:5003/prize-board")
            #self.assertEqual(response1.status_code, 200)
