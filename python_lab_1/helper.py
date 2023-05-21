import requests


def get_weather_data(access_key: str, lat: str = "13.7450255", lon: str = "100.5209932"):
    """ Get weather data from OpenWeatherMap API
    default lat-lon is for MintTower building, Bangkok, Thailand
    
    Document
    OpenWeatherMap: https://openweathermap.org/
    API key page: https://home.openweathermap.org/api_keys
    Current-weather API: https://openweathermap.org/current
    Lat-Lon finder: https://openweathermap.org/api/geocoding-api
    """
    response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather/",
                        params={
                            "lat": lat, 
                            "lon": lon, 
                            "appid": access_key
                        })
    return response


def send_line_notify(access_token: str, message: str):
    """ Send notification to Line notify API
    setting UI: https://notify-bot.line.me/th/
    API document: https://notify-bot.line.me/doc/en/
    """
    # prepare context for API: set header and params
    API_URI = 'https://notify-api.line.me/api/notify'
    headers = {
        "Authorization": f"Bearer {str(access_token)}"
    }
    params = {'message': message}

    # send request to Line notify API
    _ = requests.post(
        url=API_URI,
        headers=headers,
        params=params
    )


# if __name__ == "__main__":
#     # test `get_weather_data` function
#     access_key = "c098c02beca350bf40e4fcc3006b4f69" 
#     data = get_weather_data(access_key, lat="13.7450255", lon="100.5209986")
#     print("Weather API's status code:", data.status_code)
#     weather_data = data.json()
#     if data.status_code == 200:
#         # display appearance and description
#         appearance = weather_data["weather"][0]["main"]
#         description = weather_data["weather"][0]["description"]
#         print("The weather is", appearance, "with", description)
        
#         # display temperature
#         temp_kalvin = weather_data["main"]['temp']
#         temp = round(temp_kalvin - 273.15, 2)
#         print("Temperature:", temp)
        
#         # display humidity and wind speed
#         print("Humidity:", weather_data["main"]['humidity'], "%")
#         print("Wind Speed:", weather_data["wind"]['speed'], "m/s")
#     elif data.status_code != 200:
#         # display error message
#         print(weather_data['message'])
    
#     # test `send_line_notify` function
#     line_token = "9mi8PJinVLNprxLOyd7YgOJ6pSpxsHm4MFmdvsVKkC4" # TODO: replace with your access token
#     send_line_notify(access_token=line_token, message="Hello world!") 
#     print("Done!")
    