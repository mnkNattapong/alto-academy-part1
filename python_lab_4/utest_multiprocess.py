"""
script to test python implementation for threading/multiprocess in local machine
support: Windows, Linux, MacOS
"""

import time
from threading import Thread
import multiprocessing
from multiprocessing import Process


def sample_function(process_name: str, message: str, delay: int, max_iter: int = 10):
    print(f'start thread/process-`{process_name}`')
    counter = 0
    while True:
        counter += 1
        print(f"{counter}/{max_iter}: {message}")
        if counter >= max_iter:
            print(f"end thead/process-`{process_name}`")
            break
        time.sleep(delay)


def process_with_thread(thread_count, delay: int = 5):
    threads = list()
    for i in range(thread_count):
        _thread = Thread(target=sample_function, args=((f"threading-{i+1}", f"thred-{i+1}", delay)), daemon=True)
        threads.append(_thread)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # set the current process to be the main multiprocess
    multiprocessing.set_start_method("spawn")
    
    process_1 = Process(target=sample_function,
                    args=("process-1",
                          "test-1",
                          5,))

    process_2 = Process(target=sample_function,
                        args=("process-2",
                            "test-2",
                            10,))

    process_3 = Process(target=process_with_thread,
                        args=(3,
                            10,))
    
    # start multiprocess
    process_1.start()
    process_2.start()
    process_3.start()
    
    # start threading in main process
    threads = list()
    for i in range(3):
        _thread = Thread(target=sample_function, args=((f"main-threading-{i+1}", f"main-thred-{i+1}", 5)), daemon=True)
        threads.append(_thread)
    for thread in threads:
        thread.start()
    
    # stop threading in main process
    for thread in threads:
        thread.join()

    # stop multiprocess
    process_1.join()
    process_2.join()
    process_3.join()

    print("end of main process")
