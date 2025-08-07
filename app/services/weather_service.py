import requests
from app.utils.config import Config

def fetch_weather_from_api(city):
    url = f"{Config.WEATHER_API_URL}/{city}"
    params = {
        "key": Config.API_KEY,
        "unitGroup": "metric",
        "include": "current",
        "contentType": "json"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Erro ao buscar dados da API: {response.text}")

    return response.json()
