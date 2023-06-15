from inventory.db import db
from typing import Dict, List

inventory = db.Table(
    "inventory",
    db.Column("item_id", db.Integer, db.ForeignKey("items.id")),
    db.Column("store_id", db.Integer, db.ForeignKey("stores.id")),
)


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    price = db.Column(db.Float(precision=2))

    stores = db.relationship(
        "Store", secondary=inventory, backref=db.backref("items", lazy="dynamic")
    )

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls, name: str) -> "Item":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List:
        return cls.query.all()

    def json(self) -> Dict:
        return {"name": self.name, "price": self.price}

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
