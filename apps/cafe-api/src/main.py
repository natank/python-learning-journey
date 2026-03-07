import os
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from flasgger import Swagger

app = Flask(__name__)

# Swagger configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Cafe API",
        "description": "RESTful API for managing cafe information for remote workers",
        "version": "1.0.0",
        "contact": {
            "name": "Cafe API Team"
        }
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": ["http"],
    "tags": [
        {"name": "cafes", "description": "Cafe operations"}
    ]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

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
    """
    Get a random cafe
    ---
    tags:
      - cafes
    responses:
      200:
        description: A random cafe from the database
        schema:
          type: object
          properties:
            cafe:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Science Gallery Cafe"
                map_url:
                  type: string
                  example: "https://goo.gl/maps/RhkutvkRE1p"
                img_url:
                  type: string
                  example: "https://example.com/image.jpg"
                location:
                  type: string
                  example: "Pearse St, Dublin 2"
                seats:
                  type: string
                  example: "50-100"
                has_toilet:
                  type: boolean
                  example: true
                has_wifi:
                  type: boolean
                  example: true
                has_sockets:
                  type: boolean
                  example: true
                can_take_calls:
                  type: boolean
                  example: true
                coffee_price:
                  type: string
                  example: "€3.50"
      404:
        description: No cafes found in database
        schema:
          type: object
          properties:
            error:
              type: string
              example: "No cafes found in database"
    """
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    
    if random_cafe:
        return jsonify(cafe=random_cafe.to_dict())
    else:
        return jsonify(error="No cafes found in database"), 404


@app.route("/all")
def get_all_cafes():
    """
    Get all cafes
    ---
    tags:
      - cafes
    responses:
      200:
        description: List of all cafes in the database
        schema:
          type: object
          properties:
            cafes:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  map_url:
                    type: string
                  img_url:
                    type: string
                  location:
                    type: string
                  seats:
                    type: string
                  has_toilet:
                    type: boolean
                  has_wifi:
                    type: boolean
                  has_sockets:
                    type: boolean
                  can_take_calls:
                    type: boolean
                  coffee_price:
                    type: string
    """
    all_cafes = db.session.query(Cafe).all()
    
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(cafes=[]), 200


@app.route("/search")
def search_cafe():
    """
    Search cafes by location
    ---
    tags:
      - cafes
    parameters:
      - name: location
        in: query
        type: string
        required: true
        description: Location to search for (case-insensitive partial match)
        example: "Dublin 2"
    responses:
      200:
        description: List of cafes matching the location
        schema:
          type: object
          properties:
            cafes:
              type: array
              items:
                type: object
      400:
        description: Missing location parameter
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Missing required parameter: location"
      404:
        description: No cafes found at that location
        schema:
          type: object
          properties:
            error:
              type: string
              example: "No cafes found at that location"
    """
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
    """
    Add a new cafe
    ---
    tags:
      - cafes
    consumes:
      - application/x-www-form-urlencoded
    parameters:
      - name: name
        in: formData
        type: string
        required: true
        description: Cafe name (must be unique)
        example: "New Cafe"
      - name: map_url
        in: formData
        type: string
        required: true
        description: Google Maps URL
        example: "https://goo.gl/maps/example"
      - name: img_url
        in: formData
        type: string
        required: true
        description: Image URL
        example: "https://example.com/image.jpg"
      - name: location
        in: formData
        type: string
        required: true
        description: Location description
        example: "Main St, Dublin 1"
      - name: seats
        in: formData
        type: string
        required: true
        description: Seating capacity
        example: "20-30"
      - name: has_toilet
        in: formData
        type: integer
        required: true
        description: Has toilet (1 or 0)
        example: 1
      - name: has_wifi
        in: formData
        type: integer
        required: true
        description: Has WiFi (1 or 0)
        example: 1
      - name: has_sockets
        in: formData
        type: integer
        required: true
        description: Has power sockets (1 or 0)
        example: 1
      - name: can_take_calls
        in: formData
        type: integer
        required: true
        description: Can take calls (1 or 0)
        example: 0
      - name: coffee_price
        in: formData
        type: string
        required: false
        description: Coffee price
        example: "€3.50"
    responses:
      201:
        description: Cafe successfully created
        schema:
          type: object
          properties:
            success:
              type: string
              example: "Successfully added the new cafe"
            cafe:
              type: object
      400:
        description: Failed to add cafe (validation error or duplicate name)
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Failed to add cafe: duplicate key value"
    """
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
    """
    Update cafe coffee price
    ---
    tags:
      - cafes
    consumes:
      - application/x-www-form-urlencoded
    parameters:
      - name: cafe_id
        in: path
        type: integer
        required: true
        description: ID of the cafe to update
        example: 1
      - name: new_price
        in: formData
        type: string
        required: true
        description: New coffee price
        example: "€4.00"
    responses:
      200:
        description: Price successfully updated
        schema:
          type: object
          properties:
            success:
              type: string
              example: "Successfully updated the price"
            cafe:
              type: object
      400:
        description: Missing new_price parameter
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Missing required parameter: new_price"
      404:
        description: Cafe not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Cafe not found"
    """
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
    """
    Delete a cafe (report as closed)
    ---
    tags:
      - cafes
    parameters:
      - name: cafe_id
        in: path
        type: integer
        required: true
        description: ID of the cafe to delete
        example: 5
    responses:
      200:
        description: Cafe successfully deleted
        schema:
          type: object
          properties:
            success:
              type: string
              example: "Successfully deleted Science Gallery Cafe"
      404:
        description: Cafe not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Cafe not found"
    """
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
