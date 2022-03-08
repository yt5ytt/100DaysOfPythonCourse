from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Da li ce samo da se refreshuje ili mora da se ponovo pokrece server?'

@app.route("/exit")
def exit_site():
    return "Ovo je izlaz sa sajta. Samo da probam"

if __name__ == "__main__":
    app.run()