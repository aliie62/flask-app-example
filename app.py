# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:48:19 2019

@author: Ali Hosseini
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from resources.endpoints import get_endpoints
from models.user import User
from resources.user import loggedOutList
import os
import json
from config.db import db

app = Flask(__name__)
app.config.from_pyfile('config/config.py')
app.secret_key = os.environ.get('Flask_Secret_Key')
api = get_endpoints(app)
jwt = JWTManager(app)
db.init_app(app)

@jwt.token_in_blocklist_loader
def user_logout(jwt_header, jwt_payload):
    return jwt_payload['jti'] in loggedOutList
      
@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    user = User.find_by_id(identity)
    if user.userGroup == 2:
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
    app.run(port=5000, debug=True)