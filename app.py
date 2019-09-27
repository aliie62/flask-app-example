# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:48:19 2019

@author: hosseal
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from resources.endpoints import get_endpoints
from config.security import secret_key


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = 'unknown'
jwt = JWTManager(app)
api = get_endpoints(app)

if __name__ == '__main__':
    from config.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)