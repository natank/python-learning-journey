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
    
    def to_dict(self):
        """Serialize cafe object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    
    if random_cafe:
        return jsonify(cafe=random_cafe.to_dict())
    else:
        return jsonify(error="No cafes found in database"), 404


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(cafes=[]), 200


@app.route("/search")
def search_cafe():
    location = request.args.get('location')
    
    if not location:
        return jsonify(error="Missing required parameter: location"), 400
    
    cafes = db.session.query(Cafe).filter(Cafe.location.ilike(f"%{location}%")).all()
    
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error="No cafes found at that location"), 404


@app.route("/add", methods=["POST"])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(int(request.form.get("has_toilet", 0))),
            has_wifi=bool(int(request.form.get("has_wifi", 0))),
            has_sockets=bool(int(request.form.get("has_sockets", 0))),
            can_take_calls=bool(int(request.form.get("can_take_calls", 0))),
            coffee_price=request.form.get("coffee_price")
        )
        
        db.session.add(new_cafe)
        db.session.commit()
        
        return jsonify(success="Successfully added the new cafe", cafe=new_cafe.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=f"Failed to add cafe: {str(e)}"), 400


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.form.get("new_price")
    
    if not new_price:
        return jsonify(error="Missing required parameter: new_price"), 400
    
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price", cafe=cafe.to_dict()), 200
    else:
        return jsonify(error="Cafe not found"), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    
    if cafe:
        cafe_name = cafe.name
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success=f"Successfully deleted {cafe_name}"), 200
    else:
        return jsonify(error="Cafe not found"), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
