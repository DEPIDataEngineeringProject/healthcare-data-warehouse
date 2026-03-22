----------------claims_index--------------------

create nonclustered index idx_claims_patients
on Claims (patient_id)

create nonclustered index idx_claims_Encounter
on Claims (encounter_id)


----------------coditions_index--------------------

create nonclustered index idx_coditions_patients
on Conditions (patient_id)

create nonclustered index idx_coditions_encounters
on Conditions (Encounter_id)

----------------Encounters_index--------------------

create nonclustered index idx_Encounters_patients
on Encounters (patient_id)

create nonclustered index idx_Encounters_providers
on Encounters (provider_id)

----------------Medications_index--------------------

create nonclustered index idx_Medications_patients
on Medications (patient_id)

create nonclustered index idx_Medications_Encounters
on Medications (Encounter_id)

----------------Providers_index--------------------

create nonclustered index idx_Providers_Organizations
on Providers (organization_id)

