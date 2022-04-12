from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, insert, select, update

DB_PATH = "sqlite:////home/yt5ytt/Projects/python/100DaysOfPythonCourse/Day63-VirtualBookshelf/new-books-collection.db"

app = Flask(__name__)
engine = create_engine(DB_PATH)

metadata_obj = MetaData()

books_table = Table(
    "books",
    metadata_obj,
    Column("id", Integer, primary_key=True, unique=True),
    Column("title", String(length=250), unique=True),
    Column("author", String(length=250)),
    Column("rating", Float())
)

metadata_obj.create_all(engine)


@app.route('/')
def home():
    all_books = []
    select_all = select(books_table)
    with engine.connect() as conn:
        result = conn.execute(select_all)
        for row in result:
            all_books.append(row)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with engine.connect() as db:
            book = request.form["book_name"]
            author = request.form["author"]
            rating = float(request.form["rating"])
            stmt = insert(books_table).values(title=book, author=author, rating=rating)
            db.execute(stmt)
        return redirect(location="/")
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if "id" in request.args:
        item_id = request.args.get("id")
        select_book = select(books_table).where(books_table.c.id == item_id)
        with engine.connect() as conn:
            result = conn.execute(select_book)
            for book in result:
                book_id = book.id
                title = book.title
                author = book.author
                book_rating = book.rating
        return render_template("edit.html", id=book_id, title=title, author=author, rating=book_rating)
    elif request.method == "POST":
        rating = request.form["rating"]
        item_id = request.form["id"]
        update_data = update(books_table).where(books_table.c.id == item_id).values(rating=rating)
        with engine.connect() as conn:
            conn.execute(update_data)
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
