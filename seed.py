from app import app, db
from app.models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    # Create sample restaurants
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    # Create sample pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Add restaurants and pizzas to the database
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()

    # Create and add RestaurantPizza entries
    rp1 = RestaurantPizza(price=12.99, restaurant=restaurant1, pizza=pizza1)
    rp2 = RestaurantPizza(price=15.99, restaurant=restaurant1, pizza=pizza2)
    rp3 = RestaurantPizza(price=10.99, restaurant=restaurant2, pizza=pizza1)

    db.session.add(rp1)
    db.session.add(rp2)
    db.session.add(rp3)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_database()
        print("Database seeded successfully.")
