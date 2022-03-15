from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_funct():
        return f"<b>{function()}</b>"
    return wrapper_funct

def make_emphases(function):
    def wrapper_funct():
        return f"<em>{function()}<em>"
    return wrapper_funct

def make_underline(function):
    def wrapper_funct():
        return f"<u>{function()}</u>"
    return wrapper_funct

@app.route('/')
def hello_world():
    return 'Napravili smo promenu... Vreme je da ovo radi sa debugerom!!!'

@app.route("/exit")
@make_bold
@make_emphases
@make_underline
def exit_site():
    return "Ovo je izlaz sa sajta. Samo da probam"

if __name__ == "__main__":
    app.run(debug=True)