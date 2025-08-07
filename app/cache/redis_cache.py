from app.utils.extensions import redis_client
from app.utils.config import Config
import json

def get_cached_weather(city):
    data = redis_client.get(city.lower())
    return json.loads(data) if data else None

def set_cached_weather(city, data):
    redis_client.setex(
        city.lower(),
        Config.CACHE_TIMEOUT,
        json.dumps(data)
    )
