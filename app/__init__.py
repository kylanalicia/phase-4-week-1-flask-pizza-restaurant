from flask import Flask

app = Flask(__name__)

def create_app():
    from app import routes  # Import routes here
    return app

# Create the app instance using create_app
app = create_app()

# Import other parts of your app here if needed
