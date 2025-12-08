import os
import json
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

load_dotenv()

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

# Three locations required for dashboard
LOCATIONS = ["DowsLake", "FifthAvenue", "NAC"]

def generate_sensor_data(location):
    return {
        "location": location,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "iceThickness": round(random.uniform(20, 40), 2),
        "surfaceTemperature": round(random.uniform(-15, 2), 2),
        "snowAccumulation": round(random.uniform(0, 10), 2),
        "externalTemperature": round(random.uniform(-20, 5), 2)
    }

def main():
    print("Connecting to Azure IoT Hub...")
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("Connected! Sending messages every 10 seconds...")

    while True:
        for loc in LOCATIONS:
            data = generate_sensor_data(loc)
            message = Message(json.dumps(data))
            client.send_message(message)
            print("Sent:", data)

        time.sleep(10)

if __name__ == "__main__":
    main()
