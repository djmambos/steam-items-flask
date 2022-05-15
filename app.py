from urllib import request
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {'name': 'usp-s', 'price': 12, 'quantity': 2}
    ];
    return render_template('index.html', items=items)
