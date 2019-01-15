from app import app
from db import db
from seeds.menu import menu
from models.menu import MenuModel
from seeds.item import item
from models.item import ItemModel
from models.orderItem import OrderItemModel

db.init_app(app)


@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    db.engine.execute(MenuModel.__table__.insert(), menu)
    db.engine.execute(ItemModel.__table__.insert(), item)
