import json
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    all_cafes = Cafe.query.all()
    random_row = choice(all_cafes)
    cafe = {
        "can_take_calls": random_row.can_take_calls,
        "coffee_price": random_row.coffee_price,
        "has_sockets": random_row.has_sockets,
        "has_toilet": random_row.has_toilet,
        "has_wifi": random_row.has_wifi,
        "id": random_row.id,
        "img_url": random_row.img_url,
        "location": random_row.location,
        "map_url": random_row.map_url,
        "name": random_row.name,
        "seats": random_row.seats
    }
    return jsonify(cafe=cafe)

@app.route("/all", methods=["GET"])
def all():
    cafe_list = []
    all_cafes = Cafe.query.all()
    for cafe in all_cafes:
        single_cafe = {
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "id": cafe.id,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "map_url": cafe.map_url,
            "name": cafe.name,
            "seats": cafe.seats
        }
        cafe_list.append(single_cafe)
        
    return jsonify(cafes=cafe_list)

@app.route("/search", methods=["GET"])
def search():
    cafe_list = []
    location = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=location)
    print(type(cafes))
    
    for cafe in cafes:        
        single_cafe = {
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
        "has_sockets": cafe.has_sockets,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "id": cafe.id,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "map_url": cafe.map_url,
        "name": cafe.name,
        "seats": cafe.seats
        }
        cafe_list.append(single_cafe)
    
    if len(cafe_list) > 0:
        return jsonify(cafes=cafe_list)
    else:
        error_message = {
            "Not found": "Sorry, we don't have cafe in that location."
        }
        return jsonify(error=error_message)

## HTTP POST - Create Record
@app.route("/add")
def add():
    pass

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
