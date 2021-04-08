from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from application import app
import random

#@app.route('/rnum', methods=['GET'])
#def rnum_generator():
#    num = random.randint(100,999)
#    return 'hello' #f'{num}'

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)

