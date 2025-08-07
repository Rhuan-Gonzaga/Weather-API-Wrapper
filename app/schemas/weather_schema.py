from marshmallow import Schema, fields

class WeatherRequestSchema(Schema):
    city = fields.String(required=True)
