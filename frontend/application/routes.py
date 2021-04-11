from flask import Flask, redirect, request, url_for,render_template, Response, jsonify
from application import app#, db, models
from os import getenv
from flask_sqlalchemy import SQLAlchemy
import requests



'''
@app.route('/makemeawinner', methods=['GET','POST'])
def win_form():
    return render_template('add.html')
'''

@app.route("/prize-board", methods=['GET'])
def frontend():
    data=requests.get("http://back-end:5000/prizegen").json()
    host_name = request.host
    if data["win_lose"] == 'win':
        return render_template('winner.html', data=data) + "<br><br><br>" + print(host_name)
    else:
        return render_template('loser.html', data=data)
