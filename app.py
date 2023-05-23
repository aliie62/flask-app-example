# -*- coding: utf-8 -*-

from flask import Flask
from flask_jwt_extended import JWTManager
from resources.endpoints import get_endpoints
from models.user import User
import os
import json
from config.db import db, jwt_redis_blocklist

app = Flask(__name__)
app.config.from_pyfile("config/config.py")
app.secret_key = os.environ.get("Flask_Secret_Key")
api = get_endpoints(app)
jwt = JWTManager(app)

db.init_app(app)


@jwt.token_in_blocklist_loader
def check_token_revoke(jwt_header, jwt_payload):
    token_in_redis = jwt_redis_blocklist.get(jwt_payload["jti"])
    return token_in_redis is not None


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    user = User.find_by_id(identity)
    # It's assumed that user group 2 is Admin group here.
    # I didn't design all the tables (user groups, etc)
    if user.userGroup == 2:
        return {"is_admin": True}
    return {"is_admin": False}


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        json.dumps(
            {"description": "The token has expired", "error": "token_expired"}, indent=4
        ),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        json.dumps(
            {"description": "Signature verification failed.", "error": "invalid_token"},
            indent=4,
        ),
        401,
    )


@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    return (
        json.dumps(
            {
                "description": "Request does not contain an access token",
                "error": "authorization_required",
            },
            indent=4,
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
        json.dumps(
            {"description": "Token is not refreshed.", "error": "fresh_token_required"},
            indent=4,
        ),
        401,
    )


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        json.dumps(
            {"description": "The token has been revoked", "error": "token_revoked"},
            indent=4,
        ),
        401,
    )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000)
