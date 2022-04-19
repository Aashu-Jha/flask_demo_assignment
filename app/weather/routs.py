from flask import Blueprint

from weather.controller import (
    get_current_weather,
)

weather_api = Blueprint("weather", __name__)
weather_api.add_url_rule(rule="/currentWeather", view_func=get_current_weather, methods=["GET"])