from datetime import timedelta
import os

#JWT_AUTH_URL_RULE = '/login'
JWT_EXPIRATION_DELTA = timedelta(seconds = 600)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','sqlite:///data.db')
PROPAGATE_EXCEPTIONS = True