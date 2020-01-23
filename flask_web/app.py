# flask_web/app.py
# -*- coding: utf-8 -*- 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Team Study!!! 화이팅!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')