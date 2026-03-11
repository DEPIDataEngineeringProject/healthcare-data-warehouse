select * from Claims

select * from Payer

truncate table Payer

------------- repair the calims table ---------

alter table Claims 
drop constraint pk_claims_id

truncate table Payer

alter table Claims 
drop constraint FK_Payer  -- foriegn key refer to payer table


select * from sys.foreign_keys

alter table Claims
drop constraint FK__Claims__patient___6D0D32F4 -- foriegn key refer to patient table

alter table Claims
drop constraint FK__Claims__encounte__6E01572D -- foriegn key refer to Encounter table


select * from sys.foreign_keys

truncate table Claims 
------------ index drop to insert the data agian ----------
drop index idx_claims_patients on Claims 


drop index idx_claims_Encounter on Claims 

drop index idx_claims_payer on Claims 
--------------------- insert again -----------------
BULK INSERT Claims 
FROM 'D:\DEPI\DEPI final project\DATA_SOURCE_SQL\claims_df.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Payer 
FROM 'D:\DEPI\DEPI final project\DATA_SOURCE_SQL\payers.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

select * from sys.foreign_keys

alter table Claims
add constraint FK__Claims__patient___6D0D32F4 FOREIGN KEY (patient_id) 
references Patients(patient_id)

alter table Claims
add constraint FK__Claims__encounte__6E01572D FOREIGN KEY (encounter_id) 
references Encounters (encounter_id)

alter table Claims
add constraint FK__Claims__payers FOREIGN KEY (payer_id) 
references Payer (payer_id)
