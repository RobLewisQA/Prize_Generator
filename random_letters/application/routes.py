from flask import Flask, redirect, request, url_for,render_template
from application import app
import random

@app.route('/rletters', methods=['GET'])
def rletters_generator():
    letters = ['a','b','c','d','e']
    num = random.randint(0,5)

    return f'{letters[num]}'

