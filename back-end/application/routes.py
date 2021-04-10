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
    
    if int(new_num) < 300 & new_let == 'a':
        new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_number,win_lose='winner',prize='Gold')
        db.session.add(new_user)
        db.session.commit()
    elif int(new_num) < 300 & new_let == 'b':
        new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_number,win_lose='winner',prize='Silver')
        db.session.add(new_user)
        db.session.commit()
    elif int(new_num) < 300 & new_let == 'c':
        new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_number,win_lose='winner',prize='Bronze')
        db.session.add(new_user)
        db.session.commit()
    else:
        new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_number,win_lose='loser',prize='nothing')
        db.session.add(new_user)
        db.session.commit()
    
    data = {"rand_number":new_number,"rand_letter":new_let,"win_lose":outcome}
    requests.post('http://frontend:5003/results', json = data)
    
    #return redirect('http://frontend:5003/')
    return jsonify({"rand_number": new_number}, {"rand_letter":new_let}, {"win_lose": outcome})
    
    
    
 
@app.route('/submit',methods=['GET','POST'])
def database_sub():
  if request.method=='POST':
      content = request.json
      new_f_name = content["new_first_name"]
      new_l_name = content['new_last_name']
      names = {"first_name":new_f_name,"last_name":new_l_name}
      jsonify(names)
      requests.post(url_for('prizegen'), json = json)
      return redirect('http://fronend:5003/prize-board')


@app.route("/prizegen", methods = ['GET','POST'])
def prizegen():
    if request.method=='POST':
        content = request.json
        new_f_name = content["new_first_name"]
        new_l_name = content['new_last_name']
      
    random_number = requests.get("http://random_numbers:5001/rnum").text
    random_letter = requests.get("http://random_letters:5002/rletters").text
    num_letter = random_number + random_letter
    if int(random_number) < 300:
        outcome = 'win'
        prize = 'Gold'
      
    elif int(random_number) < 300 & (random_letter == 'a' or random_letter == 'b'):
        outcome = 'win'
        prize = 'Silver'

    elif int(random_number) < 300 & (random_letter == 'c' or random_letter == 'd'):
        outcome = 'win'
        prize = 'Bronze'
    else:
        outcome = 'lose'
        prize = 'no prize'

    data = {"rand_number":num_letter,"win_lose":outcome,"prize":prize}
    #new_user = Users(first_name=new_f_name,last_name=new_l_name,rand_number=new_number,win_lose=outcome,prize=prize_taken)
    #db.session.add(new_entry)
    #db.session.commit()
    return jsonify(data)

    
    

