from redis.asyncio import Redis
import os

host = os.getenv("REDIS_HOST")
port = os.getenv("REDIS_PORT")

def init_redis():
    return Redis(
        host=host,
        port=port,
    )