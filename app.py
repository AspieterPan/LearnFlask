import os
from flask import Flask, render_template

app = Flask(__name__)

# init config
if os.getenv("APP_ENV") == "prod":
    app.debug = True
else:
    app.debug = False


# route
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


if __name__ == "__main__":
    app.run(port=8080)
