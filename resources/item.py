from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from flask import request
import stripe

BLANK_ERROR = "'{}' cannot be blank."
ITEM_NOT_FOUND = "Item not found."
ITEM_ALREADY_EXISTS = "An item with name '{}' already exists."
INSERT_ITEM_ERROR = "An error occurred inserting the item."
ITEM_DELETED = "Item deleted."
ITEM_NOT_FOUND = "Item not found."


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help=BLANK_ERROR
                        )

    parser.add_argument('menu_id',
                        type=float,
                        required=True,
                        help=BLANK_ERROR
                        )

    parser.add_argument('description',
                        type=str,
                        required=True,
                        help=BLANK_ERROR
                        )

    parser.add_argument('image_url',
                        type=str,
                        required=True,
                        help=BLANK_ERROR
                        )

    @jwt_required()
    def get(self, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': ITEM_NOT_FOUND}, 404

    def post(self, name: str):
        if ItemModel.find_by_name(name):
            return {'message': ITEM_ALREADY_EXISTS.format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": INSERT_ITEM_ERROR}

        return item.json(), 201

    def delete(self, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': ITEM_DELETED}
        return {'message': ITEM_NOT_FOUND}, 404

    def put(self, name: str):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
            item.description = data['description']
            item.addons = data['addons']
            item.image_url = data['image_url']
            item.menu_id = data['menu_id']

        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class ItemsList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
