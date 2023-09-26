from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy for database operations.
db = SQLAlchemy()

# Define the Restaurant model.
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  # Unique restaurant name.
    address = db.Column(db.String(200), nullable=False)  # Address of the restaurant.

# Define the Pizza model.
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Name of the pizza.
    ingredients = db.Column(db.String(200), nullable=False)  # List of pizza ingredients.

# Define the RestaurantPizza model.
class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)  # Price of the pizza at the restaurant.
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    
    # Define a check constraint for the price to be within the range of 1 to 30.
    price_check = db.CheckConstraint("price >= 1 AND price <= 30")

    # Define relationships between RestaurantPizza, Restaurant, and Pizza.
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas', lazy='dynamic'))
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', lazy='dynamic'))
