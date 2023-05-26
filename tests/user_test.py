from flask_jwt_extended import create_access_token
from pytest_schema import schema, exact_schema, like_schema, SchemaError
import pytest
import json

from inventory.app import app

register_schema = {"message": str}
login_schema = {"access_token": str, "refresh_token": str}


# -----------------------
# Happy path test cases
# -----------------------
def test_user_register(client) -> None:
    body = {"username": "ali", "password": "1234"}
    response = client.post("/register", json=body)
    assert response.json == {"message": "User has been created successfully."}
    assert response.status_code == 200


def test_user_login(client) -> None:
    body = {"username": "ali", "password": "1234"}
    response = client.post("/login", json=body)
    assert response.status_code == 200


def test_user_getbyid(client) -> None:
    with app.app_context():
        access_token = create_access_token(identity=1, fresh=True)
        headers = {"Authorization": "Bearer {}".format(access_token)}
        response = client.get("/user/1", headers=headers)
        assert response.json == {"id": 1, "username": "testuser1", "active": 1}
