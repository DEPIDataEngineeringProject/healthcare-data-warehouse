import pandas as pd
import numpy as np
from faker import Faker 

fake = Faker()

patients = pd.read_csv(r'D:\DEPI\DEPI final project\data sources\patients.csv')
encounters = pd.read_csv(r'D:\DEPI\DEPI final project\data sources\encounters.csv')
n_claims = 200_000

sampled_encounters = encounters.sample(n=n_claims, replace=True).reset_index(drop=True)

patient_ids = sampled_encounters["PATIENT"].values
encounter_ids = sampled_encounters["Id"].values

num_payers = 100000  # Number of unique payers
payer_names = [fake.name() + "" for _ in range(num_payers)]

amount_billed = np.round(np.random.uniform(100, 5000, n_claims), 2)

denial_mask = np.random.rand(n_claims) < 0.18  # 18% denial
status = np.where(denial_mask, "denied", np.random.choice(["approved", "paid"], n_claims))

amount_paid = np.where(denial_mask, 0, np.round(amount_billed * np.random.uniform(0.7, 1.0, n_claims), 2))
denial_reasons = ["Incomplete documentation", "Coverage expired", "Invalid diagnosis code", "Duplicate claim", "Service not covered"]
denial_reason = np.where(denial_mask, np.random.choice(denial_reasons, n_claims), None)

payer_name = np.random.choice( payer_names, n_claims)

claim_id = np.array([np.base_repr(i + np.random.randint(1e6), 36) for i in range(n_claims)])

df = pd.DataFrame({
    "claim_id": claim_id,
    "patient_id": patient_ids,
    "encounter_id": encounter_ids,
    "payer_name": payer_name,
    "amount_billed": amount_billed,
    "amount_paid": amount_paid,
    "status": status,
    "denial_reason": denial_reason
})

df.to_json("claims.json", orient="records", indent=2)
print("the file done")