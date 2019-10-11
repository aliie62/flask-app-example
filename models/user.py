from config.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    userGroup = db.Column(db.Integer)
    active = db.Column(db.Integer)
    locked = db.Column(db.Integer)



    def __init__(self,_id,username,password, userGroup = 1, active = 1, locked = 0):
        """
        Instance attributes:
        username
        password
        userGroup:
            *1: Normal
            *2: Admin
        active:
            *0: Inactive: Being used instead of physical deletion
            *1: Active
        locked:
            *0: Not locked
            *1: Locked for any reason that doesn't comply with the available policies. For exapmale suspecious activity.
        """
        self.id = _id
        self.username = username
        self.password = password
        self.active = active
        self.locked = locked
    
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