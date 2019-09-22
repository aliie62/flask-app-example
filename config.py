from datetime import timedelta

JWT_AUTH_URL_RULE = '/login'
JWT_EXPIRATION_DELTA = timedelta(seconds = 600)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
