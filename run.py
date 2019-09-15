from app import app
from db import db
from seeds.menu import menu
from models.menu import MenuModel
from seeds.item import item
from models.item import ItemModel
from models.orderItem import OrderItemModel
from flask import Flask

# TODO: IMPORT ORDERNUMBER & MENUITEMS

db.init_app(app)

app = Flask(__name__)


@app.route("/sms")
def order_in():
    # TODO REPLACE TEXT W/ VARS
    return "Incoming order __OrderNumber__ for __OrderItems__"


if __name__ == "__main__":
    app.run(debug=True)


@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    db.engine.execute(MenuModel.__table__.insert(), menu)
    db.engine.execute(ItemModel.__table__.insert(), item)
