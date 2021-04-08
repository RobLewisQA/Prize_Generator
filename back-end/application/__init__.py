from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:passoword@35.189.72.217/flask-db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

db = SQLAlchemy(app)

from application import routes