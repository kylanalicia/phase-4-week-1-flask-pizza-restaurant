# manage.py
from app import create_app, db
from flask_migrate import Migrate
from app.models import Restaurant, Pizza , RestaurantPizza

app = create_app()
migrate = Migrate(app, db)


# def make_shell_context():
#     return dict(app=app, db=db, Restaurant=Restaurant, Pizza=Pizza, RestaurantPizza=RestaurantPizza)

if __name__ == '__main__':
    app.run(debug=True)
