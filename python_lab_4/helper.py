import requests
import openai


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


def inference_llm(json_config: dict, weather_datas: list):
    openai.api_type = "azure"
    openai.api_base = json_config.get("azure_openai_endpoint")
    openai.api_key = json_config.get("azure_openai_key")
    openai.api_version = json_config.get("azure_openai_api_version")
    map_locations = json_config.get("map_locations", list())
    
    # prepare prompt message
    location_names = [location.get("name") for location in map_locations]
    message_location_name = ""
    for idx, location_name in enumerate(location_names):
        message_location_name += f"{idx+1}. {location_name} weather station\n"

    message_weather_data = ""
    for idx, weather_data in enumerate(weather_datas):
        message_weather_data += f"{idx+1}. {weather_data.get('name')} weather station - real-time weather data:\n"
        message_weather_data += f"- Weather condition: {weather_data.get('weather_condition')}\n"
        message_weather_data += f"- Temperature: {weather_data.get('temperature')} C\n"
        message_weather_data += f"- Humidity: {weather_data.get('humidity')} %\n"
    
    gpt_role = """
        I want you to act as a AI personal assistance in smart home solutions. 
        Your main objective is to analyze real-time weather data from multiple locations, then summarize the data to user.
        If there is any abnormal or rain weather condition, you should notify the user immediately or suggest the user to take action.
    """
    prompt_message = f"""
        There are {len(location_names)} weather station locations:
        {message_location_name}
        
        {message_weather_data}
    """

    messages = [
        {"role": "system", "content": gpt_role},
        {"role": "user", "content": prompt_message}
    ]
    
    try:
        response = openai.ChatCompletion.create(
            deployment_id="altoacademy-gpt35turbo",
            messages=messages,
            temperature=0.6,
            stream=False
        )

        gpt_response = response['choices'][0]['message']['content']
    except Exception as e:
        gpt_response = f"(inference_llm) Error: {e}"

    return gpt_response, prompt_message


def demo_llm():
    import json
    with open("config.json", "r") as json_file:
        json_config = json.load(json_file)
        
    openai.api_type = "azure"
    openai.api_base = json_config.get("azure_openai_endpoint")
    openai.api_key = json_config.get("azure_openai_key")
    openai.api_version = json_config.get("azure_openai_api_version")
    
    gpt_role = """
        I want you to act as a AI personal assistance in smart home solutions. 
        Your main objective is to analyze real-time weather data from multiple locations, then summarize the data to user.
        If there is any abnormal or rain weather condition, you should notify the user immediately or suggest the user to take action.
    """
    prompt_message = """
        There are 2 weather station locations:
        1. Home weather station
        2. Office weather station
        
        Home weather station - real-time weather data:
        - Weather condition: Clouds
        - Temperature: 28.0 C
        - Humidity: 55.0 %
        
        Office weather station - real-time weather data:
        - Weather condition: Rain
        - Temperature: 29.0 C
        - Humidity: 65.0 %
    """
    messages = [
        {"role": "system", "content": gpt_role},
        {"role": "user", "content": prompt_message}
    ]
    
    response = openai.ChatCompletion.create(
        deployment_id="altoacademy-gpt35turbo",
        messages=messages,
        temperature=0.6,
        stream=False
    )

    gpt_response = response['choices'][0]['message']['content']
    print(gpt_response)


def demo_llm_full():
    import json
    with open("config.json", "r") as json_file:
        json_config = json.load(json_file)
        
    weather_datas = [
        {
            "name": "Home",
            "weather_condition": "Clouds",
            "temperature": 28.0,
            "humidity": 55.0
        },
        {
            "name": "Office",
            "weather_condition": "Rain",
            "temperature": 29.0,
            "humidity": 65.0
        }
    ]

    gpt_response, prompt_message = inference_llm(json_config, weather_datas)
    print("Prompt message: ")
    print(prompt_message)
    print("--------------------")
    print("LLM response: ")
    print(gpt_response)


if __name__ == "__main__":
    # demonstrate how LLM works
    # demo_llm()
    
    # demonstrate `inference_llm` function usage
    # demo_llm_full()
    pass
