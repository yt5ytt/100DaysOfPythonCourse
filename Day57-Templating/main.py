from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

posts = Post()

@app.route('/')
def home():
    return render_template("index.html", posts=posts.all_posts)

@app.route("/post/<int:num>")
def single_post(num):
    posts.get_post(num)
    return render_template("post.html", title=posts.title, subtitle=posts.subtitle, body=posts.body)

if __name__ == "__main__":
    app.run(debug=True)
