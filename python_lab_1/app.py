import os
from helper import get_weather_data, send_line_notify


def read_config(json_path: str) -> dict:
    """
    Read config file (JSON) and return a dictionary with the config values
    """
    # TODO: implement this function
    raise NotImplementedError()


if __name__ == "__main__":
    # read config file (JSON)
    json_path = "config.json"
    json_config: dict = read_config(json_path)
    
    # TODO: add exit case if there is any error
    while True:
        raise NotImplementedError()
        # TODO: get weather data from OpenWeatherMap API
        
        # TODO: condition checking on the weather data
        
        # TODO: send Line notification through LINE Notify API
        
        # TODO: add time sleep ex. 1 hour
