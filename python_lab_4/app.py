import os
import json
import multiprocessing
from multiprocessing import Process, Queue
from helper import get_weather_data, inference_llm, gradio_interface


def read_config(json_path: str) -> dict:
    """
    Read config file (JSON) and return a dictionary with the config values
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found at {json_path}")

    with open(json_path, "r") as json_file:
        json_config = json.load(json_file)
    return json_config

def main_process():
    # TODO: main process to collect multiple IoT data ex. weather data API
    # TODO: apply Threading to support multiple API calls at the same time
    raise NotImplementedError()

def LLM_process():
    # TODO: sub process to inference LLM model
    raise NotImplementedError()

def interface_process():
    # TODO: sub process to run the user interface
    raise NotImplementedError()

if __name__ == "__main__":
    # read config file (JSON)
    json_path = "config.json"
    json_config: dict = read_config(json_path)
    
    # set the current process to be the main multiprocess
    multiprocessing.set_start_method("spawn")
    
    # TODO: declare multiprocessing Queues to connect between processes
    
    # TODO: declare LLM process
    
    # TODO: declare interface process
    
    # TODO: run main process to collect IoT data

    # TODO: start-join each process
