from inventory.db import db
from typing import Dict


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    userGroup = db.Column(db.Integer)
    active = db.Column(db.Integer)
    locked = db.Column(db.Integer)

    def __init__(
        self,
        _id,
        username: str,
        password: str,
        userGroup: int = 1,
        active: int = 1,
        locked: int = 0,
    ) -> None:
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
        self.userGroup = userGroup
        self.active = active
        self.locked = locked

    def json(self) -> Dict:
        return {"id": self.id, "username": self.username, "active": self.active}

    @classmethod
    def find_by_username(cls, username: str) -> "User":
        return cls.query.filter_by(username=username, active=1).first()

    @classmethod
    def find_by_id(cls, user_id: int) -> "User":
        return cls.query.filter_by(id=user_id, active=1).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
