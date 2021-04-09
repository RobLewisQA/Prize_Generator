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


@app.route('/add',methods=['GET','POST'])
def add_users():
    if request.method=='POST':
      content = request.json
      new_f_name = content["new_first_name"]
      new_l_name = content['new_last_name']
      new_eml = content['new_email']
      new_num = requests.get('http://random_numbers:5001/rnum').text
      new_let = requests.get('http://random_letters:5002/rletters').text
      new_number = str(new_num)+new_let
      
      if int(new_num) < 300:
        new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_eml,win_lose=new_number,prize='winner')
        db.session.add(new_user)
        db.session.commit()
        outcome = 'win'
      else:
        new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_eml,win_lose=new_number,prize='loser')
        db.session.add(new_user)
        db.session.commit()
        outcome='lose'
      
      data = {"rand_number":new_number,"rand_letter":new_let,"win_lose":outcome}
      requests.post('http://frontend:5003/results', json = data)
      
      return redirect('http://frontend:5003/')
    #else:
    #  return jsonify({
    #      "rand_number": new_number,
    #      "rand_letter":new_let,
     #     "win_lose": outcome
     ##   })


@app.route('/submit',methods=['GET','POST'])
def database_sub():
  if request.method=='POST':
    content = request.data
    new_f_name = content["new_first_name"]
    new_l_name = content['new_last_name']
    outcome = content['win_lose']
    prize = content['prize_won']
    new_number = content['new_number']
    new_user = Users(first_name=new_f_name,last_name=new_l_name,random_number=outcome,win_lose=new_number,prize=prize)
    db.session.add(new_user)
    db.session.commit()

    return ''

    
    

