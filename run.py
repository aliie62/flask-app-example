from config.db import db
from app import app, jwt, api

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
