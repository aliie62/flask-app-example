# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:48:19 2019

@author: hosseal
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from resources.endpoints import get_endpoints
from models.user import User
import os
import json

app = Flask(__name__)
app.config.from_pyfile('config/config.py')
app.secret_key = os.environ.get('Flask_Secret_Key')
api = get_endpoints(app)
jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def is_blacklisted(decrypted_token):
    return User.find_locked(decrypted_token['identity'])
        
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin':True}
    return {'is_admin': False}

@jwt.expired_token_loader
def expired_token_callback():
    return json.dumps({
        'description': 'The token has expired',
        'error': 'token_expired'
    },indent=4), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return json.dumps({
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    },indent=4), 401

@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    return json.dumps({
        'description': 'Request does not contain an access token',
        'error': 'authorization_required'
    },indent=4), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return json.dumps({
        'description': 'Token is not refreshed.',
        'error': 'fresh_token_required'
    },indent=4), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return json.dumps({
        'description': 'The token has been revoked',
        'error': 'token_revoked'
    },indent=4), 401

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from config.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)