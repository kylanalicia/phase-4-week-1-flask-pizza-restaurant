from flask import Flask,jsonify

from models import Restaurant, db

app = Flask(__name__)

# Define the database URI and disable tracking modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db.init_app(app)

@app.route('/')
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_data = [{"id": r.id, "name": r.name, "address": r.address} for r in restaurants]
    return jsonify(restaurant_data)

if __name__ == '__main__':
    app.run(debug=True)
