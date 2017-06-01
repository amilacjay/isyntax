-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2017 at 09:54 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `university`
--

-- --------------------------------------------------------

--
-- Table structure for table `advisor`
--

CREATE TABLE `advisor` (
  `student_id` varchar(5) NOT NULL,
  `instructor_id` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `advisor`
--

INSERT INTO `advisor` (`student_id`, `instructor_id`) VALUES
('12345', '10101'),
('44553', '22222'),
('45678', '22222'),
('00128', '45565'),
('76543', '45565'),
('23121', '76543'),
('98988', '76766'),
('76653', '98345'),
('98765', '98345');

-- --------------------------------------------------------

--
-- Table structure for table `classroom`
--

CREATE TABLE `classroom` (
  `building` varchar(15) NOT NULL,
  `room_number` varchar(7) NOT NULL,
  `capacity` decimal(4,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `classroom`
--

INSERT INTO `classroom` (`building`, `room_number`, `capacity`) VALUES
('Packard', '101', '500'),
('Painter', '514', '10'),
('Taylor', '3128', '70'),
('Watson', '100', '30'),
('Watson', '120', '50');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_id` varchar(8) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `department_name` varchar(20) DEFAULT NULL,
  `credits` decimal(2,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `title`, `department_name`, `credits`) VALUES
('BIO-101', 'Intro. to Biology', 'Biology', '4'),
('BIO-301', 'Genetics', 'Biology', '4'),
('BIO-399', 'Computational Biology', 'Biology', '3'),
('CS-101', 'Intro. to Computer Science', 'Computer Science', '4'),
('CS-190', 'Game Design', 'Computer Science', '4'),
('CS-315', 'Robotics', 'Computer Science', '3'),
('CS-319', 'Image Processing', 'Computer Science', '3'),
('CS-347', 'Database System Concepts', 'Computer Science', '3'),
('EE-181', 'Intro. to Digital Systems', 'Electrical Eng', '3'),
('FIN-201', 'Investment Banking', 'Finance', '3'),
('HIS-351', 'World History', 'History', '3'),
('MU-199', 'Music Video Production', 'Music', '3'),
('PHY-101', 'Physical Principles', 'Physics', '4');

-- --------------------------------------------------------

--
-- Table structure for table `instructor`
--

CREATE TABLE `instructor` (
  `instructor_id` varchar(5) NOT NULL,
  `instructor_name` varchar(20) NOT NULL,
  `department_name` varchar(20) DEFAULT NULL,
  `salary` decimal(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `instructor`
--

INSERT INTO `instructor` (`instructor_id`, `instructor_name`, `department_name`, `salary`) VALUES
('10101', 'Srinivasan', 'Computer Science', '65000.00'),
('12121', 'Wu', 'Finance', '90000.00'),
('15151', 'Mozart', 'Music', '40000.00'),
('22222', 'Einstein', 'Physics', '95000.00'),
('32343', 'El Said', 'History', '60000.00'),
('33456', 'Gold', 'Physics', '87000.00'),
('45565', 'Katz', 'Computer Science', '75000.00'),
('58583', 'Califieri', 'History', '62000.00'),
('76543', 'Singh', 'Finance', '80000.00'),
('76766', 'Crick', 'Biology', '72000.00'),
('83821', 'Brandt', 'Computer Science', '92000.00'),
('98345', 'Kim', 'Electrical Eng', '80000.00');

-- --------------------------------------------------------

--
-- Table structure for table `prerequisite`
--

CREATE TABLE `prerequisite` (
  `course_id` varchar(8) NOT NULL,
  `prerequisite_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prerequisite`
--

INSERT INTO `prerequisite` (`course_id`, `prerequisite_id`) VALUES
('BIO-301', 'BIO-101'),
('BIO-399', 'BIO-101'),
('CS-190', 'CS-101'),
('CS-315', 'CS-101'),
('CS-319', 'CS-101'),
('CS-347', 'CS-101'),
('EE-181', 'PHY-101');

-- --------------------------------------------------------

--
-- Table structure for table `section`
--

CREATE TABLE `section` (
  `course_id` varchar(8) NOT NULL,
  `section_id` varchar(8) NOT NULL,
  `semester` varchar(6) NOT NULL,
  `started_year` decimal(4,0) NOT NULL,
  `building` varchar(15) DEFAULT NULL,
  `room_number` varchar(7) DEFAULT NULL,
  `time_slot` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `section`
--

INSERT INTO `section` (`course_id`, `section_id`, `semester`, `started_year`, `building`, `room_number`, `time_slot`) VALUES
('BIO-101', '1', 'Summer', '2009', 'Painter', '514', 'B'),
('BIO-301', '1', 'Summer', '2010', 'Painter', '514', 'A'),
('CS-101', '1', 'Fall', '2009', 'Packard', '101', 'H'),
('CS-101', '1', 'Spring', '2010', 'Packard', '101', 'F'),
('CS-190', '1', 'Spring', '2009', 'Taylor', '3128', 'E'),
('CS-190', '2', 'Spring', '2009', 'Taylor', '3128', 'A'),
('CS-315', '1', 'Spring', '2010', 'Watson', '120', 'D'),
('CS-319', '1', 'Spring', '2010', 'Watson', '100', 'B'),
('CS-319', '2', 'Spring', '2010', 'Taylor', '3128', 'C'),
('CS-347', '1', 'Fall', '2009', 'Taylor', '3128', 'A'),
('EE-181', '1', 'Spring', '2009', 'Taylor', '3128', 'C'),
('FIN-201', '1', 'Spring', '2010', 'Packard', '101', 'B'),
('HIS-351', '1', 'Spring', '2010', 'Painter', '514', 'C'),
('MU-199', '1', 'Spring', '2010', 'Packard', '101', 'D'),
('PHY-101', '1', 'Fall', '2009', 'Watson', '100', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `ID` varchar(5) NOT NULL,
  `student_name` varchar(20) NOT NULL,
  `depatment_name` varchar(20) DEFAULT NULL,
  `total_credits` decimal(3,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`ID`, `student_name`, `depatment_name`, `total_credits`) VALUES
('00128', 'Zhang', 'Computer Science', '102'),
('12345', 'Shankar', 'Computer Science', '32'),
('19991', 'Brandt', 'History', '80'),
('23121', 'Chavez', 'Finance', '110'),
('44553', 'Peltier', 'Physics', '56'),
('45678', 'Levy', 'Physics', '46'),
('54321', 'Williams', 'Computer Science', '54'),
('55739', 'Sanchez', 'Music', '38'),
('70557', 'Snow', 'Physics', '0'),
('76543', 'Brown', 'Computer Science', '58'),
('76653', 'Aoi', 'Electrical Eng', '60'),
('98765', 'Bourikas', 'Electrical Eng', '98'),
('98988', 'Tanaka', 'Biology', '120');

-- --------------------------------------------------------

--
-- Table structure for table `takes`
--

CREATE TABLE `takes` (
  `ID` varchar(5) NOT NULL,
  `course_id` varchar(8) NOT NULL,
  `section_id` varchar(8) NOT NULL,
  `semester` varchar(6) NOT NULL,
  `taken_year` decimal(4,0) NOT NULL,
  `grade` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `takes`
--

INSERT INTO `takes` (`ID`, `course_id`, `section_id`, `semester`, `taken_year`, `grade`) VALUES
('00128', 'CS-101', '1', 'Fall', '2009', 'A'),
('00128', 'CS-347', '1', 'Fall', '2009', ''),
('12345', 'CS-101', '1', 'Fall', '2009', 'C'),
('12345', 'CS-190', '2', 'Spring', '2009', 'A'),
('12345', 'CS-315', '1', 'Spring', '2010', 'A'),
('12345', 'CS-347', '1', 'Fall', '2009', 'A'),
('19991', 'HIS-351', '1', 'Spring', '2010', 'B'),
('23121', 'FIN-201', '1', 'Spring', '2010', 'C+'),
('44553', 'PHY-101', '1', 'Fall', '2009', 'B-'),
('45678', 'CS-101', '1', 'Fall', '2009', 'F'),
('45678', 'CS-101', '1', 'Spring', '2010', 'B+'),
('45678', 'CS-319', '1', 'Spring', '2010', 'B'),
('54321', 'CS-101', '1', 'Fall', '2009', 'A-'),
('54321', 'CS-190', '2', 'Spring', '2009', 'B+'),
('55739', 'MU-199', '1', 'Spring', '2010', 'A-'),
('76543', 'CS-101', '1', 'Fall', '2009', 'A'),
('76543', 'CS-319', '2', 'Spring', '2010', 'A'),
('76653', 'EE-181', '1', 'Spring', '2009', 'C'),
('98765', 'CS-101', '1', 'Fall', '2009', 'C-'),
('98765', 'CS-315', '1', 'Spring', '2010', 'B'),
('98988', 'BIO-101', '1', 'Summer', '2009', 'A'),
('98988', 'BIO-301', '1', 'Summer', '2010', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `teaches`
--

CREATE TABLE `teaches` (
  `ID` varchar(5) NOT NULL,
  `course_id` varchar(8) NOT NULL,
  `section_id` varchar(8) NOT NULL,
  `semester` varchar(6) NOT NULL,
  `year_started` decimal(4,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teaches`
--

INSERT INTO `teaches` (`ID`, `course_id`, `section_id`, `semester`, `year_started`) VALUES
('76766', 'BIO-101', '1', 'Summer', '2009'),
('76766', 'BIO-301', '1', 'Summer', '2010'),
('10101', 'CS-101', '1', 'Fall', '2009'),
('45565', 'CS-101', '1', 'Spring', '2010'),
('83821', 'CS-190', '1', 'Spring', '2009'),
('83821', 'CS-190', '2', 'Spring', '2009'),
('10101', 'CS-315', '1', 'Spring', '2010'),
('45565', 'CS-319', '1', 'Spring', '2010'),
('83821', 'CS-319', '2', 'Spring', '2010'),
('10101', 'CS-347', '1', 'Fall', '2009'),
('98345', 'EE-181', '1', 'Spring', '2009'),
('12121', 'FIN-201', '1', 'Spring', '2010'),
('32343', 'HIS-351', '1', 'Spring', '2010'),
('15151', 'MU-199', '1', 'Spring', '2010'),
('22222', 'PHY-101', '1', 'Fall', '2009');

-- --------------------------------------------------------

--
-- Table structure for table `timeslot`
--

CREATE TABLE `timeslot` (
  `timeslot_id` varchar(4) NOT NULL,
  `calender_day` varchar(1) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timeslot`
--

INSERT INTO `timeslot` (`timeslot_id`, `calender_day`, `start_time`, `end_time`) VALUES
('A', 'F', '08:00:00', '08:50:00'),
('A', 'M', '08:00:00', '08:50:00'),
('A', 'W', '08:00:00', '08:50:00'),
('B', 'F', '09:00:00', '09:50:00'),
('B', 'M', '09:00:00', '09:50:00'),
('B', 'W', '09:00:00', '09:50:00'),
('C', 'F', '11:00:00', '11:00:50'),
('C', 'M', '11:00:00', '11:00:50'),
('C', 'W', '11:00:00', '11:00:50'),
('D', 'F', '13:00:00', '13:00:50'),
('D', 'M', '13:00:00', '13:00:50'),
('D', 'W', '13:00:00', '13:00:50'),
('E', 'R', '10:30:00', '11:45:00'),
('E', 'T', '10:30:00', '11:45:00'),
('F', 'R', '14:30:00', '15:45:00'),
('F', 'T', '14:30:00', '15:45:00'),
('G', 'F', '16:00:00', '16:50:00'),
('G', 'M', '16:00:00', '16:50:00'),
('G', 'W', '16:00:00', '16:50:00'),
('H', 'W', '10:00:00', '12:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `university_department`
--

CREATE TABLE `university_department` (
  `department_name` varchar(20) NOT NULL,
  `building` varchar(15) DEFAULT NULL,
  `budget` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `university_department`
--

INSERT INTO `university_department` (`department_name`, `building`, `budget`) VALUES
('Biology', 'Watson', '90000.00'),
('Computer Science', 'Taylor', '100000.00'),
('Electrical Eng', 'Taylor', '85000.00'),
('Finance', 'Painter', '120000.00'),
('History', 'Painter', '50000.00'),
('Music', 'Packard', '80000.00'),
('Physics', 'Watson', '70000.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advisor`
--
ALTER TABLE `advisor`
  ADD PRIMARY KEY (`student_id`,`instructor_id`),
  ADD KEY `advisor_instructor` (`instructor_id`);

--
-- Indexes for table `classroom`
--
ALTER TABLE `classroom`
  ADD PRIMARY KEY (`building`,`room_number`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `department_name` (`department_name`);

--
-- Indexes for table `instructor`
--
ALTER TABLE `instructor`
  ADD PRIMARY KEY (`instructor_id`),
  ADD KEY `department_name` (`department_name`);

--
-- Indexes for table `prerequisite`
--
ALTER TABLE `prerequisite`
  ADD PRIMARY KEY (`course_id`,`prerequisite_id`),
  ADD KEY `prereq_prereq` (`prerequisite_id`);

--
-- Indexes for table `section`
--
ALTER TABLE `section`
  ADD PRIMARY KEY (`course_id`,`section_id`,`semester`,`started_year`),
  ADD KEY `building` (`building`),
  ADD KEY `room_number` (`room_number`),
  ADD KEY `section_classroom` (`building`,`room_number`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `depatment_name` (`depatment_name`);

--
-- Indexes for table `takes`
--
ALTER TABLE `takes`
  ADD PRIMARY KEY (`ID`,`course_id`,`section_id`,`semester`,`taken_year`),
  ADD KEY `takes_section` (`course_id`,`section_id`,`semester`,`taken_year`);

--
-- Indexes for table `teaches`
--
ALTER TABLE `teaches`
  ADD PRIMARY KEY (`ID`,`course_id`,`section_id`,`semester`,`year_started`),
  ADD KEY `teach_course` (`course_id`,`section_id`,`semester`,`year_started`);

--
-- Indexes for table `timeslot`
--
ALTER TABLE `timeslot`
  ADD PRIMARY KEY (`timeslot_id`,`calender_day`,`start_time`);

--
-- Indexes for table `university_department`
--
ALTER TABLE `university_department`
  ADD PRIMARY KEY (`department_name`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `advisor`
--
ALTER TABLE `advisor`
  ADD CONSTRAINT `advisor_instructor` FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`instructor_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `advisor_student` FOREIGN KEY (`student_id`) REFERENCES `student` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_dep` FOREIGN KEY (`department_name`) REFERENCES `university_department` (`department_name`) ON DELETE SET NULL;

--
-- Constraints for table `instructor`
--
ALTER TABLE `instructor`
  ADD CONSTRAINT `instructor_dep` FOREIGN KEY (`department_name`) REFERENCES `university_department` (`department_name`) ON DELETE SET NULL;

--
-- Constraints for table `prerequisite`
--
ALTER TABLE `prerequisite`
  ADD CONSTRAINT `prereq_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `prereq_prereq` FOREIGN KEY (`prerequisite_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `section`
--
ALTER TABLE `section`
  ADD CONSTRAINT `section_classroom` FOREIGN KEY (`building`,`room_number`) REFERENCES `classroom` (`building`, `room_number`) ON DELETE SET NULL,
  ADD CONSTRAINT `section_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_dep` FOREIGN KEY (`depatment_name`) REFERENCES `university_department` (`department_name`) ON DELETE SET NULL;

--
-- Constraints for table `takes`
--
ALTER TABLE `takes`
  ADD CONSTRAINT `takes_section` FOREIGN KEY (`course_id`,`section_id`,`semester`,`taken_year`) REFERENCES `section` (`course_id`, `section_id`, `semester`, `started_year`) ON DELETE CASCADE,
  ADD CONSTRAINT `takes_student` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `teaches`
--
ALTER TABLE `teaches`
  ADD CONSTRAINT `teach_course` FOREIGN KEY (`course_id`,`section_id`,`semester`,`year_started`) REFERENCES `section` (`course_id`, `section_id`, `semester`, `started_year`) ON DELETE CASCADE,
  ADD CONSTRAINT `teaches_instrutor` FOREIGN KEY (`ID`) REFERENCES `instructor` (`instructor_id`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
