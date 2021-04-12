from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from application import app#, db, models
from os import getenv
from flask_sqlalchemy import SQLAlchemy
import requests
import json


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')


<<<<<<< HEAD
@app.route("/prize-board", methods=['GET'])    # returns the pages for win or lose.
def frontend():

    data = requests.get("http://back-end:5000/prizegenerator").json()
    #data =  json.loads(response)

=======
@app.route("/prize-board", methods=['GET'])
def frontend():
    data=requests.get("http://back-end:5000/prizegen").json()
    host_name = request.host
>>>>>>> parent of 4d6ce8c... frontend/application complete
    if data["win_lose"] == 'win':
        return render_template('winner.html', data=data)
    else:
        return render_template('loser.html', data=data)
