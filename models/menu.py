from typing import Dict

from db import db


class MenuModel(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy="dynamic")

    def __init__(self, name: str):
        self.name = name

    def json(self) -> Dict:
        return {'name': self.name, 'items': [menu.json() for menu in self.items]}

    # @classmethod
    # def find_all(cls) -> List:
    #     return cls.query.all()

    @classmethod
    def find_by_name(cls, name: str):
        return MenuModel.query.filter_by(name=name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
