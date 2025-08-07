# Weather API Wrapper com Cache em Redis

Este projeto é um **wrapper de API de clima** desenvolvido com **Flask**, que busca informações meteorológicas de uma API externa (como a [Visual Crossing](https://www.visualcrossing.com/)), e utiliza **Redis** como cache para melhorar a performance e reduzir chamadas desnecessárias à API externa.

---

## Tecnologias utilizadas

- Python
- Flask
- Redis
- Marshmallow
- Requests
- Dotenv

---

## Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz com o seguinte conteúdo:

```env
API_KEY=VISUAL_CROSSING_API_KEY
WEATHER_API_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
REDIS_HOST=localhost
REDIS_PORT=6379
CACHE_TIMEOUT=43200  

## Instalação do projeto 

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

python run.py

## Como usar

Endpoint
GET /weather?city=<nome-da-cidade>
curl "http://localhost:5000/weather?city=Rio de Janeiro"

