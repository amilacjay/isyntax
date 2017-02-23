CREATE TABLE student (
	name VARCHAR,
	student_number VARCHAR,
	Social_Security_number VARCHAR,
	current_address VARCHAR,
	phone_number VARCHAR,
	permanent_address VARCHAR,
	phone_number VARCHAR,
	birth_date VARCHAR,
	sex VARCHAR,
	class VARCHAR,
	major_department VARCHAR,
	minor_department VARCHAR,
	degree_program VARCHAR
)

CREATE TABLE student (
	permanent_address VARCHAR,
	student VARCHAR,
	last_name VARCHAR
)

CREATE TABLE student_number (
	values VARCHAR UNIQUE,
	student VARCHAR
)

CREATE TABLE code (
	values VARCHAR UNIQUE,
	department VARCHAR
)

CREATE TABLE course (
	course_name VARCHAR,
	description VARCHAR,
	course_number VARCHAR,
	number VARCHAR,
	semester_hours VARCHAR,
	level VARCHAR,
	department VARCHAR
)

CREATE TABLE section (
	instructor VARCHAR,
	semester VARCHAR,
	year VARCHAR,
	course VARCHAR,
	section_number VARCHAR
)

CREATE TABLE grade_report (
	student VARCHAR,
	section VARCHAR,
	letter_grade VARCHAR,
	numeric_grade VARCHAR
)


