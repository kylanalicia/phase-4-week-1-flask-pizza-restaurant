# Import necessary modules and classes from your Flask application.
from app import create_app
from app.models import db, Restaurant, Pizza, RestaurantPizza
from random import choice as rc
from faker import Faker

# Create a Flask app instance using the create_app() factory function.
app = create_app()

# Create a Faker instance for generating fake data.
fake = Faker()

# Create and seed your database
with app.app_context():
    # Create database tables
    db.create_all()

    # Create Restaurant instances
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    # Create Pizza instances
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Create RestaurantPizza instances
    restaurant_pizza1 = RestaurantPizza(price=15.0, restaurant_id=1, pizza_id=1)
    restaurant_pizza2 = RestaurantPizza(price=20.0, restaurant_id=1, pizza_id=2)

    # Add objects to the session and commit changes to the database
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.commit()

# Print a success message after seeding the database.
print("Database seeded successfully.")
