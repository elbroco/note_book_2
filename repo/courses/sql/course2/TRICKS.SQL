

-- ENSURES THAT ID(COLUMN) IS EVEN
WHERE id % 2 = 0

-- DIFFERENCE BETWEEN TOTAL VALUES AND UNIQUE VALUES
SELECT COUNT(*) - COUNT(DISTINCT CITY) AS Difference
FROM STATION;

-- COUNTING THE NUMBER OF CHARACTERS
SELECT LENGTH(word_column) AS char_count
FROM your_table
WHERE conditions;

-- Query the two cities in STATION with the shortest
-- and longest CITY names, as well as their respective
-- lengths (i.e.: number of characters in the name).
-- If there is more than one smallest or largest city,
-- choose the one that comes first when ordered alphabetically.
-- The STATION table is described as follows:

(
    SELECT CITY, LENGTH(CITY) AS Length
    FROM STATION
    ORDER BY LENGTH(CITY), CITY
    LIMIT 1
)
UNION ALL
(
    SELECT CITY, LENGTH(CITY) AS Length
    FROM STATION
    ORDER BY LENGTH(CITY) DESC, CITY
    LIMIT 1
);


-- Query the list of CITY names from STATION
--  that either do not start with vowels or do 
--  not end with vowels. Your result cannot contain
--   duplicates.

SELECT DISTINCT CITY
FROM STATION
WHERE 
    LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u')
    OR
    LOWER(RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');


-- Write an SQL query to find the total
--  number of employees in each department 
--  from the employees table. The
--   result should include two 
--   columns: department and total_employees.

SELECT 
    department, 
    COUNT(*) AS total_employees
FROM 
    employees
GROUP BY 
    department;


-- Write an SQL query to find
-- the average salary of employees 
-- in each department from 
-- the employees table. The
-- result should include 
-- two columns: department 
-- and average_salary.


SELECT 
    department, 
    AVG(salary) AS average_salary
FROM 
    employees
GROUP BY 
    department;



