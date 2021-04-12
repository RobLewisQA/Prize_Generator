from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from application import app
from os import getenv
from flask_sqlalchemy import SQLAlchemy
import requests
import json


@app.route('/', methods=['GET','POST'])    # returns the homepage
def home():
    return render_template('home.html')


@app.route("/prize-board", methods=['GET'])    # returns the pages for win or lose.
def frontend():

    response = requests.get("http://back-end:5000/prizegen").json()
    data =  json.loads(response)

    if data["win_lose"] == 'win':
        return render_template('winner.html', data=data)
    else:
        return render_template('loser.html', data=data)
