
import os
import json
import random
import time
from dotenv import load_dotenv
load_dotenv()
CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

def simulate_sensor_data():
    """Simulate sensor readings."""
    temperature = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 90.0), 2)
    location = "Room-1"
    return {
        "temperature": temperature,
        "humidity": humidity,
        "location": location,
        "timestamp": time.time(),
    }

def main():
    if not CONNECTION_STRING:
        raise RuntimeError(
            "IOTHUB_DEVICE_CONNECTION_STRING is not set. "
            "Set it in your environment (or .env) before running."
        )

    print("Connecting to Azure IoT Hub...")
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    try:
        while True:
            telemetry = simulate_sensor_data()
            # Send JSON payload with content type for clarity
            payload = json.dumps(telemetry)
            message = Message(payload)
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            client.send_message(message)
            print("Sent:", payload)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nStopping…")
    finally:
        client.shutdown()
        print("Disconnected.")

if __name__ == "__main__":
    main()
