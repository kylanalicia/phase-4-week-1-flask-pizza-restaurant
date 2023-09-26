# Flask Code Challenge - Pizza Restaurants
 Pizza Restaurant domain.
Your job is to build out the Flask API to add the functionality described in the deliverables below.

## Getting Started
1. Clone the repository to your local machine:
   >git clone 
   >cd 
2. Create a virtual environment:
pipenv shell

3. Install project dependencies:
pip install -r requirements.txt

4. Set up the database:
flask db init
flask db migrate
flask db upgrade

5. Seed the database with initial data:
flask seed

6. Start the Flask development server:
flask run

# Models
You have created the following database tables:
Restaurant: Represents a pizza restaurant.
Pizza: Represents a pizza.
RestaurantPizza: Represents the relationship between a restaurant and a pizza, including the price.
Validations
RestaurantPizza Model:

# Must have a price between 1 and 30.
Restaurant Model:

# Must have a name less than 50 characters in length.
Must have a unique name.
# Routes
find the routes in the routes.py

# Testing
You can test the endpoints by running the Flask server and using tools like Postman to make requests.
flask run

# contributing
You can modify the code if it has errors

# License
This project is licensed under the MIT License 