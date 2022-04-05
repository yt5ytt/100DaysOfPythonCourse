from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from sqlalchemy import Table, Column, String, select, update, insert, create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# DB_PATH = "sqlite://///home/yt5ytt/Projects/python/100DaysOfPythonCourse/Day64-Top10Movies/movie_list.db"

# engine = create_engine(DB_PATH)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
