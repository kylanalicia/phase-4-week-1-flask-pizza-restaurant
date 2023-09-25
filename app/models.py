from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
   
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
  
class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    
    # Define the check constraint for price
    price_check = db.CheckConstraint("price >= 1 AND price <= 30")

    # Define the relationship between RestaurantPizza, Restaurant, and Pizza
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas', lazy='dynamic'))
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', lazy='dynamic'))
