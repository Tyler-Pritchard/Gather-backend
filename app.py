from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
# gain access to the users resource
from resources.user import UserRegister
from resources.item import Item, ItemList
#from resources.cart import Cart
#from resources.menu import Menu

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
# call UserRegister + functions
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
