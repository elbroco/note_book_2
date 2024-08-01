----HOW TO CREATE TABLES
CREATE TABLE EmployeeDemographics
( EmployeeID int,
FirstName varchar(50),
LastName varchar(50),
Age int,
Gender varchar(50)
)

CREATE TABLE EmployeeSalary
( EmployeeID int,
JobTitle varchar(50),
Salary int
)         


INSERT INTO EmployeeDemographics VALUES
(1001, 'Jim', 'Halpert', '30', 'Male'),
(1002, 'Pam', 'Beesly', '28', 'Female'),
(1003, 'Michael', 'Scott', '40', 'Male'),
(1004, 'Dwight', 'Schrute', '35', 'Male'),
(1005, 'Angela', 'Martin', '32', 'Female'),
(1006, 'Stanley', 'Hudson', '50', 'Male'),
(1007, 'Kelly', 'Kapoor', '27', 'Female'),
(1008, 'Ryan', 'Howard', '29', 'Male'),
(1009, 'Kevin', 'Malone', '33', 'Male')

INSERT INTO EmployeeSalary VALUES
(1001,'Salesman', 45000),
(1002, 'Manager', 60000),
(1003, 'Engineer', 70000),
(1004, 'Accountant', 55000),
(1005, 'Marketing Specialist', 58000),
(1006, 'HR Coordinator', 50000),
(1007, 'Software Developer', 75000),
(1008, 'Graphic Designer', 48000),
(1009, 'Consultant', 65000)


SELECT statement
top,distinct, count,As ,max, min,avg

SELECT TOP 5 *
FROM EmployeeDemographics

SELECT FirstName LastName
FROM EmployeeDemographics

SELECT DISTINCT(Gender)
FROM EmployeeDemographics

SELECT COUNT(LastName) As LastNameCount
FROM EmployeeDemographics

SELECT Min(Salary)
FROM EmployeeSalary

SELECT Max(Salary)
FROM EmployeeSalary

SELECT AVG(Salary)
FROM EmployeeSalary

-- #doing stuff from other databases

SELECT *
FROM sqltutorial.dbo.EmployeeSalary;4