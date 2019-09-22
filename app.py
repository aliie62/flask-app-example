# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:48:19 2019

@author: hosseal
"""

from flask import Flask
from flask_jwt import JWT
from resources.endpoints import get_endpoints
from config.security import secret_key, authenticate,identity


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = secret_key
jwt = JWT(app, authenticate,identity)
api = get_endpoints(app)
