# Rideau Canal Sensor Simulation

## Overview
This repository contains the IoT sensor simulation component of the **Rideau Canal Real-Time Monitoring System**.  
The simulator generates **realistic sensor readings** for three locations along the Rideau Canal:

- **Dow's Lake**
- **Fifth Avenue**
- **NAC**

Every 10 seconds, each simulated device sends a JSON message to **Azure IoT Hub**, where it flows into:

➡ Stream Analytics → Cosmos DB (real-time)  
➡ Stream Analytics → Blob Storage (historical data)  
➡ Web Dashboard (live visualization)

### Technologies Used
- **Python 3**
- **Azure IoT Device SDK**
- **JSON**
- **dotenv for environment variable management**

---

## Prerequisites
Before running the simulator, make sure you have:

- **Python 3.8+** installed  
- **Azure IoT Hub** created  
- **3 registered IoT Devices** in your IoT Hub  
- **Device connection string** for each device  
- Internet connection  

(Optional but recommended)  
- Visual Studio Code  
- Python virtual environment  

---

##  Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rideau-canal-sensor-simulation.git
cd rideau-canal-sensor-simulation


2. Create a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate   # Windows


3. Install dependencies:

pip install -r requirements.txt

4. Configuration

Copy the example environment file:

cp .env.example .env


Open .env and update your IoT Hub device connection string:

IOTHUB_DEVICE_CONNECTION_STR=your-device-connection-string-here
SENSOR_CONFIG=config/sensor_config.json


(Optional) Update sensor configuration in:

config/sensor_config.json


Example:

{
  "locations": ["DowsLake", "FifthAvenue", "NAC"],
  "send_interval_seconds": 10
}

5. Usage

Run the sensor simulator:

python sensor_simulator.py


You will see output similar to:

Sent: {"location": "DowsLake", "timestamp": "...", "iceThickness": 32.4, "surfaceTemperature": -3.1, "snowAccumulation": 1.2, "externalTemperature": -8.0}


Data is sent to Azure IoT Hub every 10 seconds.