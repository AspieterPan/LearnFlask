import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calculations.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Calculation(db.Model):
    id: Mapped[int] = db.Column(Integer, primary_key=True)
    expression: Mapped[str] = db.Column(String(255), nullable=False)
    result: Mapped[str] = db.Column(Float, nullable=False)

    def __repr__(self):
        return f"<Calculation {self.expression} = {self.result}>"


with app.app_context():
    db.create_all()

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


@app.route("/calculator_advanced", methods=["GET", "POST"])
def calcu_advanced():
    if request.method == "POST":
        expression = request.form.get("expression")
        result = eval(expression)  # Caution: Using eval() like this can be dangerous.
        new_calculation = Calculation(expression=expression, result=result)
        db.session.add(new_calculation)
        db.session.commit()
        return redirect(url_for("calcu_advanced"))
    calculations = db.session.execute(db.select(Calculation)).scalars()
    return render_template("calcu_advanced.html", calculations=calculations)


if __name__ == "__main__":
    app.run(host=host, port=8080)
