from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Users
from os import getenv
import requests_mock



class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='MY_Passeordsa',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()

        sample_insertion = Users(first_name="Jane",last_name="Doe",rand_number='345a',win_lose='lose',prize='nothing')

        db.session.add(sample_insertion)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_view_db(self):
        response = self.client.get(url_for('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane', response.data)



class TestResponse(TestBase):
    def test_backend_logic(self):
        data = {"new_first_name":"jack", "new_last_name":"jackson", "new_email":"jj@test.com"}
        response = self.client.post(url_for('add_users'), json = data)
        
        with requests_mock.mock() as g:
            g.get('http://random_numbers:5001/rnum', text = '666')
            g.get('http://random_letters:5002/rletters', text = 'b')
            data = {"new_first_name":"jack", "new_last_name":"jackson", "new_email":"jj@test.com"}
            response = self.client.post(url_for('add_users'), json = data)
            
            self.assertEqual(200, response.status_code)


