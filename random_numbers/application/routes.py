from flask import Flask, redirect, request, url_for,render_template
from application import app
import random

@app.route('/rnum', methods=['GET'])
def rnum_generator():
    num = random.randint(100,999)
    return f'{num}'

