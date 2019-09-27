# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:48:19 2019

@author: hosseal
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from resources.endpoints import get_endpoints
from config.security import secret_key
from models.user import User


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = 'unknown'
api = get_endpoints(app)
jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin':True}
    return {'is_admin': False}

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from config.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)