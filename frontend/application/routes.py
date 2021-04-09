from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from application import app#, db, models
#from application.models import Users
from flask_sqlalchemy import SQLAlchemy
import requests


@app.route('/')
def frontend():
    response = requests.get('http://back-end:5000').text
    return response #render_template('home.html', data1=data1)

# @app.route('/results', methods = ['GET','POST'])
# def results():
#     content = request.json
#     random_number = content["rand_number"]
#     random_letter = content['rand_letter']
#     outcome = content['win_lose']
#     return str(content)

@app.route('/user/add', methods=['GET','POST'])
def add_users():
    return render_template('add_user.html')
    
@app.route('/adding', methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        first_name_n = request.form['first_name']
        last_name_n = request.form['last_name']
        email_n = request.form['email']
        data = {"new_first_name":first_name_n, "new_last_name":last_name_n, "new_email":email_n}
        requests.post('http://back-end:5000/add', json = data)
        return redirect('/')

# from form receipt:
# take values from form receipt and wrap in variables
# get requests for rand number and letters
# use logic to determine whether win or lose
# use logic to determine the prize
# send a post request to the backend to persist the data in a database








@app.route('/makemeawinner', methods=['GET','POST'])
def win_form():
    return render_template('add.html')
    
@app.route('/win', methods=['GET','POST'])
def lottery_engine():
    if request.method=='POST':
        first_name_n = request.form['first_name']
        last_name_n = request.form['last_name']
        new_num = requests.get('http://random_numbers:5001/rnum').text
        new_let = requests.get('http://random_letters:5002/rletters').text
        number = str(new_num)+new_let
        if int(new_num) < 300:
            outcome = 'win'
            prize = 'Gold'
        
        elif int(new_num) < 300 & (new_let == 'a' or new_let == 'b'):
            outcome = 'win'
            prize = 'Silver'

        elif int(new_num) < 300 & (new_let == 'c' or new_let == 'd'):
            outcome = 'win'
            prize = 'Bronze'
        else:
            outcome = 'lose'
            prize = 'no prize'
        
        data2={
            "new_first_name": new_num,
            "new_last_name":new_let,
            "new_number" : number,
            "win_lose": outcome,
            "prize_won" : prize
            }
        data1 = {"new_first_name":first_name_n, "new_last_name":last_name_n, "win_lose":outcome, "prize_won": prize, "new_number":number}
        requests.post(url_for('databse_sub'), json = data2)
        
        
        
        return {
          "rand_number": new_num,
          "rand_letter":new_let,
          "win_lose": outcome,
          "prize_won" : prize
         }
        # return jsonify({
        #   "rand_number": new_num,
        #   "rand_letter":new_let,
        #   "win_lose": outcome,
        #   "prize_won" : prize
        #  })

@app.route('/prize-board')
def prize_board():
    response = lottery_engine()
    #response = requests.get('http://back-end:5000').text
    return str(response["rand_number"])