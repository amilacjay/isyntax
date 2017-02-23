CREATE TABLE department (
	name VARCHAR UNIQUE,
	number VARCHAR UNIQUE,
	particular_employee VARCHAR,
	department VARCHAR
)

CREATE TABLE department (
	several_locations VARCHAR
)

CREATE TABLE projects (
	name VARCHAR UNIQUE,
	number VARCHAR UNIQUE,
	single_location VARCHAR
)

CREATE TABLE employee (
	name VARCHAR,
	Social_Security_number VARCHAR,
	address VARCHAR,
	sex VARCHAR,
	birth_date VARCHAR
)

CREATE TABLE dependent (
	first_name VARCHAR,
	sex VARCHAR,
	birth_date VARCHAR,
	relationship VARCHAR,
	employee VARCHAR
)


