DROP TABLE IF EXISTS course CASCADE; CREATE TABLE course (
	number INTEGER UNIQUE,
	components VARCHAR(50),
	midterm_exam INTEGER UNIQUE,
	final_exam VARCHAR(50),
	project VARCHAR(50)
);

DROP TABLE IF EXISTS component CASCADE; CREATE TABLE component (
	number_of_points INTEGER UNIQUE,
	weight VARCHAR(50),
	maximum VARCHAR(50),
	points VARCHAR(50),
	weight VARCHAR(50),
	% VARCHAR(50),
	course_grade VARCHAR(50)
);


