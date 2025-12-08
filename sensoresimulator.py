import json
import time
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "YOUR_DEVICE_CONNECTION_STRING"

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

locations = ["DowsLake", "FifthAvenue", "NAC"]

while True:
    for loc in locations:
        data = {
            "location": loc,
            "iceThickness": round(random.uniform(28, 35), 2),
            "surfaceTemp": round(random.uniform(-12, 2), 2),
            "snow": round(random.uniform(5, 12), 2),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        msg = Message(json.dumps(data))
        client.send_message(msg)
        print("Sent:", data)

    time.sleep(10)
