import os
import json
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# Load .env file
load_dotenv()

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

LOCATIONS = ["DowsLake", "FifthAvenue", "NAC"]

def generate_sensor_data(location):
    return {
        "location": location,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "iceThickness": round(random.uniform(25.0, 40.0), 2),
        "surfaceTemperature": round(random.uniform(-15.0, 5.0), 2),
        "snowAccumulation": round(random.uniform(0.0, 10.0), 2),
        "externalTemperature": round(random.uniform(-20.0, 3.0), 2),
    }

def main():
    print("Connecting to Azure IoT Hub...")
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("Connected! Sending data every 10 seconds...\n")

    while True:
        for location in LOCATIONS:
            payload = generate_sensor_data(location)
            message = Message(json.dumps(payload))

            print("Sending:", payload)
            client.send_message(message)

        time.sleep(10)

if __name__ == "__main__":
    main()
