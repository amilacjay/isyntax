DROP TABLE IF EXISTS doctor CASCADE;
CREATE TABLE doctor (
	name VARCHAR(50),
	address VARCHAR(50),
	contact_phones VARCHAR(50),
	area_of_specialization VARCHAR(50),
	PRIMARY KEY()
);

DROP TABLE IF EXISTS Patient CASCADE;
CREATE TABLE Patient (
	name VARCHAR(50),
	address VARCHAR(50),
	phones VARCHAR(50),
	health_record_number INTEGER,
	date_of_birth DATETIME,
	history_of_appointments VARCHAR(50),
	prescriptions VARCHAR(50),
	blood_tests VARCHAR(50),
	diagnoses INTEGER,
	valid_refill INTEGER,
	PRIMARY KEY()
);


