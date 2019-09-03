from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

    return """<h1>Hello From Flask</h1>
    <h2> Version Three of Dockerland </h2>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)