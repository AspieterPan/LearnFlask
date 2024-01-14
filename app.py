import os
from flask import Flask, render_template

app = Flask(__name__)

# init config
if os.getenv("APP_ENV") == "prod":
    app.debug = False
    host = "0.0.0.0"
else:
    app.debug = True
    host = "127.0.0.1"


# route
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


if __name__ == "__main__":
    app.run(host = host, port=8080)
