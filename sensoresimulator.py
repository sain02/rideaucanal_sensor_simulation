import os
import json
import random
import time
from datetime import datetime, timezone
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# Load .env file
load_dotenv()

# Get device connection string
CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

def generate_sensor_data():
    """Generate random readings for Rideau Canal sensors."""
    payload = {
        "location": "DowsLake",   # OR change per device
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "iceThickness": round(random.uniform(20.0, 40.0), 2),
        "surfaceTemperature": round(random.uniform(-10.0, 2.0), 2),
        "snowAccumulation": round(random.uniform(0.0, 6.0), 2),
        "externalTemperature": round(random.uniform(-20.0, 5.0), 2)
    }
    return payload

def main():
    print("Connecting to Azure IoT Hub...")
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    client.connect()
    print("Connected! Sending messages every 10 seconds...\n")

    try:
        while True:
            data = generate_sensor_data()
            message = Message(json.dumps(data))
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            print("Sending:", data)
            client.send_message(message)

            time.sleep(10)

    except KeyboardInterrupt:
        print("Stopped.")

    finally:
        client.shutdown()

if __name__ == "__main__":
    main()
