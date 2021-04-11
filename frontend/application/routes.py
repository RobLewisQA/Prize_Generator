from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from application import app, db, models
from application.models import Outcomes


@app.route('/', methods=['GET','POST'])    # returns the homepage
def home():
    return render_template('home.html')


@app.route("/prize-board", methods=['GET'])    #
def frontend():
    random_number = requests.get("http://random_numbers:5001/rnum").text
    random_letter = requests.get("http://random_letters:5002/rletters").text

    data = requests.get("http://back-end:5000/prizegen").json()
    
    new_entry = Outcomes(rand_number=data["rand_number"],win_lose=data["win_lose"],prize=data["prize"])    # add new record to database
    db.session.add(new_entry)
    db.session.commit()
    

    if data["win_lose"] == 'win':
        return render_template('winner.html', data=data)
    else:
        return render_template('loser.html', data=data)
