from config.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    active = db.Column(db.Integer)

    def __init__(self,_id,username,password,active = 1):
        self.id = _id
        self.username = username
        self.password = password
        self.active = active
    
    def json(self):
        return {
            'id':self.id,
            'usrename':self.username,
            'active': self.active
            }

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username,active=1).first()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id,active=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

# class UserSchema(ma):
#     class Meta:
#         model = User
#         sqla_session = db.session
