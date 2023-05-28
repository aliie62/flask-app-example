from flask_sqlalchemy import SQLAlchemy
import redis
import os

db = SQLAlchemy()

jwt_redis_blocklist = redis.StrictRedis(
    host=os.environ.get("REDIS_HOST", "127.0.0.1"),
    port=os.getenv("REDIS_PORT", "6379"),
    db=0,
    decode_responses=True,
)
