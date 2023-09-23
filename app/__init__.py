from flask import Flask
from sqlalchemy import SQLalchemy


app = Flask(__name__)

db = SQLalchemy()

def create_app():
    from app import routes  # Import routes here
    return app

# Create the app instance using create_app
app = create_app()


