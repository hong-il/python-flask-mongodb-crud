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
    @ Description : Rendering, request page
"""
from flask import Flask, render_template, request, abort, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
import time

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/crud"
mongo = PyMongo(app)


@app.template_filter("datetime_format")
def datetime_format(value):
    if value is None:
        return ""

    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    value = datetime.fromtimestamp((int(value) / 1000)) + offset
    return value.strftime("%B %d, %Y")


@app.route('/')
def index():
    # Page value (If value is null, default value is 1)
    page = request.args.get("page", default=1, type=1)
    # Posts in a page
    limit = request.args.get("limit", 7, type=1)
    PST_MST = mongo.db.post
    # Skip prev posts and get limited posts
    posts = PST_MST.find({}).skip((page - 1) * limit).limit(limit)
    return render_template('index.html', posts=posts)


@app.route('/write', methods=["GET", "POST"])
def write():
    if request.method == "POST":
        PST_CAT_TP = request.form.get("PST_CAT_TP")
        PST_TITLE = request.form.get("PST_TITLE")
        PST_SUB_TITLE = request.form.get("PST_SUB_TITLE")
        PST_CATEGORY = request.form.get("PST_CATEGORY")
        PST_CAT_TXT = request.form.get("PST_CAT_TXT")
        PST_CONTENT = request.form.get("PST_CONTENT")

        PST_CREATED_DATE = round(datetime.utcnow().timestamp() * 1000)
        PST_MST = mongo.db.post
        insert_post = {
            "PST_CAT_TP": PST_CAT_TP,
            "PST_TITLE": PST_TITLE,
            "PST_SUB_TITLE": PST_SUB_TITLE,
            "PST_CATEGORY": PST_CAT_TXT if PST_CATEGORY == 0 else PST_CATEGORY,
            "PST_CONTENT": PST_CONTENT,
            "PST_CREATED_DATE": PST_CREATED_DATE
        }

        insertedPost = PST_MST.insert_one(insert_post)
        inserted_id = str(insertedPost.inserted_id)

        return redirect(url_for("post", PST_ID=inserted_id))
    else:
        return render_template("write.html")


@app.route('/post/<PST_ID>')
def post(PST_ID):
    # PST_ID = request.args.get("PST_ID")
    if PST_ID is not None:
        PST_MST = mongo.db.post
        data = PST_MST.find_one({"_id": ObjectId(PST_ID)})

        if data is not None:
            select_post = {
                "PST_ID": data.get("_id"),
                "PST_CAT_TP": data.get("PST_CAT_TP"),
                "PST_TITLE": data.get("PST_TITLE"),
                "PST_SUB_TITLE": data.get("PST_SUB_TITLE"),
                "PST_CATEGORY": data.get("PST_CATEGORY"),
                "PST_CONTENT": data.get("PST_CONTENT"),
                "PST_CREATED_DATE": data.get("PST_CREATED_DATE")
            }

            return render_template("post.html", post=select_post)
    return abort(404)
