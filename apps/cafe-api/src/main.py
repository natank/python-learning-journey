import os
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///cafes.db'
)
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    
    if random_cafe:
        return jsonify(
            cafe={
                "id": random_cafe.id,
                "name": random_cafe.name,
                "map_url": random_cafe.map_url,
                "img_url": random_cafe.img_url,
                "location": random_cafe.location,
                "seats": random_cafe.seats,
                "has_toilet": random_cafe.has_toilet,
                "has_wifi": random_cafe.has_wifi,
                "has_sockets": random_cafe.has_sockets,
                "can_take_calls": random_cafe.can_take_calls,
                "coffee_price": random_cafe.coffee_price
            }
        )
    else:
        return jsonify(error="No cafes found in database"), 404


@app.route("/all")
def get_all_cafes():
    return jsonify(message="TODO: Implement GET all cafes endpoint")


@app.route("/search")
def search_cafe():
    return jsonify(message="TODO: Implement GET search cafe endpoint")


@app.route("/add", methods=["POST"])
def add_cafe():
    return jsonify(message="TODO: Implement POST add cafe endpoint")


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    return jsonify(message=f"TODO: Implement PATCH update price for cafe {cafe_id}")


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    return jsonify(message=f"TODO: Implement DELETE cafe {cafe_id}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
