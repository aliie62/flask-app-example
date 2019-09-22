from config.db import db

inventory = db.Table('inventory',
                    db.Column('item_id',db.Integer, db.ForeignKey('items.id')),
                    db.Column('store_id', db.Integer, db.ForeignKey('stores.id'))
                    )


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.INTEGER, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    stores = db.relationship('Store', secondary=inventory,
                            backref = db.backref('items', lazy='dynamic'))

    def __init__(self,name,price):
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def json(self):
        return {'name':self.name, 'price':self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



# class ItemSchema(ma):
#     class Meta:
#         model = Item
#         sqla_session = db.session
