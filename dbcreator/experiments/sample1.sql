DROP TABLE IF EXISTS department CASCADE; CREATE TABLE department (
	name VARCHAR(50) UNIQUE,
	number VARCHAR(50) UNIQUE,
	particular_employee VARCHAR(50),
	department VARCHAR(50)
);

DROP TABLE IF EXISTS department CASCADE; CREATE TABLE department (
	several_locations VARCHAR(50)
);

DROP TABLE IF EXISTS projects CASCADE; CREATE TABLE projects (
	name VARCHAR(50) UNIQUE,
	number VARCHAR(50) UNIQUE,
	single_location VARCHAR(50)
);

DROP TABLE IF EXISTS employee CASCADE; CREATE TABLE employee (
	name VARCHAR(50),
	Social_Security_number VARCHAR(50),
	address VARCHAR(50),
	sex VARCHAR(50),
	birth_date VARCHAR(50)
);

DROP TABLE IF EXISTS dependent CASCADE; CREATE TABLE dependent (
	first_name VARCHAR(50),
	sex VARCHAR(50),
	birth_date VARCHAR(50),
	relationship VARCHAR(50),
	employee VARCHAR(50)
);


