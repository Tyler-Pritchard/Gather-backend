from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims,
    jwt_optional,
    get_jwt_identity
)
from models.item import ItemModel
from flask import request
import stripe

BLANK_ERROR = "'{}' cannot be blank."
ITEM_NOT_FOUND = "Item not found."
ITEM_ALREADY_EXISTS = "An item with name '{}' already exists."
INSERT_ITEM_ERROR = "An error occurred inserting the item."
ITEM_DELETED = "Item deleted."
ITEM_NOT_FOUND = "Item not found."
UNAUTHORIZED_USER = "Admin privilege required."
PLEASE_LOG_IN = "Log in for more info on this product."


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

    @classmethod
    @jwt_required
    def get(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': ITEM_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if ItemModel.find_by_name(name):
            return {'message': ITEM_ALREADY_EXISTS.format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": INSERT_ITEM_ERROR}

        return item.json(), 201

    @jwt_required
    def delete(cls, name: str):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': UNAUTHORIZED_USER}, 401

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': ITEM_DELETED}
        return {'message': ITEM_NOT_FOUND}, 404

    @classmethod
    def put(cls, name: str):
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
    @jwt_optional
    def get(cls, name: str):
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]
        if user_id:
            return {'items': items}, 200
        return {
            'items': [item['name'] for item in items],
            'message': PLEASE_LOG_IN
        }, 200
