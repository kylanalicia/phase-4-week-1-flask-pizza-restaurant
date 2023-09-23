from flask import Flask
from sqlalchemy import SQLAlchemy

# create flass application instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite///phase-4-week-1-flask-pizza-restaurant.db'

db = SQLAlchemy()

def create_app():
    from app import routes  # Import routes here
    return app

# Create the app instance using create_app
app = create_app()


