import os
import json
import time
import pendulum
import gradio as gr
import multiprocessing
from multiprocessing import Process, Queue
from helper import get_weather_data, inference_llm


def read_config(json_path: str) -> dict:
    """
    Read config file (JSON) and return a dictionary with the config values
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found at {json_path}")

    with open(json_path, "r") as json_file:
        json_config = json.load(json_file)
    return json_config

def main_process(iot_queue, openmap_key: str, map_locations: list, delay: int = 60):
    print('start IoT data collection (Main) process')
    # wriet main process to collect multiple IoT data ex. weather data API
    while True:
        weather_data = list()
        for map_location in map_locations:
            # TODO: apply Threading to support multiple API calls at the same time (later)
            # TODO: request Weather data from API
            pass
            
            # TODO: prepare data format for IoT-Queue
        
        # TODO: insert IoT data to Queue
        
        time.sleep(delay)

def LLM_process(iot_queue, llm_result_queue, json_config: dict, MAX_LLM_QUEUE_SIZE: int = 50):
    # write sub process to inference LLM model
    print('start LLM process')
    while True:
        try:
            # TODO: get IoT data from Queue
            weather_datas = None  # edit here
            
            if weather_datas is None:
                continue
            
            if len(weather_datas) > 0:
                # TODO: inference LLM model
                pass
                
                # TODO: insert LLM result to Queue
                # TODO: handle `llm_result_queue` Queue size to prevent memory leak (later)

        except Exception as e:
            print("LLM_process: ", e)

def interface_process(llm_result_queue):
    print('start Interface process')
    
    def _get_current_analytics(chat_history):
        llm_result = dict()
        # TODO: get latest LLM-response data from LLM-Queue
        
        
        if len(llm_result) == 0:
            return chat_history + [[None, "Jarvis: There is no data yet or the latest weather analysis is already shown."]]
        
        current_weather = f"Datetime: {llm_result.get('timestamp', '-')}\n"
        weather_datas = llm_result.get("weather_datas", dict())
        for idx, weather_data in enumerate(weather_datas):
            current_weather += f"{idx+1}. {weather_data.get('name')} weather station - real-time weather data:\n"
            current_weather += f"- Weather condition: {weather_data.get('weather_condition')}\n"
            current_weather += f"- Temperature: {weather_data.get('temperature')} C\n"
            current_weather += f"- Humidity: {weather_data.get('humidity')} %\n"
        return chat_history + [[current_weather, llm_result.get("gpt_response", "")]]

    with gr.Blocks() as demo:
        gr.HTML("""<h1 align="center">AI Personal Assistance</h1>""")
        
        chatbot_intro_message = "I'm Jarvis, your personal AI assistance. Click below button to analyze current weather from multiple locations"
        chatbot = gr.Chatbot(label="AltoGPT chatbot", value=[[None, chatbot_intro_message]]).style(height=600)
        submit = gr.Button("Show current weather analysis", variant="primary")
        
        submit.click(_get_current_analytics, chatbot, chatbot, queue=False)

    demo.queue(concurrency_count=3)
    demo.launch(
        server_name="0.0.0.0", 
        server_port=7860,
        # auth=("username", "password")  # add authentication to UI
        )

if __name__ == "__main__":
    # read config file (JSON)
    json_path = "config.json"
    json_config: dict = read_config(json_path)
    
    openmap_key = json_config.get("openmap_key", None)
    azure_openai_endpoint = json_config.get("azure_openai_endpoint", None)
    azure_openai_key = json_config.get("azure_openai_key", None)
    map_locations = json_config.get("map_locations", list())
    
    # set the current process to be the main multiprocess
    multiprocessing.set_start_method("spawn")
    
    # TODO: declare multiprocessing Queues to connect between processes
    """ sample Queue code:
    sample_queue.put(dict_data)  # insert data to queue
    dict_data = sample_queue.get()  # get data from queue
    """
    iot_queue = Queue()  # transfer IoT data from main process to LLM process
    llm_result_queue = Queue()  # transfer LLM result from LLM process to interface process
    
    # TODO: declare LLM process
    
    # TODO: declare interface process
    
    # TODO: start each process
    
    # TODO: run main process to collect IoT data
    
    # TODO: join/stop each process
