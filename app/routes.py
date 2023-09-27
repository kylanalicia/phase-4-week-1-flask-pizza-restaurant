
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
    restaurant_list = [
        {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        } for restaurant in restaurants
    ]
    return jsonify(restaurant_list)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({"error": "Restaurant not found"}), 404
        pizzas = RestaurantPizza.query.filter_by(restaurant_id=id)
        pizza_list = [
            {
                'id': pizza.pizza.id,
                'name': pizza.pizza.name,
                'ingredients': pizza.pizza.ingredients
            } for pizza in pizzas
        ]

        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': pizza_list
        }
        return jsonify(restaurant_data)
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({"error": "Restaurant not found"}), 404
        
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

 
# Route to retrieve all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [
        {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        } for pizza in pizzas
    ]
    return jsonify(pizza_list)

# Route to retrieve pizza details by ID
@app.route('/pizzas/<int:id>', methods=['GET'])
def get_pizza(id):
    try:
        pizza = Pizza.query.get(id)
        if not pizza:
            return jsonify({"error": "Pizza not found"}), 404
        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        })
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

 

# Route to create a new pizza
@app.route('/pizzas', methods=['POST'])
def create_pizza():
    try:
        data = request.get_json()
        name = data.get('name')
        ingredients = data.get('ingredients')
        if not name or not ingredients:
            return jsonify({"error": "Name and ingredients are required"}), 400
        pizza = Pizza(name=name, ingredients=ingredients)
        db.session.add(pizza)
        db.session.commit()

        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

 

# Route to delete a pizza by ID
@app.route('/pizzas/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    try:
        pizza = Pizza.query.get(id)
        if not pizza:
            return jsonify({"error": "Pizza not found"}), 404

        db.session.delete(pizza)
        db.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(port = 8000)
