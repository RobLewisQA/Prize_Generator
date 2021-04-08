from flask import Flask, redirect, request, url_for,render_template,jsonify
from application import app, db, models
from application.models import Users
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import requests


@app.route('/')
def hello():
  data1 = Users.query.all()
  return render_template('home.html', data1=data1)


# @app.route('/users/add', methods=['GET','POST'])
# def add_user():
#     requests.get('http://frontend:5003/posted').text
#     return render_template('add_user.html')

@app.route('/added', methods=['GET'])
def receive_data():
  #new_data = requests.get('http://frontend:5003/form').text
  return requests.get('http://frontend:5003/form').text

@app.route('/add',methods=['GET','POST'])
def add_users():
    if request.method=='POST':
      content = request.json
      #response = requests.get('http://frontend:5003/posted').text
      new_f_name = content["new_first_name"]#response.split(" ")[0]
      new_l_name = content['new_last_name']#response.split(" ")[1]
      new_eml = content['new_email']#response.split(" ")[2]
      new_num = requests.get('http://random_numbers:5001/rnum').text
      new_let = requests.get('http://random_letters:5002/rletters').text
      new_number = str(new_num)+new_let
      if int(new_num) < 300:
        new_user = Users(first_name=new_f_name,last_name=new_l_name,email=new_eml,rand_number=new_number,win_lose='winner')
        db.session.add(new_user)
        db.session.commit()
        outcome = 'win'
      
      else:
        new_user = Users(first_name=new_f_name,last_name=new_l_name,email=new_eml,rand_number=new_number,win_lose='loser')
        db.session.add(new_user)
        db.session.commit()
        outcome='lose'
        #data = Users.query.
      #return redirect('http://frontend:5003/home')
      return jsonify({
        "rand_number": new_number,
        "rand_letter":new_let,
        "win_lose": outcome
      })

