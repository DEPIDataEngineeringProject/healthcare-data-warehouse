CREATE DATABASE HealthCareDB

USE HealthCareDB

CREATE TABLE Patients (
	patient_id uniqueidentifier PRIMARY KEY,
	first_name NVARCHAR(50) NOT NULL,
    middle_name NVARCHAR(50),
	last_name NVARCHAR(50) ,
	birth_date DATE,
	gender char(1),
	race NVARCHAR(50),
	city NVARCHAR(50),
	insurace_type float 
)

create table Providers (
	provider_id uniqueidentifier PRIMARY KEY,
	name NVARCHAR(100) NOT NULL,
	specialty NVARCHAR(100),
	organization_id int,
	city NVARCHAR(50),
)
create table Organizations (
	id int PRIMARY KEY,
	name NVARCHAR(100) NOT NULL,
	city NVARCHAR(50),
	state NVARCHAR(50),
)
alter table Providers
add constraint FK_Providers FOREIGN KEY (organization_id) 
REFERENCES Organizations(id) on delete cascade 
on update cascade

CREATE TABLE Encounters (
	encounter_id uniqueidentifier PRIMARY KEY,
	patient_id uniqueidentifier,
	provider_id uniqueidentifier,
	encounter_type NVARCHAR(50),
	start_time DATETIME,
	end_time DATETIME,
	totel_cost DECIMAL(10, 2),
)
alter table Encounters 
add constraint FK_patient foreign key (patient_id) 
references Patients(patient_id) on delete cascade
on update cascade

alter table Encounters 
add constraint FK_provider foreign key (provider_id) 
references Providers (provider_id) on delete cascade
on update cascade


create table Claims (
	claim_id uniqueidentifier PRIMARY KEY,
	patient_id uniqueidentifier foreign key references Patients(patient_id),
	encounter_id uniqueidentifier foreign key references Encounters (encounter_id),
	payer_id int,
	amount_billed DECIMAL(10, 2),
	amount_paid DECIMAL(10, 2),
	Status  NVARCHAR(50),
)

create table Payer(
	payer_id int PRIMARY KEY,
	payer_name nvarchar(100)
)

alter table Claims
add constraint FK_Payer foreign key (payer_id) 
references Payer (payer_id) 
on delete cascade 
on update cascade

create table Conditions (
	condition_id uniqueidentifier PRIMARY KEY,
	patient_id uniqueidentifier foreign key references Patients(patient_id),
	Encounter_id uniqueidentifier foreign key references Encounters (encounter_id),
	icd10_code NVARCHAR(10),
	decription NVARCHAR(255),
	onset_date DATE,
	resolved_date DATE,
)

create table Medications (
	medication_id uniqueidentifier PRIMARY KEY,
	patient_id uniqueidentifier foreign key references Patients(patient_id),
	encounter_id uniqueidentifier foreign key references Encounters (encounter_id),
	drug_code NVARCHAR(50),
	description NVARCHAR(255),
	start_date DATE,
	stop_date DATE,
	cost DECIMAL(10, 2),
)

CREATE TABLE vital_signs (
    vital_id BIGINT PRIMARY KEY,
    patient_id UNIQUEIDENTIFIER,
    heart_rate INT,
    systolic_bp INT,
    diastolic_bp INT,
    temp DECIMAL(4,1),
	spo2 DECIMAL(4,1),
    timestamp DATETIME,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
)

