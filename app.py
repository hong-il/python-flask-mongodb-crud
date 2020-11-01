# pip install virtualenv
# python -m pip install --upgrade pip
# conda create -n crud
# conda activate crud
# conda install flask-pymongo
"""
    @ Author    : hong-il
    @ Date      : 2020-11-01
    @ File name : app.py
    @ File path : /
    @ Description : Rendering page
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/write')
def write():
    return render_template('write.html')


if __name__ == '__main__':
    app.run()
