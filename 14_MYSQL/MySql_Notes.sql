
CREATE DATABASE databasename;
DROP DATABASE databasename;
TRUNCATE TABLE Categories;  -- equivalent to DELETE * FROM tablename;

BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak';

-- creates a differential back up of the database "testDB"
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'
WITH DIFFERENTIAL;


-- constraints 
NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Uniquely identifies a row/record in another table
CHECK - Ensures that all values in a column satisfies a specific condition e.g. CHECK (Age>=18)
DEFAULT - Sets a default value for a column when no value is specified e.g.  City varchar(255) DEFAULT 'Sandnes'
INDEX - Used to create and retrieve data from the database very quickly


/* warning sql server differs on AUTO_INCREMENT and primary key */
CREATE TABLE Customers (
	CustomerID	  int NOT NULL AUTO_INCREMENT,
	CustomerName  varchar(255) NOT NULL,	
	ContactName	  varchar(255),		
	Address 	  varchar(255) NOT NULL,		
	City          varchar(255),		
	PostalCode    varchar(255) NOT NULL,	
	Country       varchar(255),	
	PRIMARY KEY (CustomerID)
);


/* CREATE AND INSERT (note sql server is different*/  
CREATE TABLE new_table_name AS
    (SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....);


/* returns the CREATE TABLE command required to create the table */
SHOW CREATE TABLE <table-name>; 


/* INSERT INTO EXISTING TABLE */
INSERT INTO table1 VALUES (...)
SELECT * from table2 ...

/* IF COLUMNS MATCH ... */
INSERT INTO orders_backup SELECT *  FROM orders where OrdersID < 92000


/* DATE TYPES */
https://www.w3schools.com/sql/sql_datatypes.asp
-- MySQL comes with the following data types for storing a date or a date/time value in the database:

DATE - format YYYY-MM-DD
DATETIME - format: YYYY-MM-DD HH:MI:SS
TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
YEAR - format YYYY or YY


-- MySql Functions
https://www.w3schools.com/sql/sql_ref_mysql.asp
DATE_ADD(NOW(), INTERVAL 5 HOUR)
DATE_SUB("2017-06-15", INTERVAL 10 DAY)


-- CONCAT() function is used to add two or more strings. don't use the '+' operator as with sql server
SELECT CONCAT (string1, string2,�) FROM TableName 


-- MySql LIMIT
SELECT * FROM Customers LIMIT 9;   -- selects first 9 rows
SELECT * FROM Customers LIMIT 3,9; -- selects first 9 starting from the 4th row


-- WARNING the default datatype is 'TEXT' which is a pain to work with and deprecated.  
-- FOR 'TEXT' need to use 'LIKE' instead of '=' in sql query

/* Standard Queries */
SELECT * FROM Customers WHERE Country='Germany' AND City='Berlin';
SELECT * FROM Customers WHERE NOT Country='Germany'
SELECT * FROM Customers WHERE Country='Germany' AND (City='Berlin' OR City='M�nchen');
SELECT * FROM Customers WHERE NOT Country='Germany' AND NOT Country='USA'
SELECT * FROM Customers ORDER BY Country;
SELECT * FROM Customers ORDER BY Country DESC;
SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;
SELECT * FROM Customers WHERE Country is NULL;
SELECT * FROM Customers WHERE CustomerID BETWEEN 45 AND 55;



/* DISTINCT */
SELECT DISTINCT Country from Customers;  -- lists all distinct countries
SELECT COUNT(DISTINCT Country) FROM Customers; -- counts all DISTINCT rows in table Customers
SELECT COUNT(*) FROM Customers; -- counts all rows in table 'Customers'


/* Modifies Tables */
UPDATE Customers
SET ContactName = 'Adolf Hitler', City= 'Hell'   -- NOTE YOU CAN NOT USE 'AND' must use comma ','
WHERE CustomerID = 50;
DELETE FROM Customers WHERE ContactName='Adolf Hitler';



/*  % - The percent sign represents zero, one, or multiple characters
    _ - The underscore represents a single character  */
SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';

/* [charlist] - Defines sets and ranges of characters to match
   [^charlist] or [!charlist] - Defines sets and ranges of characters NOT to match */

-- The following SQL statement selects all customers with a City starting with "b", "s", or "p":
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';

--The following SQL statement selects all customers with a City starting with "a", "b", or "c":
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';

-- using NOT
SELECT * FROM Customers
WHERE City NOT LIKE '[a-r]%';



/*SUB Query*/
SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);

/*BETWEEN*/
SELECT * FROM Orders
WHERE OrderDate BETWEEN '07/04/1996' AND '07/09/1996';  /* INCLUDES 07/04 EXCLUDES 07/09 unless you write as '07/09/1996 23:23:59'  */

/*ALIASES*/
SELECT CustomerID as ID, CustomerName AS Customer
FROM Customers;



SELECT * from Orders where CustomerID in (9,10,11)
SELECT * from Orders where CustomerID not in (9,10,11)
/* WARNING THIS WILL NOT RETURN ANYTHING FOR SOME REASON CAN NOT HAVE NULL IN THE SET */
SELECT * from Orders where CustomerID not in (9,10,11,NULL) 


/*join two tables*/
SELECT O.OrderID, C.CustomerName, O.OrderDate,  
FROM Orders as O INNER JOIN Customers as C ON O.CustomerID=C.CustomerID
WHERE C.CustomerID = 9;



/*join 3 tables*/
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

/*left join keeps all left table data populating with NULL from right data
  if there is no match*/
SELECT C.CustomerName, O.OrderID
FROM Customers as C LEFT JOIN Orders as O 
ON C.CustomerID = O.CustomerID
ORDER BY C.CustomerName;

/*right join*/
SELECT O.OrderID, E.LastName
FROM Orders as O RIGHT JOIN Employees as E 
ON O.EmployeeID = E.EmployeeID
ORDER BY O.OrderID;

/*outer join */
SELECT C.CustomerName, O.OrderID
FROM Customers as C  FULL OUTER JOIN Orders as O
ON C.CustomerID=O.CustomerID
ORDER BY C.CustomerName;


/*self join - joins table with itself adding WHERE conditions*/
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID  AND A.City = B.City 
ORDER BY A.City;


 -- here is good example 
 
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

SELECT
    a.Name as Employee
FROM
    Employee as a
        JOIN Employee as b on a.ManagerID = b.Id
WHERE a.Salary > b.Salary


/*UNION example - same number of columns and matchable datatypes in each */
/* change to UNION ALL if you want to include repeat records in your result*/
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION  
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;


/*The GROUP BY statement is often used with aggregate functions 
(COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.*/

SELECT COUNT(CustomerID) FROM Customers

SELECT COUNT(CustomerID), Country FROM Customers
GROUP BY Country;


SELECT S.ShipperName, O.OrderID
FROM Orders as O LEFT JOIN Shippers as S 
ON O.ShipperID = S.ShipperID
ORDER BY ShipperName;

SELECT S.ShipperName, COUNT(O.OrderID) AS NumberOfOrders 
FROM Orders as O LEFT JOIN Shippers as S 
ON O.ShipperID = S.ShipperID
GROUP BY ShipperName;


/*HAVING examples*/
/*HAVING is used for a condition on the Aggregate using GROUP, WHERE would not work
this is in the case that the condition is a function of the aggregate value and 
not a function of one of the columns */
/*group-count customers for a country when they are more than five*/
/* You can use HAVING for duplicate checks */

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;


SELECT E.LastName, COUNT(O.OrderID) AS NumberOfOrders
FROM Orders as O INNER JOIN Employees as E ON O.EmployeeID = E.EmployeeID
GROUP BY LastName
HAVING COUNT(O.OrderID) > 10;






/* MySQL 8.0 introduces a rank() function - otherwise you need to self join*/

/* RANK() FUNCTION will numerate the rows based on a specific column (OrderID) and can have a separate account for the PARTITION (EmployeeID*/
/* ROW_NUMBER() IS similar but will enumerate rows as 1, 2, 3 even if they are identical when ordered
/* REMEMBER, you can use multiple fields for ORDER BY command 
/* Ranks all orders,  Latest order has xrank = 1 */
SELECT EmployeeID, OrderID,
       RANK() OVER (ORDER BY OrderID DESC) xrank  -- NOTE Missing 'AS'
FROM Orders ORDER BY xrank


/* NOTE USING RANK() FOR MYSQL  REMOVE THE WORD 'AS' e.g. */
SELECT EmployeeID, OrderID,
       RANK() OVER (PARTITION BY EmployeeID ORDER BY OrderID DESC) xrank
FROM Orders ORDER BY EmployeeID


/* USE SELF JOIN AS ALTERNATIVE TO RANK */
SELECT  A.CategoriesID,  A.CategoryName, B.CategoriesID, B.CategoryName
FROM  categories A, categories B
Where A.CategoriesID <> B.CategoriesID AND A.CategoryName = B.CategoryName


/* dump and reload database */

mysqldump db_name t1 > dump.sql
mysql db_name < dump.sql



/* FOR MYSQL USE */
CREATE TABLE new_tbl AS (SELECT * FROM orig_tbl);

/* EXISTS keyword */
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE SupplierId = Suppliers.supplierId AND Price < 20)


/* this didn't work for ecusad, maybe version is too old */
-- mysqlcheck -u root -p --auto-repair --check --optimize --all-databases

/* SEE INDEXES */
SHOW INDEX FROM tblname FROM dbname;

/* CREATES REGULAR INDEX ON COLUMN=POLICY_SUFFIX */
CREATE INDEX idx_POLICY_SUFFIX ON POLICY_COVERAGE2 (POLICY_SUFFIX);  

/* CREATES REGULAR INDEX ALL VALUES MUST BE UNIQUE IN THE COLUMN*/
/* WARNING - the UNIQUE keyword seems to make no difference in MySql 5.6 innodb 
all keys are required to be unique */
CREATE UNIQUE INDEX idx_POLICY_SUFFIX ON POLICY_COVERAGE2 (POLICY_SUFFIX); 

/* COMBINATION INDEX */
CREATE INDEX idx_pname ON Persons (LastName, FirstName);


/* FOR MYSQL INNO */
-- When you define a primary key for an InnoDB table, MySQL uses the primary key as the clustered index 


/* Drops specific Index differs to sql server */
ALTER TABLE table_name DROP INDEX index_name;
	


/* ******* DELETE ALL CONSTRAINTS / KEYS **************** */
--TEMP DISABLE FOREIGN KEYS FOR DELETION
SET FOREIGN_KEY_CHECKS=0
DELETE FROM tscapp.dashboard_policy WHERE customer_id in
(7465687900100103060,
 7585827310230113750,
 7565657600176103140, 
 8372666509445114280, 
 7469776521503114290, 
 8673867300496103140, 
 6869686900036103060, 
 8472847211622114110, 
 8365776500005117870, 
 8673326700075103140,  
 8384327200930112300)
SET FOREIGN_KEY_CHECKS=1   -- RE-ENABLE FOREIGN KEYS


