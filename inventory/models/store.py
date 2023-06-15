from inventory.db import db
from typing import Dict, List


class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def find_by_name(cls, name: str) -> "Store":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["Store"]:
        return cls.query.all()

    def json(self) -> Dict:
        return {
            "name": self.name,
            "items": [{"name": item.name} for item in self.items.all()],
        }

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
