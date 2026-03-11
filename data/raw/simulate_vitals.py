import random
import time
import json
import uuid
from datetime import datetime

def generate_vitals(patient_id):

    # 85% normal
    if random.random() < 0.85:
        return {
            "heart_rate": random.randint(60, 100),
            "systolic_bp": random.randint(110, 130),
            "diastolic_bp": random.randint(70, 85),
            "temperature": round(random.uniform(36.5, 37.5), 1),
            "spo2": random.randint(95, 100),
            "anomaly": False
        }

    # anomaly
    return {
        "heart_rate": random.randint(150, 190),
        "systolic_bp": random.randint(70, 80),
        "diastolic_bp": random.randint(40, 50),
        "temperature": round(random.uniform(39, 40.5), 1),
        "spo2": random.randint(85, 89),
        "anomaly": True
    }

while True:
    data = generate_vitals(str(uuid.uuid4()))

    message = {
        "device_id": str(uuid.uuid4()),
        "patient_id": data,
        "timestamp": datetime.utcnow().isoformat()
    }

    print(json.dumps(message))

    time.sleep(3)
    exit()  # Remove this line to keep the simulation running indefinitely
   