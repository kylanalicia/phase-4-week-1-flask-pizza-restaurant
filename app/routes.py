from app import app  # Import the app instance

@app.route('/', methods=['GET'])
def index():
    return '<h1>Pizza restaurant</h1>'
