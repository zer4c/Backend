import os

from dotenv import load_dotenv
import redis

load_dotenv()
REDIS_PORT = os.getenv("REDIS_PORT")
APP_HOST = os.getenv("APP_HOST")

pool = redis.ConnectionPool().from_url(f"redis://{APP_HOST}:{REDIS_PORT}")

def get_redis_session():
    rd = redis.Redis().from_pool(pool)
    return rd


