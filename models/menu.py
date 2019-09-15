from typing import Dict, List, Union

from db import db
from models.item import menu_item

menus_menu = Dict[str, Union[str, List[menu_item]]]


class MenuModel(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, name: str):
        self.name = name

<<<<<<< HEAD
    def json(self) -> menus_menu:
        return {"name": self.name, "items": [menu.json() for menu in self.items]}
=======
    def json(self, name: str) -> menus_menu:
        return {'name': self.name,
                'items': [menu.json() for menu in self.items]}
>>>>>>> 87f9a316bf146f28944e7edd847f83263c32f672

    @classmethod
    def find_all(cls) -> List["MenuModel"]:
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name: str) -> "MenuModel":
        return MenuModel.query.filter_by(name=name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
