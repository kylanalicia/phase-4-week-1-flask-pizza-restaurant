from sqlalchemy import SQLalchemy

db = SQLalchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

