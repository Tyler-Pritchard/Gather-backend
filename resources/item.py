from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from flask import request
import stripe


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('menu_id',
                        type=float,
                        required=True,
                        help="Every item needs a menu id."
                        )

    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="Every item needs a description."
                        )

    parser.add_argument('image_url',
                        type=str,
                        required=True,
                        help="Every item needs an image."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
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
