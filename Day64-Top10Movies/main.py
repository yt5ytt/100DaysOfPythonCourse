import ast
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from classes.db import Db
from classes.forms import UpdateForm, AddMovieForm
from classes.api_engine import MovieFinder

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

db = Db()
db.create_movie_table()
db.metadata.create_all(db.engine)


@app.route("/")
def home():
    all_movies = db.get_movie_row()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        movies = MovieFinder(title)
        return render_template("select.html", movies=movies.data)
    else:
        return render_template("add.html", form=form)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = UpdateForm()
    title = request.args.get("title")
    if form.validate_on_submit():
        # rating = form.rating.data
        review = form.review.data
        title = request.form["title"]
        db.update_movie(review=review, title=title)
        return redirect(url_for('home'))
    return render_template("edit.html", title=title, form=form)


@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")
    db.delete_movie(movie_id)
    return redirect(url_for('home'))


@app.route("/select", methods=["GET", "POST"])
def select():
    if request.method == "GET":
        movie = request.args.get("movie")
        movie = ast.literal_eval(movie)
        year = movie["release_date"].split("-")[0]
        db.insert_movie(
            title=movie["title"],
            year=year,
            rating=float(movie["vote_average"]),
            description=movie["overview"],
            img_url=movie["poster_path"]
        )
        return redirect(url_for('edit', title=movie["title"]))
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)
