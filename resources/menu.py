from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.menu import MenuModel

BLANK_ERROR = "'{}' cannot be blank."
MENU_NOT_FOUND = "Menu not found."
MENU_ALREADY_EXISTS = "A menu with name '{}' already exists."
CREATE_MENU_ERROR = "An error occurred while creating the menu."
MENU_DELETED = "Menu deleted."


class Menu(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True, help=BLANK_ERROR)

    @classmethod
    @jwt_required()
    def get(cls, name: str):
        menu = MenuModel.find_by_name(name)
        if menu:
            return menu.json()
        return {"message": MENU_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if MenuModel.find_by_name(name):
            return {"message": MENU_ALREADY_EXISTS.format(name)}, 400

        data = Menu.parser.parse_args()
        menu = MenuModel(name)
        try:
            menu.save_to_db()
        except:
            return {"message": CREATE_MENU_ERROR}, 500

        return menu.json(), 201

    @classmethod
    def delete(cls, name: str):
        menu = MenuModel.find_by_name(name)
        if menu:
            menu.delete_from_db()
            return {"message": MENU_DELETED}
        return {"message": MENU_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
        data = Menu.parser.parse_args()

        menu = MenuModel.find_by_name(name)

        if menu:
            menu.name = data["name"]
            menu.menu_id = data["menu_id"]

        else:
            menu = MenuModel(name, **data)

        menu.save_to_db()

        return menu.json()


class MenusList(Resource):
    @classmethod
    def get(cls):
        return {"menus": [menu.json() for menu in MenuModel.query.all()]}
