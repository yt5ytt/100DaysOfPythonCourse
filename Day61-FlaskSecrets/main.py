from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import Login

EMAIL = "admin@email.com"
PASS = "12345678"


app = Flask(__name__)
Bootstrap(app)

app.secret_key = "SomeRandomKey"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    email = None
    password = None
    form = Login()
    if form.validate_on_submit():
        if form.email.data == EMAIL and form.password.data == PASS:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", email=email, password=password, form=form)


if __name__ == '__main__':
    app.run(debug=True)