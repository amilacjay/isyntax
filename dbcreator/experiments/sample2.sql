DROP TABLE IF EXISTS student CASCADE; CREATE TABLE student (
	name VARCHAR(50),
	student_number INTEGER UNIQUE,
	Social_Security_number INTEGER UNIQUE,
	current_address VARCHAR(50),
	phone_number VARCHAR(50) UNIQUE,
	permanent_address VARCHAR(50),
	birth_date DATETIME,
	sex VARCHAR(50),
	class VARCHAR(50),
	major_department VARCHAR(50),
	minor_department INTEGER UNIQUE,
	degree_program VARCHAR(50),
	student VARCHAR(50),
	last_name VARCHAR(50)
);

DROP TABLE IF EXISTS student_number CASCADE; CREATE TABLE student_number (
	values VARCHAR(50) UNIQUE,
	student VARCHAR(50)
);

DROP TABLE IF EXISTS code CASCADE; CREATE TABLE code (
	values VARCHAR(50) UNIQUE,
	department VARCHAR(50)
);

DROP TABLE IF EXISTS course CASCADE; CREATE TABLE course (
	course_name VARCHAR(50),
	description VARCHAR(50),
	course_number INTEGER UNIQUE,
	number_of_semester INTEGER UNIQUE,
	hours VARCHAR(50),
	level VARCHAR(50),
	offering_department VARCHAR(50),
	distance DOUBLE
);

DROP TABLE IF EXISTS section CASCADE; CREATE TABLE section (
	instructor VARCHAR(50),
	semester VARCHAR(50),
	year VARCHAR(50),
	course VARCHAR(50),
	section_number INTEGER UNIQUE
);

DROP TABLE IF EXISTS grade_report CASCADE; CREATE TABLE grade_report (
	student VARCHAR(50),
	section VARCHAR(50),
	letter_grade VARCHAR(50),
	numeric_grade VARCHAR(50)
);


