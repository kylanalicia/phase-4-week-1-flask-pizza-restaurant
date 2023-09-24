from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Correct import statement

db = SQLAlchemy()

# Create Flask application instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phase-4-week-1-flask-pizza-restaurant.db'

def create_app():
    from app import routes  # Import routes here
    return app

# Create the app instance using create_app
app = create_app()
