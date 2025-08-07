from flask import Blueprint, request, jsonify
from app.schemas.weather_schema import WeatherRequestSchema
from app.models.weather_request import WeatherRequest
from app.services.weather_service import fetch_weather_from_api
from app.cache.redis_cache import get_cached_weather, set_cached_weather

weather_bp = Blueprint("weather", __name__)
schema = WeatherRequestSchema()

@weather_bp.route("/weather", methods=["GET"])
def get_weather():
    args = schema.load(request.args)
    city = args["city"]

    cached = get_cached_weather(city)
    if cached:
        return jsonify({"source": "cache", "data": cached})

    data = fetch_weather_from_api(city)
    set_cached_weather(city, data)
    return jsonify({"source": "api", "data": data})
