from flask_restful import Resource
from models.menu import MenuModel


class Menu(Resource):
    def get(self, name):
        menu = MenuModel.find_by_name(name)
        if menu:
            return menu.json()
        return {'message': 'Menu not found'}, 404

    def post(self, name):
        if MenuModel.find_by_name(name):
            return {'message': "A menu with name '{}' already exists.".format(name)}, 400

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


class MenuList(Resource):
    def get(self):
        return {'menus': [menu.json() for menu in MenuModel.query.all()]}
