from datetime import timedelta
import os

JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=600)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLITE_URI", "")
PROPAGATE_EXCEPTIONS = True
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECK = ["access", "refresh"]
