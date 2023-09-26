# Import necessary modules and classes from your Flask application.
from app import create_app, db
from flask_migrate import Migrate
from app.models import Restaurant, Pizza, RestaurantPizza

# Create a Flask app instance using the create_app() function.
app = create_app()

# Initialize the Migrate extension with your Flask app and database.
migrate = Migrate(app, db)

# This section of code will run only if this script is executed directly (not imported as a module).
if __name__ == '__main__':
    # Start the Flask development server with debugging enabled.
    app.run(debug=True)
