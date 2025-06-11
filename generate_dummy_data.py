import requests
import json
import time
from datetime import datetime
import random

# Render URL for the API endpoint
RENDER_URL = "https://gen-api-xxpm.onrender.com/api/receive-generator-data/"

def generate_random_data():
    # Generate random values within realistic ranges
    return {
        "array_[i]": [
            random.choice([0, 1, 2]),  # Control switch position (0: Off, 1: Auto, 2: Manual)
            random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),  # Genset state
            random.randint(0, 100),  # Current fault
            random.choice([0, 1, 2])  # Current fault severity
        ],
        "array_[ii]": [
            random.uniform(220, 240),  # L1-N voltage
            random.uniform(220, 240),  # L2-N voltage
            random.uniform(220, 240)   # L3-N voltage
        ],
        "array_[iii]": [
            random.uniform(380, 420),  # L1-L2 voltage
            random.uniform(380, 420),  # L2-L3 voltage
            random.uniform(380, 420)   # L3-L1 voltage
        ],
        "array_[iv]": [
            random.uniform(80, 120),   # L1 current
            random.uniform(80, 120),   # L2 current
            random.uniform(80, 120)    # L3 current
        ],
        "array_[v]": [
            random.uniform(20, 25),    # L1 kW
            random.uniform(20, 25),    # L2 kW
            random.uniform(20, 25)     # L3 kW
        ],
        "array_[vi]": [
            random.uniform(65, 75),    # Total kW
            random.uniform(10, 13),    # L1 kVAR
            random.uniform(10, 13),    # L2 kVAR
            random.uniform(10, 13),    # L3 kVAR
            random.uniform(30, 40)     # Total kVAR
        ],
        "array_[vii]": [
            random.uniform(75, 85),    # L1 kVA
            random.uniform(75, 85),    # L2 kVA
            random.uniform(75, 85),    # L3 kVA
            random.uniform(45, 55)     # Total kVA
        ],
        "array_[viii]": [
            random.uniform(12.0, 14.0),  # Battery voltage
            random.uniform(4.0, 5.0)     # Oil pressure
        ],
        "array_[ix]": [
            random.uniform(70, 75)     # Coolant temperature
        ],
        "array_[x]": [
            random.uniform(1450, 1550),  # Engine speed
            random.randint(300, 400)     # Start attempts
        ],
        "array_[xi]": [
            random.uniform(220, 240),  # Utility L1-N voltage
            random.uniform(220, 240),  # Utility L2-N voltage
            random.uniform(220, 240)   # Utility L3-N voltage
        ],
        "array_[xii]": [
            random.uniform(380, 420),  # Utility L1-L2 voltage
            random.uniform(380, 420),  # Utility L2-L3 voltage
            random.uniform(380, 420)   # Utility L3-L1 voltage
        ],
        "array_[xiv]": [
            random.uniform(27, 29)     # Charging alternator voltage
        ],
        "array_[xv]": [
            random.choice([0, 1]),     # Modbus remote start
            random.choice([0, 1]),     # Modbus fault reset
            random.choice([0, 1])      # Network shutdown modbus command
        ]
    }

def send_dummy_data():
    try:
        # Generate random data
        test_data = generate_random_data()
        
        # Send POST request to the API
        response = requests.post(RENDER_URL, json=test_data)
        
        # Print timestamp and response
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{timestamp}] Sending data...")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 201:
            print("Data successfully saved!")
        else:
            print("Failed to save data!")
            
    except requests.exceptions.ConnectionError:
        print("Connection Error: Could not connect to the server. Please check your internet connection.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    print("Starting dummy data generation (Press Ctrl+C to stop)...")
    try:
        while True:
            send_dummy_data()
            # Wait for 1 minute before sending next data
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nStopping data generation...")

if __name__ == "__main__":
    main() 