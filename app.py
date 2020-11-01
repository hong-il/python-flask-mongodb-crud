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
from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/crud"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/write', methods=["GET", "POST"])
def write():
    if request.method == "POST":
        PST_CAT_TP = request.form.get("PST_CAT_TP")
        PST_TITLE = request.form.get("PST_TITLE")
        PST_SUB_TITLE = request.form.get("PST_SUB_TITLE")
        PST_CATEGORY = request.form.get("PST_CATEGORY")
        PST_CAT_TXT = request.form.get("PST_CAT_TXT")
        PST_CONTENT = request.form.get("PST_CONTENT")

        PST_MST = mongo.db.post
        post = {
            "PST_CAT_TP": PST_CAT_TP,
            "PST_TITLE": PST_TITLE,
            "PST_SUB_TITLE": PST_SUB_TITLE,
            "PST_CATEGORY": PST_CAT_TXT if PST_CATEGORY == 0 else PST_CATEGORY,
            "PST_CONTENT": PST_CONTENT
        }

        PST_MST.insert_one(post)

        return render_template('index.html')
    else:
        return render_template('write.html')



