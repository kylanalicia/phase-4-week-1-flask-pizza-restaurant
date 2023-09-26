from sqlite3 import IntegrityError
from flask import Flask,jsonify, request

from models import Pizza, Restaurant, RestaurantPizza, db

app = Flask(__name__)

# Define the database URI and disable tracking modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_data = [{"id": r.id, "name": r.name, "address": r.address} for r in restaurants]
    return jsonify(restaurant_data)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in restaurant.pizzas]
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": pizzas
        }
        return jsonify(restaurant_data)
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404
    
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_data = [{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas]
    return jsonify(pizza_data)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    try:
        new_restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        return jsonify(pizza_data)
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400

if __name__ == '__main__':
    app.run(port = 8000)
