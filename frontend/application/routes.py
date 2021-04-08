from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from application import app#, db, models
#from application.models import Users
from flask_sqlalchemy import SQLAlchemy
import requests
import pandas as pd



@app.route('/')
def frontend():
    response = requests.get('http://back-end:5000').text
    return response #render_template('home.html', data1=data1)

# @app.route('/results')
# def results():
#     df = pd.read_html(requests.get('http://back-end:5000').text)
#     df1 = df.sort_values(by='id', ascending=False).head(1)
#     return pd.to_html(df1)
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

#@app.route('/posted', methods=['GET','POST'])
#def rletters_generator():
#    first_name_n = request.form['first_name']
#    last_name_n = request.form['last_name']
#    email_n = request.form['email']
#    return f'{first_name_n}+{last_name_n} + {email_n} '

