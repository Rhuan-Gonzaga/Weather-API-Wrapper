from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    WEATHER_API_URL = os.getenv("WEATHER_API_URL")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    CACHE_TIMEOUT = int(os.getenv("CACHE_TIMEOUT", 43200))  
