from flask import Flask,request,render_template,redirect
import sqlite3
import os

class Review(object):
    def __init__(self,name,review):
        self.name = name
        self.review = review

DATA_PATH = "/database"

if os.path.exists(DATA_PATH) == False:
    os.mkdir(DATA_PATH)

app = Flask(__name__)

def init_tables():

    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS REVIEWS (name TEXT NOT NULL, review TEXT NOT NULL)"
    conn = sqlite3.connect(os.path.join(DATA_PATH,"reviews.db"))
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE)
    conn.commit()
    conn.close()

init_tables()

def add_review(name,review):

    ADD_REVIEW = "INSERT INTO REVIEWS (name,review) VALUES (?,?)"
    conn = sqlite3.connect(os.path.join(DATA_PATH,"reviews.db"))
    cursor = conn.cursor()
    conn.execute(ADD_REVIEW,(name,review))
    conn.commit()
    conn.close()

def load_reviews():

    reviews = []

    LOAD_REVIEW = "SELECT * from REVIEWS"
    conn = sqlite3.connect(os.path.join(DATA_PATH,"reviews.db"))
    cursor = conn.cursor()
    results = conn.execute(LOAD_REVIEW)

    for row in results:
        reviews.append(Review(row[0],row[1]))
    return reviews

@app.route("/",methods=["POST","GET"])
def index():

    if request.method == "POST":
        name = request.form["name"]
        review = request.form["review"]

        add_review(name,review)

        return redirect("/reviews")

    return render_template("index.html")

@app.route("/reviews",methods=["GET"])
def reviews():

    reviews = load_reviews()

    return render_template("reviews.html",reviews=reviews)

app.run(host="0.0.0.0",port=5000)
