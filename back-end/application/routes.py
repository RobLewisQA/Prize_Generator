from flask import Flask, redirect, request, url_for,render_template,jsonify
from application import app, db, models
from application.models import Outcomes
from flask_sqlalchemy import SQLAlchemy
import requests


@app.route("/prizegen", methods = ['GET'])    
def prizegen():
    random_number = requests.get("http://random_numbers:5001/rnum").text
    random_letter = requests.get("http://random_letters:5002/rletters").text

    num_letter = random_number + random_letter    # request both service outputs & concatenate them

    if (int(random_number) < 200) & (random_letter == 'e'):    # logic to determine if win or lose and prize
        outcome = 'win'
        prize = 'Gold'
    elif (int(random_number) < 300) & (random_letter == 'a' or random_letter == 'b'):
        outcome = 'win'
        prize = 'Silver'
    elif (int(random_number) < 400) & (random_letter == 'c' or random_letter == 'd'):
        outcome = 'win'
        prize = 'Cheese'
    else:
        outcome = 'lose'
        prize = 'no prize'
    
    data = {"rand_number":num_letter,"win_lose":outcome,"prize":prize}
    
    new_entry = Outcomes(rand_number=num_letter,win_lose=outcome,prize=prize)    # add new record to database
    db.session.add(new_entry)
    db.session.commit()

    return jsonify(data)
