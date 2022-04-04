from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, insert, select

app = Flask(__name__)
engine = create_engine(r'sqlite:///D:\__Projects\mojiProjekti\python\100DaysOfCode\Day63-VirtualBookshelf\new-books-collection.db')

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


if __name__ == "__main__":
    app.run(debug=True)

