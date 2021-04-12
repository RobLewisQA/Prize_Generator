from flask import Flask, redirect, request, url_for,render_template
from application import app
import random

@app.route('/rletters', methods=['GET'])    # generating a random letter selection
def rletters_generator():
    letters = ['a','b','c','d','e','v','x','y','z']
    num = random.randint(0,4)

    return f'{letters[num]}'

