from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.menu import MenuModel


class Menu(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="Every menu needs a description."
                        )

    parser.add_argument('image_url',
                        type=str,
                        required=True,
                        help="Every menu needs an image."
                        )

    @jwt_required()
    def get(self, name):
        menu = MenuModel.find_by_name(name)
        if menu:
            return menu.json()
        return {'message': 'Menu not found'}, 404

    def post(self, name):
        if MenuModel.find_by_name(name):
            return {'message': "A menu with name '{}' already exists.".format(name)}, 400

        data = Menu.parser.parse_args()
        menu = MenuModel(name)
        try:
            menu.save_to_db()
        except:
            return {'message': 'An error occurred while creating the menu.'}, 500

        return menu.json(), 201

    def delete(self, name):
        menu = MenuModel.find_by_name(name)
        if menu:
            menu.delete_from_db()
            return {'message': 'Menu deleted'}
        return {'message': 'Menu not found.'}, 404

    def put(self, name):
        data = Menu.parser.parse_args()

        menu = MenuModel.find_by_name(name)

        if menu:
            menu.price = data['price']
            menu.description = data['description']
            menu.addons = data['addons']
            menu.image_url = data['image_url']
            menu.menu_id = data['menu_id']

        else:
            menu = MenuModel(name, **data)

        menu.save_to_db()

        return menu.json()


class MenusList(Resource):
    def get(self):
        return {'menus': [menu.json() for menu in MenuModel.query.all()]}
