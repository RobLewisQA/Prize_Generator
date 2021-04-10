from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from application import app#, db, models
#from application.models import Users
from flask_sqlalchemy import SQLAlchemy
import requests


@app.route('/')
def frontend():
    response = requests.get('http://back-end:5000').text
    return response + ' hello' #render_template('home.html', data1=data1)


@app.route('/user/add', methods=['GET','POST'])
def add_users():
    return render_template('add_user.html')
    
@app.route('/adding', methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        first_name_n = request.form['first_name']
        last_name_n = request.form['last_name']
        data = {"new_first_name":first_name_n, "new_last_name":last_name_n}
        requests.post('http://back-end:5000/add', json = data)
        return redirect('/')

# from form receipt:
# take values from form receipt and wrap in variables
# get requests for rand number and letters
# use logic to determine whether win or lose
# use logic to determine the prize
# send a post request to the backend to persist the data in a database





# @app.route('/prize_page')
# def prize_page():
#     response = requests.get('http://back-end:5000/').text
#     return response


    
# @app.route('/win', methods=['GET','POST'])
# def lottery_engine():
#     if request.method=='POST':
#         first_name_n = request.form['first_name']
#         last_name_n = request.form['last_name']
#         new_num = requests.get('http://random_numbers:5001/rnum').text
#         new_let = requests.get('http://random_letters:5002/rletters').text
#         number = str(new_num)+new_let
#         if int(new_num) < 300:
#             outcome = 'win'
#             prize = 'Gold'
        
#         elif int(new_num) < 300 & (new_let == 'a' or new_let == 'b'):
#             outcome = 'win'
#             prize = 'Silver'

#         elif int(new_num) < 300 & (new_let == 'c' or new_let == 'd'):
#             outcome = 'win'
#             prize = 'Bronze'
#         else:
#             outcome = 'lose'
#             prize = 'no prize'
        
#         data2={
#             "new_first_name": new_num,
#             "new_last_name":new_let,
#             "new_number" : number,
#             "win_lose": outcome,
#             "prize_won" : prize
#             }
#         data1 = {"new_first_name":first_name_n, "new_last_name":last_name_n, "win_lose":outcome, "prize_won": prize, "new_number":number}
#         requests.post(url_for('databse_sub'), json = data1)
    
#     return ''



@app.route('/makemeawinner', methods=['GET','POST'])
def win_form():
    return render_template('add.html')


@app.route('/form-sub', methods=['GET','POST'])
def form_sub():
    if request.method=='POST':
        first_name_n = request.form['first_name']
        last_name_n = request.form['last_name']
        data = {"new_first_name":first_name_n, "new_last_name":last_name_n}
        requests.post('http://back-end:5000/prizegen', json = data)
        return redirect('prizeboard')

@app.route("/prize-board", methods=['GET'])
def home():

    data=requests.get("http://back-end:5000/prizegen").json()
    # number = f'{submission_response["rand_number"]}'
    # letter = f'{submission_response["rand_letter"]}'
    # win_lose = f'{submission_response["win_lose"]}'
    # prize = f'{submission_response["prize"]}'
    # if win_lose == 'win':
    #     return render_template('main.html', data=prize)
    # else:
    #     return 'Try again!'
    if data["win_lose"] == 'win':
        return render_template('winner.html', data=data)
    else:
        return render_template('loser.html', data=data)
