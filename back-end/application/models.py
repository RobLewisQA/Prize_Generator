from application import db 
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	rand_number = db.Column(db.String(150), nullable=False, unique=True)
	win_lose = db.Column(db.String(150), nullable=False)
	prize = db.Column(db.String(150), nullable=False)
