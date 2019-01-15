import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.menu import Menu, MenusList
from seeds.menu import menu
from models.menu import MenuModel
from seeds.item import item
from models.item import ItemModel

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://Tyler:postgres@localhost/gather_python')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    db.engine.execute(MenuModel.__table__.insert(), menu)
    db.engine.execute(ItemModel.__table__.insert(), item)


jwt = JWT(app, authenticate, identity)

api.add_resource(Menu, '/menu/<string:name>')
api.add_resource(MenusList, '/menus')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
