from db import db


class OrderItemModel(db.Model):
    __tablename__ = 'orderItems'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey(
        'items.id', ondelete="SET NULL"))
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def json(self):
        return {'name': self.name, 'price': self.price, 'orderItems': [orderItem.json() for orderItem in self.orderItems], 'quantity': self.quantity}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
