import os
import json
import time
from helper import get_weather_data, send_line_notify

def read_config(json_path: str) -> dict:
    """
    Read config file (JSON) and return a dictionary with the config values
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found at {json_path}")
    
    with open(json_path, "r") as json_file:
        json_config: dict = json.load(json_file)
        
    return json_config


if __name__ == "__main__":
    # read config file (JSON)
    json_path = "config.json"
    json_config: dict = read_config(json_path)
    
    # get config values
    time_sleep = json_config.get("time_sleep", 60*60) # unit: second
    weather_access_key = json_config.get("weather_access_key", "")
    line_notify_token = json_config.get("line_notify_token", "")
    lat = json_config.get("lat", "3.7450255")
    lon = json_config.get("lon", "100.5209986")
    
    # error handling for config values
    if weather_access_key == "":
        raise ValueError("weather_access_key is empty")
    if line_notify_token == "":
        raise ValueError("line_notify_token is empty")
    
    
    # TODO: add exit case if there is any error
    # TODO: apply clean code principle
    while True:
        # get weather data from OpenWeatherMap API
        print("getting weather data")
        request_data = get_weather_data(weather_access_key, lat=lat, lon=lon)
        
        # error handling for API response
        if request_data.status_code != 200:
            time.sleep(int(time_sleep)) # unit : second
            continue
            
        weather_data : dict =  request_data.json()
            
        # select data from APT response
        weather_condition = weather_data["weather"][0]["main"]
        
        # condition checking on the weather data
        if weather_condition == "Clouds":
            # construct message
            print("constructing message")
            message = f"Today's weather is {weather_condition}"
    
            # send Line notification through LINE Notify API
            send_line_notify(access_token=line_notify_token, message=message)
        
        # add time sleep ex. 1 hour
        time.sleep(int(time_sleep)) # unit : second
        