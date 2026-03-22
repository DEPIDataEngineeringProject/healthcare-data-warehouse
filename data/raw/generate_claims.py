import pandas as pd
import numpy as np
import uuid
import random
from faker import Faker
import json

fake = Faker()

# =========================
# Load Data
# =========================
patients_df = pd.read_csv(r"D:\DEPI\DEPI final project\data sources\patients.csv")
encounters_df = pd.read_csv(r"D:\DEPI\DEPI final project\data sources\encounters.csv")

# =========================
# Payers Setup (Realistic)
# =========================
payers = [
    {"name": "Medicare", "type": "public"},
    {"name": "Medicaid", "type": "public"},
    {"name": "Blue Cross Blue Shield", "type": "private"},
    {"name": "Aetna", "type": "private"},
    {"name": "Cigna", "type": "private"},
    {"name": "UnitedHealthcare", "type": "private"},
    {"name": "Self-Pay", "type": "self"}
]

# Denial reasons
denial_reasons = [
    "Missing documentation",
    "Invalid coding",
    "Out of network",
    "Duplicate claim",
    "Service not covered"
]

# =========================
# Helper Functions
# =========================

def choose_payer():
    return random.choice(payers)


def generate_status(payer_type):
    r = random.random()

    # Public insurance (lower denial)
    if payer_type == "public":
        if r < 0.75:
            return "paid"
        elif r < 0.9:
            return "approved"
        else:
            return "denied"

    # Private insurance (moderate denial)
    elif payer_type == "private":
        if r < 0.65:
            return "paid"
        elif r < 0.85:
            return "approved"
        elif r < 0.95:
            return "denied"
        else:
            return "appealed"

    # Self pay (no denial)
    else:
        return "paid"


def generate_amounts(base_cost, status):
    # Add some noise to base encounter cost
    amount_billed = round(base_cost * random.uniform(0.9, 1.3), 2)

    if status == "paid":
        amount_paid = round(amount_billed * random.uniform(0.7, 1.0), 2)
    elif status == "approved":
        amount_paid = round(amount_billed * random.uniform(0.5, 0.8), 2)
    elif status == "denied":
        amount_paid = 0
    else:  # appealed
        amount_paid = round(amount_billed * random.uniform(0.3, 0.6), 2)

    return amount_billed, amount_paid


def generate_processing_days(status):
    if status == "paid":
        return random.randint(3, 10)
    elif status == "approved":
        return random.randint(5, 15)
    elif status == "denied":
        return random.randint(7, 20)
    else:
        return random.randint(10, 30)


# =========================
# Generate Claims
# =========================

claims = []

for _, encounter in encounters_df.iterrows():

    payer = choose_payer()
    status = generate_status(payer["type"])

    base_cost = encounter.get("total_cost", random.uniform(500, 20000))

    amount_billed, amount_paid = generate_amounts(base_cost, status)

    claim = {
        "claim_id": str(uuid.uuid4()),
        "patient_id": encounter["PATIENT"],
        "encounter_id": encounter["Id"],
        "payer_name": payer["name"],
        "payer_type": payer["type"],
        "amount_billed": amount_billed,
        "amount_paid": amount_paid,
        "status": status,
        "processing_days": generate_processing_days(status),
        "denial_reason": random.choice(denial_reasons) if status == "denied" else None,
        "claim_date": fake.date_between(start_date="-2y", end_date="today").isoformat()
    }

    claims.append(claim)

# =========================
# Save Output
# =========================

with open("Claims_v2.json", "w") as f:
    json.dump(claims, f, indent=4)

print(f"Generated {len(claims)} claims successfully")