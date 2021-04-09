from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

class TestBase(TestCase):
    def create_app(self):
        return app


# frontend
# class TestResponse(TestBase):
#     def test_backend_logic(self):
#         with patch('requests.post') as p:
#             p.return_value.text = 'test'

#             data = {"new_first_name":"jack", "new_last_name":"jackson", "new_email":"jj@test.com"}
#             response = self.client.post(url_for('add_user'), data = data)
            
#             self.assertEqual(200, response.status_code)
