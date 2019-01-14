from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey(
        'menus.id', ondelete="SET NULL"))
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    description = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    orders = db.relationship('OrderItemModel', lazy="dynamic")

    def __init__(self, name, price, description, addons, image_url, menu_id):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url
        self.menu_id = menu_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'description': self.description, 'image_url': self.image_url, 'menu_id': self.menu_id}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
