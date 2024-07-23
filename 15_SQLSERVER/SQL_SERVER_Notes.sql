/* https://www.sqlservertutorial.net/advanced-sql-server/ */

--  USE https://dbfiddle.uk/  to practice queries

/* Example create */

CREATE TABLE Customers (
CustomerID	  int IDENTITY(1,1) PRIMARY KEY,   /* IDENTITY increments the primary key starting from 1, interval 1 */
CustomerName  varchar(255) NOT NULL,	
ContactName	  varchar(255),		
Address 	  varchar(255) NOT NULL,		
City          varchar(255),		
PostalCode    varchar(255) NOT NULL,	
Country       varchar(255),	
Email         varchar(255) NOT NULL UNIQUE,  /* UNIQUE CONSRTAINT */
AddedDate     date DEFAULT GETDATE()  /* DEFAULT VALUE */
CHECK (Country <> 'Russia')  /* VALUE CONSTRAINT */
);

-- Alter table to set a column 'ID' as UNIQUE
ALTER TABLE Persons ADD UNIQUE(ID);

-- Alter table to set combination of columsn as UNIQUE
ALTER TABLE Persons Add UNIQUE(code,country_name)

/* this table will not be stored after the stored procedure is run, or the query window is closed
   does not need to be dropped */
CREATE TABLE #TempTable(
   LeadID varchar(64),
   RecordID varchar(64),
   FirstName varchar(64),
   LastName varchar(64),
   DateStamp datetime)


/* DATA TYPES */
https://www.w3schools.com/sql/sql_datatypes.asp
--SQL Server comes with the following data types for storing a date or a date/time value in the database:
DATE -- format YYYY-MM-DD
DATETIME -- format: YYYY-MM-DD HH:MI:SS
SMALLDATETIME -- format: YYYY-MM-DD HH:MI:SS
TIMESTAMP -- format: a unique number

-- ADD COLUMN
ALTER TABLE [WangExport].[dbo].[FIVE_SIGMA_PAYMENT_NUMBER]
ADD tax_id_number char(9)

-- DROP COLUMN
ALTER TABLE Customers
DROP COLUMN ContactName;

-- WARNING the default datatype is 'TEXT' which is a pain to work with and deprecated.  
-- FOR 'TEXT' need to use 'LIKE' instead of '=' in sql query

/* You need to do this in correct order due to dependencies */
DROP TABLE Customers;
DROP TABLE Suppliers;
DROP TABLE Employees;
DROP TABLE Shippers;
DROP TABLE Categories;
DROP TABLE Products;
DROP TABLE Orders;
DROP TABLE OrderDetails;

DROP DATABASE Practice;  -- close all open query windows for which DB is in Use 


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

-- Without DEFAULT keyword - note using single quotes for strings
INSERT INTO Messages (user_name, message_txt) VALUES ('ob', 'this is another message');

-- Insert Multiple Rows is significantly faster than consecutive inserts
INSERT INTO Messages (user_name, message_txt)  
VALUES ('ob', 'message 3'),
	   ('ob', 'message 4'),
	   ('ob', 'message 5');
		 
		 

/* Day Of Week Functions Use ... */
SELECT DATENAME(dw,GETDATE()) -- Friday
SELECT DATEPART(dw,GETDATE()) -- 6

/*
year, yyyy, yy = Year
quarter, qq, q = Quarter
month, mm, m = month
dayofyear, dy, y = Day of the year
day, dd, d = Day of the month
week, ww, wk = Week
weekday, dw, w = Weekday
hour, hh = hour
minute, mi, n = Minute
second, ss, s = Second
millisecond, ms = Millisecond
*/


/* DISTINCT */
SELECT DISTINCT Country from Customers;  -- lists all distinct countries
SELECT COUNT(DISTINCT Country) FROM Customers; -- counts all DISTINCT rows in table Customers
SELECT COUNT(*) FROM Customers; -- counts all rows in table 'Customers'
/* Warning: DISTINCT is An Expensive Keyword */

select * from Customers where CustomerID = 50

/* Modifies Tables */
UPDATE Customers
SET ContactName = 'Adolf Hitler', City= 'Hell' 
WHERE CustomerID = 50;

DELETE FROM Customers WHERE ContactName='Adolf Hitler';

SELECT AVG(CustomerID) from Customers;

SELECT AVG(DateDifference) As AvergageTimeToSale,
       STDEV(DateDifference) AS StandardDeviation 
	FROM TMP_AVERAGE_SALE_TIME;
    DROP TABLE TMP_AVERAGE_SALE_TIME;

SELECT TOP 3 * FROM Customers
WHERE Country='Germany';

SELECT TOP 50 PERCENT * FROM Customers;

SELECT MIN(Price) AS SmallestPrice
FROM Products;

	
%   -- Match any string of any length (including 0 length)
_   -- Match one single character
[]  -- Match any characters in the brackets, e.g. [xyz] = x or y or z  Note: [(a-c)] works the same as [abc]
[^] -- Match any character not in the brackets, e.g. [^xyz]            Note: [^(a-c)] works the same as [^abc]	
	
	
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

-- same as above using carrot '^'
SELECT * FROM Customers
WHERE City LIKE '[^(a-r)]%';

-- IN Operator
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');


/* Searching for NOT NULL */
SELECT * FROM Customers 
WHERE CustomerName IS NOT NULL


/* CASE WHEN - THEN - ELSE - END conditions in SELECT */
/* only lists the numeric postal codes */
SELECT CASE WHEN ISNUMERIC(PostalCode) = 1  THEN  PostalCode  ELSE NULL END as COLUMN1
FROM Customers;

SELECT CAST(ISNUMERIC(PostalCode) as bit) FROM Customers

SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);

/* BETWEEN */
SELECT * FROM Orders
WHERE OrderDate BETWEEN '07/04/1996' AND '07/09/1996';  /* INCLUDES 07/04 EXCLUDES 07/09 unless you write as '07/09/1996 23:23:59'  */

/* ALIASES */
SELECT CustomerID as ID, CustomerName AS Customer
FROM Customers;

/* Brackets allow for spaces in Column Name */
SELECT CustomerName AS Customer, ContactName AS [Contact Person]
FROM Customers;

SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;


SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;


SELECT * from Orders where CustomerID = 9
SELECT * from Customers where CustomerID = 9

SELECT * from Orders where CustomerID in (9,10,11)
SELECT * from Orders where CustomerID not in (9,10,11)
/* WARNING THIS WILL NOT RETURN ANYTHING FOR SOME REASON CAN NOT HAVE NULL IN THE SET */
SELECT * from Orders where CustomerID not in (9,10,11,NULL) 


/*join two tables*/
SELECT O.OrderID, C.CustomerName, O.OrderDate,  
FROM Orders as O INNER JOIN Customers as C ON O.CustomerID=C.CustomerID
WHERE C.CustomerID = 9;


/* Note O.* returns all fields only from Orders table */
SELECT O.*
FROM Orders as O INNER JOIN Customers as C ON O.CustomerID=C.CustomerID
WHERE C.CustomerID = 9;


select Top(5) * from Customers
select Top(5) * from Orders order by CustomerID

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

/*outer join  keyword 'OUTER' is not required, only helps distinguish with INNER JOIN*/
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


e.g.

SELECT A, B, SUM(C)
FROM TBL_NAME
GROUP BY A, B

SELECT A, B, AVG(0.25*C + 2.75*D)
FROM TBL_NAME
GROUP BY A, B

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

/* STUFF() function deletes a part of a string and then inserts another part into the string, starting at a specified position */
/* concatenate/aggregate strings of column3  */
SELECT GroupColumn
      ,STUFF((SELECT N', ' + column3 
              FROM tblName AS t2 
              WHERE t2.GroupColumn=t.GroupColumn 
              FOR XML PATH,TYPE).value(N'.','nvarchar(max)'),1,2,'')
FROM tblName AS t
GROUP BY GroupColumn;


/* EXISTS examples, can also be written with a JOIN */
/* lists products available under $20 */
SELECT ProductName FROM Products as P, Suppliers as S WHERE P.SupplierId = S.SupplierId AND P.Price < 20;

/*select suppliers where there EXISTS a product which is under $20 which they supply to us */
SELECT SupplierName FROM Suppliers as S
WHERE EXISTS (SELECT ProductName FROM Products as P WHERE P.SupplierId = S.SupplierId AND P.Price < 20);


/* products priced $22 */
SELECT ProductName FROM Products as P, Suppliers as S WHERE P.SupplierId = S.supplierId AND P.Price = 22

/* Suppliers who supply a product priced $22*/
SELECT SupplierName
FROM Suppliers WHERE EXISTS 
(SELECT ProductName FROM Products WHERE SupplierId = Suppliers.supplierId AND Price = 22);

/* equivalent command using a JOIN */
SELECT S.SupplierName
FROM Suppliers as S INNER JOIN Products as P on  S.SupplierID = P.SupplierID
WHERE P.Price = 22



/* this returns ProductID = 35 & 55 */
SELECT ProductID FROM OrderDetails WHERE Quantity > 99 

/*The ANY or SOME operator returns TRUE if any of the subquery values meet the condition.*/
/* ANY keyword is used for a query meaning ANY of the results of the following query */
SELECT ProductName
FROM Products
WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity > 99);

/*The ALL operator returns TRUE if all of the subquery values meet the condition.*/
/* ALL keyword. returns all products which have sold exactly 10 units in ALL order */
/* can't think of example that returns something */
SELECT OrderID
FROM OrderDetails
WHERE ProductID IN (11,42); = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity > 99);


SELECT DAY(GETDATE()) AS DayOfMonth; --RETRUNS DAY OF THE MONTH
SELECT COALESCE(NULL, NULL, NULL, 'W3Schools.com', NULL, 'Example.com'); -- RETURNS first non-NULL object in list


/* VIEWS get updated with the original data tables*/
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);


/* Query a VIEW */
SELECT * FROM [Products Above Average Price]
WHERE Price BETWEEN 30 AND 32

/* DROP VIEW */
DROP VIEW [Products Above Average Price];


/* T-SQL Window Functions (Nothing to do with the Windows OS) */

-- Introduced in 2005, functionality added in 2012 - WILL NOT WORK FOR ALL VERSIONS
--  TRY THIS: https://towardsdatascience.com/intro-to-window-functions-in-sql-23ecdc7c1ceb
--- TRY THIS: https://towardsdatascience.com/writing-advanced-sql-queries-in-pandas-1dc494a17afe

-- RANK() OVER ... FUNCTION will numerate the rows based on a specific column (OrderID) and can have a separate account for the PARTITION equal values will share rank e.g. 1,1,3,4 
-- ROW_NUMBER() OVER ... is similar but will enumerate rows as 1,2,3,4 even if they are identical when ordered
-- DENSE_RANK() OVER ... is similar but will not skip values as in RANK(),   e.g.  1,1,2,3
-- NTILE(n) OVER ... (ORDER BY ColumnName DESC), will divide ALL of the rows into 'n' groups, or use PARTITION to divide the subgroups into buckets of 'n'
-- SUM(x)  OVER (ORDER BY ColumName) as Tallycolumn ...  this will give the running sum of field 'x' in the PARTITION group
-- AVG(x)  OVER ... this will give the running average of field 'x' in the PARTITION group
-- LAG(x)  OVER ... this will give the value of field 'x' for the previous row in this PARTITION group, or NULL if this is the first
-- LEAD(x) OVER ... this will give the value of field 'x' for the next row in this PARTITION group, or NULL if this is the first
-- FIRST_VALUE(x) OVER ...  this will give the value of field 'x' for the first row in this PARTITION group
-- LAST_VALUE(x) OVER ...  this will give the value of field 'x' for the last row in this PARTITION group


-- ROWS BETWEEN start AND end      (Relative Aggregates Using ROWS BETWEEN)  Oren has not used yet!!
-- RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW   Oren has not used yet!!
-- RANGE BETWEEN FOLLOWING PRECEDING AND CURRENT ROW  Oren has not used yet!!

-- T-SQL in SQL Server 2012
/*
CUME_DIST() OVER ... � calculates the position of a value relative to a group of values
PERCENT_RANK() OVER ... � calculates the percent rank of a value in a group of values
PERCENTILE_CONT(X) WITHIN GROUP (ORDER BY ... � looks at the percent rank of values in a group until it finds one greater than or equal to X.
PERCENTILE_DISC(X) WITHIN GROUP (ORDER BY ... � looks at the cumulative distribution of values in a group until it finds one greater than or equal to X

*/


/* REMEMBER, you can use multiple fields for ORDER BY command 
/* Ranks all orders,  Latest order has xrank = 1 */
SELECT EmployeeID, OrderID,
       RANK() OVER (ORDER BY OrderID DESC) as xrank
FROM Orders ORDER BY xrank


/* Returns a ranked set of orders for partitioned each EmployeeID with xrank == 1 for the latest order */
/* Each Employee ID set has its own ranking */
SELECT EmployeeID, OrderID,
       RANK() OVER (PARTITION BY EmployeeID ORDER BY OrderID DESC) as xrank
FROM Orders ORDER BY EmployeeID


SELECT *, 
	RANK() OVER (PARTITION BY Country ORDER BY SupplierID DESC) as xrank,
	NTILE(2) OVER (PARTITION BY Country ORDER BY SupplierID DESC) as ntile4  -- this divides your ranks into TWO buckets  i.e. xrank=1,3,5 goes into bucket 1,  xrank=2,4,6 goes into bucket 2
FROM Suppliers


SELECT * ,
	RANK() OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as xrank,
	SUM(Quantity) OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as SoldSoFar,
	AVG(Quantity) OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as MovingAverage,
	LAG(OrderID)  OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as PrevOrderID,
	LEAD(OrderID)  OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as NextOrderID,
	FIRST_VALUE(OrderID)  OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as FirstOrderID,
	LAST_VALUE(OrderID)  OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as LastOrderID,
	CUME_DIST()   OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as CumilativeDistribution,
	PERCENT_RANK()   OVER (PARTITION BY ProductID ORDER BY OrderDetailsID) as PercentRank
FROM OrderDetails



/* CTE (Common Table Expression) 'WITH name AS' defines a temporary result set which you can then use in a SELECT statement.  
It becomes a convenient way to manage complicated queries. */
/* Selects the Latest Order for each Employee */

WITH SQL1 AS 
(SELECT EmployeeID, OrderID,
        RANK() OVER (PARTITION BY EmployeeID ORDER BY OrderID DESC) as xrank FROM Orders)
SELECT * FROM SQL1 WHERE xrank = 1

/* DOUBLE CTE STATEMENT */
WITH TBL1 AS (SELECT * ....), TBL2 AS (SELECT * .....)
SELECT * FROM TBL1 INNER JOIN TBL2

/* NESTED CTE QUERY */
WITH TBL1 AS (SELECT * FROM ...),
     TBL2 AS (SELECT * FROM TBL1),
	 TBL3 AS (SELECT * FROM TBL2)
SELECT * FROM TBL3


/* DELETE ALL DUPLICATE ROWS */  
--  I don't think this works,
WITH TMP AS
  (SELECT COL1,COL2,COL3, ROW_NUMBER() OVER (PARTITION BY COL1 ORDER BY COL1 DESC) as xrank
      FROM Table1)
  DELETE FROM TMP WHERE xrank > 1



/* CTE (Common Table Expression) in MySQL may also work in SQL SERVER */
SELECT auto_policy_id, Counter FROM (SELECT  auto_policy_id, count(customer_id) as counter
                                     FROM tscapp.dashboard_policy  
                                     WHERE auto_policy_id IS NOT NULL 
									 GROUP BY auto_policy_id )  as TMP WHERE Counter > 1




/* PRINT A FULL COLUMN AS A LIST */
/*SQL SERVER 2017 */
SELECT STRING_AGG(columnName,',') as list FROM tableName 
/* Earlier Versions */
DECLARE @list varchar (200)
SET @list = ''
SELECT @list = CASE WHEN @list = '' Then columnName ELSE @list + ',' + columnName END
  FROM tableName
PRINT @list


/* NOLOCK keyword does not lock the table from other queries that are being run at that time */
/*
The WITH (NOLOCK) hint is an explicit command directed at a specific table or view used to set the transaction 
isolation level against the table or tables within a view for a query. Once issued, locks will not be used against 
the data within the table. The advantage to this is there is no chance a deadlock will occur against any other queries 
running against the table. The other indirect advantage is that less memory will be used in order to hold locks against that data.
*/
SELECT * FROM Orders WITH (NOLOCK)


/*Move a table from one database to another database SQL Server */ 
select * into DB_2.[dbo].T1 from DB_1.[dbo].[T1]

/* SELECT ... INTO WILL CREATE A NEW TABLE */
SELECT column1, column2, column3, ...
INTO newtable [IN externaldb] -- IN CLAUSE Will crate new table in the external database not the current one you are using
FROM oldtable
WHERE condition;


/* INSERT INTO WILL ADD TO AN EXISTING DATABASE */
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;


INSERT INTO table2
SELECT * FROM table1
WHERE condition;

/* How to label result tables in multiple SELECT output? */
/* this will mark the first field as the name of the table */
Select 'Employee' as TABLE_NAME, * from Employee 


WAITFOR DELAY '00:00:15'  /* pauses the T-SQL for 15 secs */


/* ********************************************************************* */
/* ******************* SQL STORED PROCEDURES *************************** */
/* ******************CAN USE SELECT STATEMENTS************************** */  
/* ********************************************************************* */  
CREATE OR ALTER PROCEDURE [dbo].[SP_VehicleAuto]
	-- Add the parameters for the stored procedure here
	--<@Param1, sysname, @p1> <Datatype_For_Param1, , int> = <Default_Value_For_Param1, , 0>, 
	--<@Param2, sysname, @p2> <Datatype_For_Param2, , int> = <Default_Value_For_Param2, , 0>
AS
BEGIN
	-- SET NOCOUNT ON  added to prevent extra result sets from
	-- interfering with SELECT statements. The Msg tab will not do row counts.
	SET NOCOUNT ON;  -- THIS IS ESSENTIAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!
	DROP TABLE dbo.WEB_VEHICLE_AUTO;
	
    WITH TEMP as (SELECT AutoPolicyID, RANK() OVER (PARTITION BY [UserID] ORDER BY [RowID] DESC) AS Xrank FROM WEB_CUSTOMER)
	SELECT DA_CAR_SYMBOL AS AutoPolicySymbol,
	       CONVERT(int, CONVERT(varchar(6), DA_CAR_ACCOUNT) + CONVERT(varchar(2), DA_CAR_SUFFIX)) AS AutoPolicyID,
	       DA_CAR_RISK_NUM  AS CarNumber,
	       DA_CAR_EFF_DATE  AS CarEffectiveDate,
	       DA_CAR_VID       AS VinNumber,
	       DA_CAR_CAR_YEAR  AS CarYear,
	       dbo.FN_ToProperCase(RTRIM(DA_CAR_CAR_MAKE))  AS CarMake,
	       dbo.FN_ToProperCase(RTRIM(DA_CAR_CAR_MODEL)) AS CarModel,
	       dbo.FN_ToProperCase(RTRIM(DA_CAR_CAR_STYLE)) AS CarStyle
	 INTO dbo.WEB_VEHICLE_AUTO  /* this generates new table, does not require CREATE statement */
	 FROM dbo.POLICY03_AUTO, TEMP
	 WHERE Xrank = 1 AND CONVERT(int, CONVERT(varchar(6), DA_CAR_ACCOUNT) + CONVERT(varchar(2), DA_CAR_SUFFIX)) = AutoPolicyID
	 ORDER by 1,2,3;
     SELECT * FROM WEB_VEHICLE_AUTO;
    -- Insert statements for procedure here
	--SELECT <@Param1, sysname, @p1>, <@Param2, sysname, @p2>
END


/******************************************************************************************/
/******************************************************************************************/
/* STORED PROCEDURE WITH OUTPUTS AND RETURNS */
/******************************************************************************************/
/******************************************************************************************/
CREATE PROCEDURE [dbo].[SP_FINDSTRING]  
	(@str1 varchar(20),@op varchar(100) OUTPUT)

AS

    DECLARE @str2 varchar(100) 
    SET @str2 ='welcome to sql server. Sql server is a product of Microsoft' 
    IF(PATINDEX('%'+@str1 +'%',@str2)>0) 
	BEGIN
        SELECT @op =  @str1+' present in the string' 
		RETURN 0
	END
    ELSE
	BEGIN 
        SELECT @op = @str1+' not present'
		RETURN 1
	END
	
/* Execute using Code */
  DECLARE @output_value VARCHAR(100)
  DECLARE @return_value tinyint
  EXEC @return_value = SP_FINDSTRING 'sql', @output_value OUTPUT  /*don't forget OUTPUT*/
  SELECT @return_value,@output_value
  
 /* Which Produces */ 
 /* 0	sql present in the string */

/******************************************************************************************/
/******************************************************************************************/
/******************************************************************************************/

	
/* RENAMING STORED PROCEDURE */
sp_rename 'GetProductDesc','GetProductDesc_new'



/* ********************************************************************* */
/* SQL FUNCTIONS (TABLE-VALUED / SCALAR-VALUED / AGGREGATE FUNCTIONS )   */
/* ********************************************************************* */
/* ******************CAN NOT USE SELECT STATEMENTS********************** */  
/* Below code with generate a scalar-valued function that will Title Case */
/* RIGHT CLICK AND SELECT MODIFY IF YOU NEED TO UPDATE */
/* Set default value to 'Fred' for name if no parameter is passed */
/*SCALAR-VALUED Example - Only Returns One Value */
CREATE or ALTER FUNCTION [dbo].[FN_ToProperCase](@name nvarchar(500) = 'Fred')
RETURNS nvarchar(500)
AS
BEGIN
declare @pos    int = 1
      , @pos2   int

if (@name <> '')--or @name = lower(@name) collate SQL_Latin1_General_CP1_CS_AS or @name = upper(@name) collate SQL_Latin1_General_CP1_CS_AS)
begin
    set @name = lower(rtrim(@name))
    while (1 = 1)
    begin
        set @name = stuff(@name, @pos, 1, upper(substring(@name, @pos, 1)))
        set @pos2 = patindex('%[- ''.)(]%', substring(@name, @pos, 500))
        set @pos += @pos2
        if (isnull(@pos2, 0) = 0 or @pos > len(@name))
            break
    end
end

return @name
END

/****** TEST EXAMPLE ******/
SELECT dbo.FN_ToProperCase('hello WORld')

/***********************************************************************/
/* TABLE-VALUED Example returning 3 values as a table */
/* Usage example SELECT * FROM dbo.FN_WangHomePremiumCalc(10058132)  */
CREATE FUNCTION dbo.FN_WangHomePremiumCalc
(
	@PolicyID int
)
RETURNS 
@PremiumCalc  TABLE 
(
	AnnualPremium            money
	CoverageACPremium        money
	OtherPremium             money
)
AS
BEGIN
	/****************************/
    /* PROCESSING CODE GOES HERE */
    /****************************/
	INSERT @PremiumCalc
	SELECT @AnnualPremium, @CoverageACPremium, @OtherPremium
	RETURN 
END
GO


/* TEMPORARY FUNCTION for newer versions only */
CREATE TEMPORARY FUNCTION get_gender(type varchar) AS (
   CASE WHEN type = "M" THEN "male"
        WHEN type = "F" THEN "female"
        ELSE "n/a"
   END
)
SELECT
  name,
  get_gender(Type) as gender
FROM bill


/***********************************************************************/
/* T-SQL Loop Through 'YourField' using SQL Query with CURSOR   
/* NOTE THIS TAKES A LONG TIME - BETTER TO DO THE LOOPING IN PYTHON    */
/***********************************************************************/
DECLARE @MyCursor CURSOR;
DECLARE @MyField YourFieldDataType;
BEGIN
    SET @MyCursor = CURSOR FOR
    select YourField from dbo.table  /* 'YourField' generates a list of values for @MyCursor */
        where StatusID = 7      
    OPEN @MyCursor 
	
    FETCH NEXT FROM @MyCursor 
    INTO @MyField

    WHILE @@FETCH_STATUS = 0
    BEGIN
      /*
         YOUR ALGORITHM GOES HERE   
      */
      FETCH NEXT FROM @MyCursor 
      INTO @MyField 
    END; 

    CLOSE @MyCursor ;
    DEALLOCATE @MyCursor;
END;


/********************************************/
/* IF - ELSE for one or multiple statements */
/* PRINT displays on the 'Message' tab ******/
/********************************************/

PRINT(CONVERT (varchar, SYSDATETIME()) +  ' - Yourlabel') -- use this to check seconds timestamp 

IF DATEPART(dw, GETDATE()) = 7 OR DATEPART(dw, GETDATE()) = 1
   PRINT 'It is the weekend.'
ELSE
   PRINT 'It is a weekday.'

IF DATEPART(dw, GETDATE()) = 7 OR DATEPART(dw, GETDATE()) = 1
BEGIN
   PRINT 'It is the weekend.'
   PRINT 'Get some rest on the weekend!'
END
ELSE
BEGIN
   PRINT 'It is a weekday.'
   PRINT 'Get to work on a weekday!'
END

/************************************************/
-- RETURNS SERVER NAME
SELECT @@SERVERNAME

/************************************************/
SELECT 1 / 3 -- INTEGER DIVISION
SELECT CAST(1 AS float) / CAST(3 AS float) -- REGULAR DIVISION

/*  NOTE ON CAST VS CONVERT */
/*
CONVERT is SQL Server specific, CAST is ANSI.
CONVERT is more flexible in that you can format dates etc (see below). Other than that, they are pretty much the same. 
If you don't care about the extended features, use CAST.
For some numerical conversions where CAST should be used to preserve precision.
'FORMAT' T-SQL function available in newer versions
*/

/* Date format with CONVERT */
SELECT 
GETDATE() AS 'GETDATE()', -- 2020-11-17 12:28:59.510
CONVERT(VARCHAR,GETDATE(),100) AS 'Style 100',   -- Nov 17 2020 12:28PM
CONVERT(VARCHAR,GETDATE(),1) AS 'Style 1',       -- 11/17/20
CONVERT(VARCHAR,GETDATE(),101) AS 'Style 101',   -- 11/17/2020
CONVERT(VARCHAR,GETDATE(),7) AS 'Style 7',       -- Nov 17, 20
CONVERT(VARCHAR,GETDATE(),107) AS 'Style 107',   -- Nov 17, 2020
CONVERT(VARCHAR,GETDATE(),8) AS 'Style 8',       -- 12:28:59
CONVERT(VARCHAR,GETDATE(),9) AS 'Style 9',       -- Nov 17 2020 12:28:59:510PM
CONVERT(VARCHAR,GETDATE(),10) AS 'Style 10',     -- 11-17-20
CONVERT(VARCHAR,GETDATE(),110) AS 'Style 110',   -- 11-17-2020
CONVERT(VARCHAR,GETDATE(),11) AS 'Style 11',     -- 20/11/17
CONVERT(VARCHAR,GETDATE(),111) AS 'Style 111',   -- 2020/11/17
CONVERT(VARCHAR,GETDATE(),12) AS 'Style 12',     -- 201117
CONVERT(VARCHAR,GETDATE(),112) AS 'Style 112',   -- 20201117
CONVERT(VARCHAR,GETDATE(),14) AS 'Style 13'      -- 12:28:59:510


DECLARE @cmd VARCHAR(500)
SET @cmd =  'bcp  "Select top 3 INV_ACCOUNT_NUMBER, INV_SUFFIX from WangExport.dbo.INVOICE" queryout "C:\AIT\NewPolicyData\test101.csv" -w -C OEM -t"," -T -S '+@@servername    
print @cmd
EXEC master..xp_cmdshell @cmd


/* RUN THIS TO ENABLE xp_cmdshell use  one line at a time ending with 'GO' */

EXEC sp_configure 'show advanced options', 1
GO
RECONFIGURE
GO

EXEC sp_configure 'xp_cmdshell', 1
GO
RECONFIGURE
GO

/* Example use of the command line function 'bcp' which you could run from a command line on the server.  This runs it in T-SQL */
DECLARE @cmd VARCHAR(500)
SET @cmd =  'bcp  "Select top 3 INV_ACCOUNT_NUMBER, INV_SUFFIX from WangExport.dbo.INVOICE" queryout "C:\AIT\NewPolicyData\test101.csv" -w -C OEM -t"," -T -S '+@@servername    
print @cmd
EXEC master..xp_cmdshell @cmd


/* This will disable the cmd shell */
EXEC sp_configure 'xp_cmdshell', 1
GO
RECONFIGURE
GO

/* This switches off advanced options */
EXEC sp_configure 'show advanced options', 0
GO
RECONFIGURE
GO




/* table to catch the triggers */
CREATE TABLE [dbo].[TMP](
	    [RowID] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
		[Message] varchar(100) NOT NULL,
		[DateStamp] [datetime] NOT NULL
) 


/* Example of an AFTER TRIGGER for INSERT & UPDATE & DELETE but you can choose only one if you want*/
CREATE TRIGGER trgActorsChanged
ON tblActor
AFTER INSERT,UPDATE,DELETE
AS
BEGIN
	PRINT(CONVERT (varchar, SYSDATETIME()) +  ' - Something happened to tblActor')
	INSERT INTO WangExport.dbo.Tmp VALUES ('TEST MESSAGE', SYSDATETIME())
END


/* This sets an INSTEAD OF Trigger which blocks an INSERT and raises and error */
CREATE TRIGGER TR_MyTrigger
ON dbo.FIXED_TBL
INSTEAD OF INSERT
AS
BEGIN
	RAISERROR('No more rows can be added',16,1)
END

--Disable a DML trigger
DISABLE TRIGGER TR_MyTrigger ON tblActor
GO
--Enable a DML trigger
ENABLE TRIGGER TR_MyTrigger ON tblActor
GO




/* CREATES REGULAR INDEX ON COLUMN=POLICY_SUFFIX */
CREATE INDEX idx_POLICY_SUFFIX ON POLICY_COVERAGE2 (POLICY_SUFFIX);  

/* CREATES FASTER REGULAR INDEX BUT ALL VALUES MUST BE UNIQUE IN THE COLUMN*/
CREATE UNIQUE INDEX idx_POLICY_SUFFIX ON POLICY_COVERAGE2 (POLICY_SUFFIX); 


/* CREATES REGULAR INDEX ON MULTIPLE COLUMNS (note the order is important*/
CREATE INDEX idx_last_name_first_name on UserTable (last_name, first_name) 



/* CREATES CLUSTERED INDEX, THIS IS FASTER - UNIQUE ROWS and they are ordered with the
    CLUSTERED command for quicker lookup can only cluster one column though */
CREATE UNIQUE CLUSTERED INDEX idx_POLICY_NUMBER ON POLICY_COVERAGE2 (POLICY_NUMBER); 


/* CAN CHECK IF EXISTS FIRST */
IF NOT EXISTS (SELECT * FROM sys.indexes WHERE Name = 'idx_POLICY_NUMBER')
	BEGIN 
		CREATE INDEX idx_POLICY_NUMBER ON POLICY_COVERAGE2 (POLICY_NUMBER); 
	END

/* Drops specific Index */
DROP INDEX BILLING_BASE.idx_POLICY_NUMBER	
	
	
/* *******DELETE ALL CONSTRAINTS/KEYS***************** */	
DECLARE @indexName VARCHAR(128)
DECLARE @tableName VARCHAR(128)
DECLARE [indexes] CURSOR FOR
        SELECT          [sysindexes].[name] AS [Index],
                        [sysobjects].[name] AS [Table]
        FROM            [sysindexes]
        INNER JOIN      [sysobjects]
        ON              [sysindexes].[id] = [sysobjects].[id]
        WHERE           [sysindexes].[name] IS NOT NULL 
        AND             [sysobjects].[type] = 'U'
		AND             [sysindexes].[name] LIKE 'PK__%'  --'idx%'
OPEN [indexes]

FETCH NEXT FROM [indexes] INTO @indexName, @tableName
WHILE @@FETCH_STATUS = 0
BEGIN
	    -- DROPS PRIMARY KEY CONSTRAINST
        Exec ('ALTER TABLE [' + @tableName + '] DROP CONSTRAINT [' + @indexName + ']')
        FETCH NEXT FROM [indexes] INTO @indexName, @tableName
END
CLOSE           [indexes]
DEALLOCATE      [indexes]
GO




/* ********************************************************************************************************************************************* */
/* PIVOT TABLES - Not User Friendly - Better to pivot them in Pandas 11/18/19 */
/* ********************************************************************************************************************************************* */
SELECT 
    *
FROM 
(
    SELECT 
        [SalesPerson],
		AutoSold AS [ASales], 
        DATENAME(DW, [date]) AS [WeekDay] -- This output must match the 'IN' clause below
    FROM [TMP_123]
) as [PivotSource]
PIVOT
(
	SUM(ASales)  -- THE Aggregate
	FOR [WeekDay] IN ([Monday], [Tuesday], [Wednesday], [Thursday], [Friday]) -- Match to pivoted columns
)as [PivotTable]
	

/* 
SalesPerson	Monday	Tuesday	Wednesday	Thursday	Friday
-----------------------------------------------------------
Chris 		1		2		1			3			5
David 		0		0		4			3			2
*/
/* ********************************************************************************************************************************************* */

/* Drop table if Exists */
IF OBJECT_ID('dbo.TableName', 'U') IS NOT NULL 
  DROP TABLE dbo.TableName; 
  
/* for SQL SERVER 2016+ use ... */
DROP TABLE TableName IF EXISTS
  
  
/* XML DATA */  
DECLARE @string VARCHAR(100);
DECLARE @xml XML;
SET @string = 
'<bookstore>
<book>Candide</book>
<book>Pride and Prejudice</book>
</bookstore>';
SET @xml = CONVERT(XML, @string, 1);
SELECT @xml.query('/bookstore/book[2]');    -- <book>Pride and Prejudice</book>   (Returns XML)
SELECT @xml.value('(/bookstore/book)[2]', 'VARCHAR(100)')  -- Pride and Prejudice


/* Useful SQL SERVER Functions */
ISDATE('2017-08-25')   -- RETURNS BOOLEAN 
STUFF()  -- REPLACES CHARACTERS within index range 
CHARINDEX(substring, string, start) -- more useful than PATINDEX(%pattern%, string)

/* SQL Patterns wild cards for LIKE keyword */
%   -- Match any string of any length (including 0 length)
_   -- Match one single character
[]  -- Match any characters in the brackets, e.g. [xyz] = x or y or z  Note: [(a-c)] works the same as [abc]
[^] -- Match any character not in the brackets, e.g. [^xyz]            Note: [^(a-c)] works the same as [^abc]


/* Escape character for single quote use double single  */
SELECT 'OREN''S PROGRAM'      -- Returns OREN'S PROGRAM
SELECT '''' + 'OREN' + ''''   -- Returns 'OREN'


/* @@ROWCOUNT based on previous SQL Return */

IF ( @@ROWCOUNT = 0 ) SELECT NULL;



/* VARIANCE & STANDARD DEVIATION */

-- VAR_POP: This is the population variance
-- VAR_SAMP: This is the sample variance
-- STDDEV_SAMP: This is the sample standard deviation
-- STDDEV_POP: This is the population standard deviation


SELECT
  VARIANCE(amount) AS var_amount,
  VAR_POP(amount) AS var_pop_amount,
  VAR_SAMP(amount) AS var_samp_amount,
  STDDEV_SAMP(amount) as stddev_sample_amount,
  STDDEV_POP(amount) as stddev_pop_amount,
FROM bill