from typing import Dict, List, Union

from db import db


menu_item = Dict[str, Union[int, str, float]]


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey(
        'menus.id', ondelete="SET NULL"))
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    description = db.Column(db.String(500))
    # TODO Check file reference re: image_url bug
    image_url = db.Column(db.String(500))
    orders = db.relationship('OrderItemModel', lazy="dynamic")

    def __init__(self, name: str, price: float, description: str, addons,  image_url: str, menu_id: int):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url
        self.menu_id = menu_id

    def json(self) -> menu_item:
        return {'name': self.name, 'price': self.price, 'description': self.description, 'image_url': self.image_url, 'menu_id': self.menu_id}

    # @classmethod
    # def find_all(cls) -> List["ItemModel"]:
    #     return cls.query.all()

    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
