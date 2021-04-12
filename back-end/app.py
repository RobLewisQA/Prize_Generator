from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import app, db

db.create_all()

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
