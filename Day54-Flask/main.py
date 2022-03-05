from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Da li ce samo da se refreshuje ili mora da se ponovo pokrece server?'