from flask import Flask, render_template
from fake_posts import FakePosts

app = Flask(__name__)
blog = FakePosts()

@app.route("/")
def home():
    return render_template("index.html", posts=blog.data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:num>")
def single_post(num):
    for blog_post in blog.data:
        if blog_post["id"] == num:
            image = "{{ url_for('static', filename='assets/img/post-bg.jpg')}}"
            return render_template("post.html", post=blog_post, image=image)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
