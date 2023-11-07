import random
import time
import threading
import json

def generate_data(thermometer_id):
    while True:
        data = {
            "value": round(random.uniform(18, 25), 2),
            "timestamp": time.time(),
            "device_id": f"thermometer_{thermometer_id}"
        }

        print(json.dumps(data))

        time.sleep(random.uniform(1, 5))

if __name__ == '__main__':
    num_thermometers = 3
    threads = []

    for i in range(1, num_thermometers + 1):
        thread = threading.Thread(target=generate_data, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
