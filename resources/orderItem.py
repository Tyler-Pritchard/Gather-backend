from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.orderItem import OrderItemModel

BLANK_ERROR = "'{}' cannot be blank."
QUANTITY_ERROR = "Quantity cannot be less than 1."
ITEM_NOT_FOUND = "Item not found."
ITEM_ALREADY_EXISTS = "An item with name '{}' already exists."
CREATE_ITEM_ERROR = "An error occurred while creating the item."
ORDERITEM_DELETED = "'{}' deleted."
ORDERITEM_NOT_FOUND = "OrderItem not found."


class OrderItem(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help=BLANK_ERROR
                        )
    parser.add_argument('price',
                        type=int,
                        required=True,
                        help=BLANK_ERROR
                        )
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help=QUANTITY_ERROR
                        )

    @jwt_required()
    # TODO change functions to increase value of "quantity" instead of throwing an error
    def get(self, name: str):
        orderItem = OrderItemModel.find_by_name(name)
        if orderItem:
            return orderItem.json()
        return {'message': ITEM_NOT_FOUND}, 404

    def post(self, name: str, price: float):
        if OrderItemModel.find_by_name(name):
            # switch to quantity ++
            return {'message': ITEM_ALREADY_EXISTS.format(name)}, 400

        data = OrderItem.parser.parse_args()
        orderItem = OrderItemModel(name, price)
        try:
            orderItem.save_to_db()
        except:
            return {'message': CREATE_ITEM_ERROR}, 500

        return orderItem.json(), 201

    def delete(self, name: str):
        orderItem = OrderItemModel.find_by_name(name)
        if orderItem:
            orderItem.delete_from_db()
            return {'message': ORDERITEM_DELETED}
        return {'message': ORDERITEM_NOT_FOUND}, 404

    def put(self, name: str):
        data = OrderItem.parser.parse_args()

        orderItem = OrderItemModel.find_by_name(name)

        if orderItem:
            orderItem.name = data['name']
            orderItem.price = data['price']
            orderItem.quantity = data['quantity']

        else:
            orderItem = OrderItemModel(name, **data)

        orderItem.save_to_db()

        return orderItem.json()


class OrderItemsList(Resource):
    def get(self):
        return {'orderItems': [OrderItem.json() for OrderItem in OrderItemModel.query.all()]}
