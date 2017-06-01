-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 28, 2017 at 05:04 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `company_new`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `Department_name` varchar(15) NOT NULL,
  `Department_number` int(11) NOT NULL,
  `Manager_ssn` char(9) NOT NULL,
  `Manager_start_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`Department_name`, `Department_number`, `Manager_ssn`, `Manager_start_date`) VALUES
('Headquarters', 1, '888665555', '1981-06-19'),
('Administration', 4, '987654321', '1995-01-01'),
('Research', 5, '333445555', '1988-05-22');

-- --------------------------------------------------------

--
-- Table structure for table `department_locations`
--

CREATE TABLE `department_locations` (
  `Department_number` int(11) NOT NULL,
  `Department_location` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department_locations`
--

INSERT INTO `department_locations` (`Department_number`, `Department_location`) VALUES
(1, 'Houston'),
(4, 'Stafford'),
(5, 'Bellaire'),
(5, 'Houston'),
(5, 'Sugarland');

-- --------------------------------------------------------

--
-- Table structure for table `dependent`
--

CREATE TABLE `dependent` (
  `Employee_ssn` char(9) NOT NULL,
  `Dependent_name` varchar(15) NOT NULL,
  `Sex` char(1) DEFAULT NULL,
  `Birthdate` date DEFAULT NULL,
  `Relationship` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dependent`
--

INSERT INTO `dependent` (`Employee_ssn`, `Dependent_name`, `Sex`, `Birthdate`, `Relationship`) VALUES
('123456789', 'Alice', 'F', '1988-12-30', 'DAUGHTER'),
('123456789', 'Elizabeth', 'F', '1967-05-05', 'SPOUSE'),
('123456789', 'Michael', 'M', '1988-01-04', 'SON'),
('333445555', 'Alice', 'F', '1986-04-05', 'DAUGHTER'),
('333445555', 'Joy', 'F', '1958-05-03', 'SPOUSE'),
('333445555', 'Theodore', 'M', '1983-10-25', 'SON'),
('987654321', 'Abner', 'M', '1942-02-28', 'SPOUSE');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Name` varchar(40) NOT NULL,
  `Ssn` char(9) NOT NULL,
  `Birthdate` date DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Sex` char(1) DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `Supervisor_ssn` char(9) DEFAULT NULL,
  `Department_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Name`, `Ssn`, `Birthdate`, `Address`, `Sex`, `Salary`, `Supervisor_ssn`, `Department_number`) VALUES
('John B Smith', '123456789', '1965-01-09', NULL, 'M', '30000.00', '333445555', 5),
('Franklin T Wong', '333445555', '1955-12-08', NULL, 'M', '40000.00', '888665555', 5),
('Joyce A English', '453453453', '1972-07-31', NULL, 'F', '25000.00', '987654321', 5),
('Ramesh K Narayan', '666884444', '1962-09-15', NULL, 'M', '38000.00', '888665555', 5),
('James E Borg', '888665555', '1937-11-10', NULL, 'M', '55000.00', '333445555', 1),
('Jennifer S Wallace', '987654321', '1941-06-20', NULL, 'F', '43000.00', '333445555', 4),
('Ahmad V Jabbar', '987987987', '1969-03-29', NULL, 'M', '25000.00', '987654321', 4),
('Alicia J Zelaya', '999887777', '1968-07-19', '', 'F', '25000.00', NULL, 4);

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `Project_name` varchar(15) NOT NULL,
  `Project_number` int(11) NOT NULL,
  `Project_location` varchar(15) DEFAULT NULL,
  `Department_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`Project_name`, `Project_number`, `Project_location`, `Department_number`) VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4);

-- --------------------------------------------------------

--
-- Table structure for table `workplace`
--

CREATE TABLE `workplace` (
  `Employee_ssn` char(9) NOT NULL,
  `Project_number` int(11) NOT NULL,
  `Hours` decimal(3,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `workplace`
--

INSERT INTO `workplace` (`Employee_ssn`, `Project_number`, `Hours`) VALUES
('123456789', 1, '32.0'),
('123456789', 2, '7.0'),
('333445555', 2, '10.0'),
('333445555', 3, '10.0'),
('333445555', 10, '10.0'),
('333445555', 20, '10.0'),
('453453453', 1, '20.0'),
('453453453', 2, '20.0'),
('666884444', 3, '40.0'),
('987654321', 20, '15.0'),
('987654321', 30, '20.0'),
('987987987', 10, '35.0'),
('987987987', 30, '5.0'),
('999887777', 10, '10.0'),
('999887777', 30, '10.0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`Department_number`),
  ADD UNIQUE KEY `Dname` (`Department_name`),
  ADD KEY `department_employee` (`Manager_ssn`);

--
-- Indexes for table `department_locations`
--
ALTER TABLE `department_locations`
  ADD PRIMARY KEY (`Department_number`,`Department_location`);

--
-- Indexes for table `dependent`
--
ALTER TABLE `dependent`
  ADD PRIMARY KEY (`Employee_ssn`,`Dependent_name`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Ssn`),
  ADD KEY `employee_department` (`Department_number`),
  ADD KEY `employee_employee` (`Supervisor_ssn`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`Project_number`),
  ADD UNIQUE KEY `Pname` (`Project_name`),
  ADD KEY `project_department` (`Department_number`);

--
-- Indexes for table `workplace`
--
ALTER TABLE `workplace`
  ADD PRIMARY KEY (`Employee_ssn`,`Project_number`),
  ADD KEY `works_project` (`Project_number`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `department_employee` FOREIGN KEY (`Manager_ssn`) REFERENCES `employee` (`Ssn`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `department_locations`
--
ALTER TABLE `department_locations`
  ADD CONSTRAINT `location_department` FOREIGN KEY (`Department_number`) REFERENCES `department` (`Department_number`);

--
-- Constraints for table `dependent`
--
ALTER TABLE `dependent`
  ADD CONSTRAINT `Dependent_Employee` FOREIGN KEY (`Employee_ssn`) REFERENCES `employee` (`Ssn`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_department` FOREIGN KEY (`Department_number`) REFERENCES `department` (`Department_number`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `employee_employee` FOREIGN KEY (`Supervisor_ssn`) REFERENCES `employee` (`Ssn`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `project_department` FOREIGN KEY (`Department_number`) REFERENCES `department` (`Department_number`);

--
-- Constraints for table `workplace`
--
ALTER TABLE `workplace`
  ADD CONSTRAINT `works_employee` FOREIGN KEY (`Employee_ssn`) REFERENCES `employee` (`Ssn`),
  ADD CONSTRAINT `works_project` FOREIGN KEY (`Project_number`) REFERENCES `project` (`Project_number`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
