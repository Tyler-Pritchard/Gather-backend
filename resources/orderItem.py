from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.orderItem import OrderItemModel


class OrderItem(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="Every item needs a name."
                        )
    parser.add_argument('price',
                        type=int,
                        required=True,
                        help="Every item needs a price."
                        )
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="Quantity cannot be less than 1."
                        )

    @jwt_required()
    # change functions to increase value of "quantity" instead of throwing an error
    def get(self, name):
        orderItem = OrderItemModel.find_by_name(name)
        if orderItem:
            return orderItem.json()
        return {'message': 'Item not found'}, 404

    def post(self, name, price):
        if OrderItemModel.find_by_name(name):
            # switch to quantity ++
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = OrderItem.parser.parse_args()
        orderItem = OrderItemModel(name, price)
        try:
            orderItem.save_to_db()
        except:
            return {'message': 'An error occurred while creating the item.'}, 500

        return orderItem.json(), 201

    def delete(self, name):
        orderItem = OrderItemModel.find_by_name(name)
        if orderItem:
            orderItem.delete_from_db()
            return {'message': 'OrderItem deleted'}
        return {'message': 'OrderItem not found.'}, 404

    def put(self, name):
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
