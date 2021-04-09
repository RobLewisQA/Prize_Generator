from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from application import app,db
from application import db

db.drop_all()
db.create_all()

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
