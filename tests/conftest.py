import pytest

from inventory.app import app, db
from inventory.models.user import User


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.testing = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    client = app.test_client()
    with app.app_context():
        db.create_all()
    yield client
