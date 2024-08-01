----- sql joins

A JOIN clause is used to combine rows 
from two or more tables, based on a 
related column between them.

(INNER) JOIN: Returns records that
have matching values in both tables

LEFT (OUTER) JOIN: Returns all records
from the left table, and the matched 
records from the right table

RIGHT (OUTER) JOIN: Returns all records
from the right table, and the matched
records from the left table

FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

https://upload.wikimedia.org/wikipedia/commons/9/9d/SQL_Joins.svg


--- 

Inner Join:

SELECT columns
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;


Left Join:

SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;


Right Join:

SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;


Full Join:

SELECT columns
FROM table1
FULL JOIN table2
ON table1.column_name = table2.column_name;

Cross Join:

SELECT columns
FROM table1
CROSS JOIN table2;


Self Join:

SELECT a.columns, b.columns
FROM table1 a, table1 b
WHERE a.common_column = b.common_column;


--- sql union operator

The UNION operator is used to
combine the result-set of two
 or more SELECT statements.

Every SELECT statement within UNION 
must have the same number of columns

The columns must also have similar 
data types

The columns in every SELECT statement
must also be in the same order



SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;


SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

SELECT 'Customer' AS Type, ContactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers;

--- union all

The UNION operator selects only
distinct values by default. 
To allow duplicate values, use UNION ALL:

SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;


SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;


--- union with where




SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;


SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

---- group by statement

The GROUP BY statement groups rows that 
have the same values into summary rows,
like "find the number of customers in each country".

The GROUP BY statement is often used 
with aggregate functions 
(COUNT(), MAX(), MIN(), SUM(), AVG()) 
to group the result-set by one or more columns.

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);


SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;


SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;

--- group by with join

SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;


--- having

The HAVING clause was added to SQL because 
the WHERE keyword cannot be used 
with aggregate functions.

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

The following SQL statement
lists the number of customers
in each country. Only include
countries with more than 5 customers:

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;


The following SQL statement lists 
the employees that have registered more than 10 orders:

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;


The following SQL statement lists if the employees
"Davolio" or "Fuller" have registered more than 25 
orders:

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
WHERE LastName = 'Davolio' OR LastName = 'Fuller'
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 25;



--- exists operator

The EXISTS operator is used to test 
for the existence of any record in a subquery.

The EXISTS operator returns TRUE 
if the subquery returns one or more records.

SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);


The following SQL statement returns TRUE 
and lists the suppliers with a product 
price less than 20:


SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);


The following SQL statement returns 
TRUE and lists the suppliers with a 
product price equal to 22:

SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22);

--- any and all operators

The ANY and ALL operators allow 
you to perform a comparison 
between a single column value 
and a range of other values.


-- any operator

The ANY operator:

returns a boolean value as a result

returns TRUE if ANY of the subquery values
meet the condition

ANY means that the condition will be
true if the operation is true for 
any of the values in the range.


SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
  (SELECT column_name
  FROM table_name
  WHERE condition);

The following SQL statement lists the 
ProductName if it finds ANY records 
in the OrderDetails table has Quantity 
equal to 10 (this will return TRUE 
because the Quantity column has some 
values of 10):

SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);


The following SQL statement 
lists the ProductName if it
finds ANY records in the
OrderDetails table has 
Quantity larger than 99
(this will return TRUE
because the Quantity 
column has some values larger than 99):


  SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity > 99);


---- all operator

The ALL operator:

returns a boolean value as a result

returns TRUE if ALL of the subquery values meet 
the condition

is used with SELECT, WHERE 
and HAVING statements

ALL means that the condition 
will be true only if the operation
is true for all values in the range.


SELECT ALL column_name(s)
FROM table_name
WHERE condition;


SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL
  (SELECT column_name
  FROM table_name
  WHERE condition);



SELECT ALL ProductName
FROM Products
WHERE TRUE;

The following SQL statement lists 
the ProductName if ALL the records 
in the OrderDetails table has
Quantity equal to 10. This will
of course return FALSE because 
the Quantity column has many
different values (not only the value of 10):

SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);


----------------------

--- select into
--- insert into select
--- case
--- null functions
--- stored procedures
--- comments
--- operators

SELECT Count(*),department, total_employees
FROM employees









