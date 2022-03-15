from flask import Flask
from random import randint
import const

if const.number == "":
    random_number = randint(0, 9)
    const.number = int(random_number)
    print(const.number)

app = Flask(__name__)

@app.route("/")
def home_page():
    return const.HOMEPAGE

@app.route("/<int:number>")
def guessed_number(number):
    if number < random_number:
        return const.LOWER_NUMBER
    elif number > random_number:
        return const.HIGHER_NUMBER
    else:
        const.number = ""
        return const.MATCH_NUMBER

if __name__ == "__main__":
    app.run(debug=True)