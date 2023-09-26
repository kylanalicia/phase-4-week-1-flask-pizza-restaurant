# Import necessary modules and classes from the Flask framework.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a SQLAlchemy instance for database operations.
db = SQLAlchemy()

# Create a Migrate instance for database migrations.
migrate = Migrate()

# Define a factory function to create and configure the Flask app.
def create_app():
    # Create a Flask app instance.
    app = Flask(__name__)
    
    # Configure the app to use an SQLite database located at 'your_database.db'.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    
    # Initialize the app with the SQLAlchemy and Migrate extensions.
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app  # Return the configured Flask app instance.
