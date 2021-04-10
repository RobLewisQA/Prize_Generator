from application import db 
from flask_sqlalchemy import SQLAlchemy

class Outcomes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	rand_number = db.Column(db.String(150), nullable=False, unique=True)
	win_lose = db.Column(db.String(150), nullable=False)
	prize = db.Column(db.String(150), nullable=False)
