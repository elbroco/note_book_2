--Some of The Most Important SQL Commands
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index


------------------------------------------

-- select sintax

SELECT column1, column2, ...
FROM table_name;


---- selecting all 
select *

--- DISTINCT 
The SELECT DISTINCT 
statement is used to return 
only distinct (different) values.

SELECT DISTINCT column1, column2, ...
FROM table_name;

-- COUNT DISTINCT 

By using the DISTINCT keyword in
a function called COUNT, we can
return the number of different countries.

SELECT COUNT(DISTINCT column1) FROM table_name;


-- WHERE

The WHERE clause
 is used to filter records.

It is used to extract only
 those records that fulfill a specified condition.

SELECT column1, column2, ...
FROM table_name
WHERE condition;

The WHERE clause is not only
used in SELECT statements,
it is also used in UPDATE, DELETE, etc.!


Operator	Description	Example
=	Equal	
>	Greater than	
<	Less than	
>=	Greater than or equal	
<=	Less than or equal	
<>	Not equal. Note: In some versions of SQL this operator may be written as !=	
BETWEEN	Between a certain range	
LIKE	Search for a pattern	
IN	To specify multiple possible values for a column


---- order by

The ORDER BY keyword is used to 
sort the result-set in ascending
or descending order.

SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;


The ORDER BY keyword sorts the records
in ascending order by default. To sort
the records in descending order, use the DESC keyword.

For string values the ORDER BY keyword will order alphabetically:


--ORDER BY Several Columns
The following SQL statement selects all customers
from the "Customers" table, sorted by the "Country"
and the "CustomerName" column. This means that it orders
by Country, but if some rows have the same Country, 
it orders them by CustomerName:

SELECT * FROM Customers
ORDER BY Country, CustomerName;


--Using Both ASC and DESC

SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;

--The SQL AND Operator

The WHERE clause can contain one or many AND operators.

SELECT *
FROM Customers
WHERE Country = 'Spain' AND CustomerName LIKE 'G%';


SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;


--AND vs OR

The AND operator displays a record
 if all the conditions are TRUE.

The OR operator displays a record 
if any of the conditions are TRUE.


-- Combining AND and OR

SELECT * FROM Customers
WHERE Country = 'Spain' AND 
(CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');


--- or operator

SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;

The OR operator is used to filter 
records based on more than one 
condition, like if you want to 
return all customers from Germany 
but also those from Spain:

SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;


---- not operator

The NOT operator is used in combination with
other operators
to give the opposite result, also called the 
negative result.

In the select statement below we want 
to return all customers that are NOT from Spain:

SELECT * FROM Customers
WHERE NOT Country = 'Spain';

SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;


--- not like

SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'A%';


--- not between

SELECT * FROM Customers
WHERE CustomerID NOT BETWEEN 10 AND 60;

--- not in

SELECT * FROM Customers
WHERE City NOT IN ('Paris', 'London');

---- not greater than

SELECT * FROM Customers
WHERE NOT CustomerID > 50;

--- not less than

SELECT * FROM Customers
WHERE NOT CustomerId < 50;

---- INSERT INTO

The INSERT INTO statement is
 used to insert new records in a table.

-- FIRST WAY

Specify both the column names and the 
values to be inserted:

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

-- SECOND WAY
If you are adding values for all 
the columns of the table, you do 
not need to specify the column names
in the SQL query. However, make 
sure the order of the values is
in the same order as the columns
in the table

INSERT INTO table_name
VALUES (value1, value2, value3, ...);


-- INSERT MULTIPLE ROWS

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');



---- NULL VALUES

A field with a NULL value is a field with no value.

If a field in a table is optional, it is 
possible to insert a new record or update
a record without adding a value to this 
field. Then, the field will be saved 
with a NULL value.

A field with a NULL value is one
that has been left blank during
record creation!

-- TESTING FOR NULL VALUES

-- IS NULL 
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;

-- IS NOT NULL

SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;

SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL;

---- UPDATE 
The UPDATE statement is used 
to modify the existing records in a table.

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

Be careful when updating records
in a table! Notice the WHERE clause 
in the UPDATE statement. The WHERE
clause specifies which record(s)
that should be updated. If you 
omit the WHERE clause, all records
in the table will be updated!

UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

--- UPDATE MULTIPLE ROWS

UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';

-- UPDATE WARNING

Be careful when updating records.
If you omit the WHERE clause, 
ALL records will be updated!

UPDATE Customers
SET ContactName='Juan';

---- DELETE

The DELETE statement is used 
to delete existing records in a table.

DELETE FROM table_name WHERE condition;

If you omit the WHERE clause, all records
in the table will be deleted!

DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

--- DELETE ALL RECORDS

DELETE FROM table_name;

--- DELETE A COMPLETE TABLE

DROP TABLE table_name;


--- SELECT TOP 

The SELECT TOP clause is used
to specify the number of records to return.

SELECT TOP 3 * FROM Customers;

MySQL Syntax:

SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

-- ADDING WHERE

SELECT TOP 3 * FROM Customers
WHERE Country='Germany';

SELECT * FROM Customers
WHERE Country='Germany'
LIMIT 3;

--- ADDING ORDER BY

SELECT TOP 3 * FROM Customers
ORDER BY CustomerName DESC;

SELECT * FROM Customers
ORDER BY CustomerName DESC
LIMIT 3;

--- SQL AGGREATE FUNCTIONS


An aggregate function is a function that
performs a calculation on a set of values,
and returns a single value.

Aggregate functions are often used with the
GROUP BY clause of the SELECT statement.
The GROUP BY clause splits the result-set
into groups of values and the aggregate
function can be used to return a single
value for each group.

The most commonly used SQL aggregate functions are:

MIN() - returns the smallest value within the selected column
MAX() - returns the largest value within the selected column
COUNT() - returns the number of rows in a set
SUM() - returns the total sum of a numerical column
AVG() - returns the average value of a numerical column
Aggregate functions ignore null values (except for COUNT()).


---- MIN AND MAX

The MIN() function returns the smallest
 value of the selected column.

SELECT MIN(column_name)
FROM table_name
WHERE condition;

SELECT MIN(Price)
FROM Products;

The MAX() function returns the largest
 value of the selected column.

SELECT MAX(Price)
FROM Products;

SELECT MAX(column_name)
FROM table_name
WHERE condition;

-- ALIAS

SELECT MIN(Price) AS SmallestPrice
FROM Products;

--- ADDING GROUP BY

SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;

---   COUNT

The COUNT() function returns the number of rows
that matches a specified criterion.

SELECT COUNT(column_name)
FROM table_name
WHERE condition;

SELECT COUNT(*)
FROM Products;

--- SPECIFY COLUMN


You can specify a column name instead
of the asterix symbol (*).

If you specify a column name instead of (*),
NULL values will not be counted.

SELECT COUNT(ProductName)
FROM Products;

-- ADD WHERE

SELECT COUNT(ProductID)
FROM Products
WHERE Price > 20;

--- IGNORING DUPLICATES

SELECT COUNT(DISTINCT Price)
FROM Products;

--  ALIAS

SELECT COUNT(*) AS [Number of records]
FROM Products;


-- COUNT AND GROUP BY

SELECT COUNT(*) AS [Number of records], CategoryID
FROM Products
GROUP BY CategoryID;

--- SUM FUNCTION

The SUM() function returns
the total sum of a numeric column.

SELECT SUM(column_name)
FROM table_name
WHERE condition;

SELECT SUM(Quantity)
FROM OrderDetails;

-- ADD WHERE

SELECT SUM(Quantity)
FROM OrderDetails
WHERE ProductId = 11;


-- USE ALIAS

SELECT SUM(Quantity) AS total
FROM OrderDetails;

-- SUM AND GROUP BY
Here we use the SUM() function and
the GROUP BY clause, to return the
Quantity for each OrderID in the
OrderDetails table:

SELECT OrderID, SUM(Quantity) AS [Total Quantity]
FROM OrderDetails
GROUP BY OrderID;


--- SUM WITH EXPRESSIONS

SELECT SUM(Quantity * 10)
FROM OrderDetails;

-- AVG FUNCTION

The AVG() function returns 
the average value of a numeric column.

SELECT AVG(column_name)
FROM table_name
WHERE condition;

SELECT AVG(Price)
FROM Products;

--- add where

SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;

--- add alias

SELECT AVG(Price) AS [average price]
FROM Product

-- higher than average

SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);


-- add group by

SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;

--- like operator

The LIKE operator is used in a
WHERE clause to search for a
specified pattern in a column.

There are two wildcards often used
in conjunction with the LIKE operator:

The percent sign % represents zero, 
one, or multiple characters
The underscore sign _ represents 
one, single character


SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;

SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';


--- wildcards

--- wildcard _
The _ wildcard represents
a single character.

It can be any character or number,
but each _ represents one, and only one, character.

Return all customers from a city that 
starts with 'L' followed by one wildcard
character, then 'nd' and then two wildcard characters:

SELECT * FROM Customers
WHERE city LIKE 'L_nd__';

--- wildcard %

The % wildcard represents any number of characters,
even zero characters.

SELECT * FROM Customers
WHERE city LIKE '%L%';

-- starts with

SELECT * FROM Customers
WHERE CustomerName LIKE 'La%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'a%' OR CustomerName LIKE 'b%';

--- ends with

SELECT * FROM Customers
WHERE CustomerName LIKE '%a';

--- combining
Return all customers 
that starts with "b" and ends with "s":

SELECT * FROM Customers
WHERE CustomerName LIKE 'b%s';

--- contains

Return all customers that contains the phrase 'or'

SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';


--- combining wildcards

Return all customers that starts with
 "a" and are at least 3 characters in length:

SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';



Return all customers that have "r" in the second position:

SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';


--- wildcard []

Return all customers starting
with either "b", "s", or "p":

SELECT * FROM Customers
WHERE CustomerName LIKE '[bsp]%';

---  wildcard -
The - wildcard allows you to specify
a range of characters inside the [] wildcard.

Return all customers starting 
with "a", "b", "c", "d", "e" or "f":

SELECT * FROM Customers
WHERE CustomerName LIKE '[a-f]%';

----  in operator

The IN operator allows you 
 specify multiple values in a WHERE clause.

The IN operator is a shorthand 
for multiple OR conditions.

SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

Return all customers from 'Germany', 'France', or 'UK'

SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

---- not in 

Return all customers that are NOT
 from 'Germany', 'France', or 'UK':

SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');


--- in  / not in (SELECT)

SELECT * FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);

SELECT * FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);

--- between 

The BETWEEN operator selects values within
a given range. The values can be numbers, text, or dates.

The BETWEEN operator is inclusive:
begin and end values are included. 

Selects all products with a price between 10 and 20:

SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;


---- not between

SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;

---- between with in

The following SQL statement
selects all products with a price
between 10 and 20. In addition, 
the CategoryID must be either 1,2, or 3:


SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID IN (1,2,3);

--- between text values

The following SQL statement selects all 
products with a ProductName alphabetically
between Carnarvon Tigers and Mozzarella di Giovanni:


SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;


SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;


--- between dates

SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;

SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';

--- ALIASES

Aliases are often used to make column names more readable.

SELECT column_name(s)
FROM table_name AS alias_name;

SELECT column_name AS alias_name
FROM table_name;


SELECT CustomerID AS ID
FROM Customers;

AS IS optional

SELECT CustomerID ID
FROM Customers;

--- ALIAS FOR COLUMNS

SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;

---Using Aliases With a Space Character

SELECT ProductName AS [My Great Products]
FROM Products;

SELECT ProductName AS "My Great Products"
FROM Products;


--- CONCATENATE COLUMNS

SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;

SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;




































