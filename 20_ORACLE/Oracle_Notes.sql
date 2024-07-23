-- =====================================================================================================================
-- See https://www.oracletutorial.com/oracle-basics/oracle-select/
-- Get expert help with Oracle PL/SQL= (extension of SQL) by asking TOM https://asktom.oracle.com/
-- Data Types: https://www.w3resource.com/oracle/oracle-data-types.php
-- RESERVED WORDS: https://doc.ispirer.com/sqlways/Output/SQLWays-1-134.html
-- USE https://dbfiddle.uk/  to practice queries
-- =====================================================================================================================
------------------------------------------------------------------------------------------------------------------------
ANSI SQL DATA-TYPE               ORACLE DATA-TYPE
------------------------------------------------------------------------------------------------------------------------
CHARACTER(n)                     CHAR(n)
CHAR(n)	                         CHAR(n)

CHARACTER VARYING(n)             VARCHAR2(n)
CHAR VARYING(n)	                 VARCHAR2(n)

NATIONAL CHARACTER(n)            NCHAR(n)
NATIONAL CHAR(n)                 NCHAR(n)
NCHAR(n)	                     NCHAR(n)

NATIONAL CHARACTER VARYING(n)    NVARCHAR2(n)
NATIONAL CHAR VARYING(n)         NVARCHAR2(n)
NCHAR VARYING(n)	             NVARCHAR2(n)

FLOAT                            FLOAT(126)
DOUBLE PRECISION                 FLOAT(126)
REAL                             FLOAT(63)

NUMERIC[(p,s)]                   NUMBER(p,s)
DECIMAL[(p,s)]                   NUMBER(p,s)

INT                              NUMBER(38) = NUMBER  (38 is default, no restrictions on precision)
INTEGER                          NUMBER(38) = NUMBER  (38 is default, no restrictions on precision)
SMALLINT                         NUMBER(19)
DATE
TIME
TIMESTAMP                        TIMESTAMP(6) = TIMESTAMP  (6 is default)


OTHER ORACLE DATA-TYPES
BLOB  -- The BLOB data type stores binary large objects. BLOB can store up to 4 gigabytes of binary data.
CLOB  -- The CBLOB data type stores character large objects. CLOB can store up to 4 gigabytes of character data.
NCLOB  -- The NCBLOB data type stores character large objects in multibyte national character set. NCLOB can store up to 4 gigabytes of character data.
BFILE  -- The BFILE data type enables access to binary file LOBs that are stored in file systems outside the Oracle database. A BFILE column stores a locator, which serves as a pointer to a binary file on the server's file system. The maximum file size supported is 4 gigabytes.

------------------------------------------------------------------------------------------------------------------------

-- Public synonyms
CREATE PUBLIC SYNONYM employees for hr.employees;

-- Private synonyms, unlike public synonyms, can be referenced only by the schema that owns the table or object.
CREATE SYNONYM addresses FOR hr.locations;

-- Drop a synonym (either type)
DROP SYNONYM addresses;


-- ================================================================================================================================================================

-- ALL ROLES / PRIVS FOR THE sysdba ONLY
SELECT * FROM DBA_ROLES;
SELECT * FROM DBA_ROLE_PRIVS;

-- FREE SPACE FOR SYSDBA ONLY
SELECT * FROM DBA_FREE_SPACE WHERE TABLESPACE_NAME=<tablespacename>;

select owner, segment_name, sum(bytes)/1024/1024/1024 GB from dba_segments
where segment_type='TABLE' and segment_name=upper('&TABLE_NAME') group by segment_name;

-- PARTITION SIZE
select PARTITION_NAME, sum(bytes)/1024/1024/1024 GB from dba_segments where SEGMENT_NAME=upper('&TABLE_NAME') and PARTITION_NAME='P01' group by PARTITION_NAME;

-- Bytes size of columns for a given row
SELECT VSIZE(COL1) + VSIZE("_COL2") FROM TABLE_NAME

-- FREE SPACE FOR USER
select segment_name,sum(bytes)/1024/1024/1024 GB from user_segments
where segment_type='TABLE' and segment_name=upper('&TABLE_NAME') group by segment_name;


SELECT * FROM USER_USERS;                                    -- ONLY CURRENT USER INFO
SELECT * FROM ALL_USERS WHERE USERNAME='<your-user-name>';   -- ALL USER INFO
ALTER USER <user-name> IDENTIFIED BY "<new password>" REPLACE "<old password>";   -- CHANGE PASSWORD

-- LIST CURRENT SESSION ACTIVE ROLES
select * from session_roles;     -- ROLES FOR CURRENT USER (LIST ONLY)
SELECT * FROM USER_ROLE_PRIVS;   -- ROLES FOR CURRENT USER

-- LIST USER PRIVILEGES
SELECT * FROM USER_SYS_PRIVS;

-- USE RIGHT-CLICK QUICK DDL to see the definitions of PK (Primary Key) and UK  (Uniqueness Constraints)  FK (Foreign Key)

-- LIST TABLE CONSTRAINTS WITH
SELECT * FROM USER_CONSTRAINTS WHERE table_name = XXX;
SELECT * FROM USER_CONSTRAINTS WHERE CONSTRAINT_TYPE = 'U' AND CONSTRAINT_NAME LIKE '%_UK%';
SELECT * FROM USER_CONSTRAINTS WHERE OWNER = '<tbl-owner>' AND CONSTRAINT_NAME = '<constr-name';

SELECT * FROM SYS.USER_CONSTRAINTS  WHERE table_name = 'STUDENT' AND OWNER='SCHEMA_1'  -- FOR CURRENT OWNER
SELECT * FROM SYS.ALL_CONSTRAINTS  WHERE table_name = 'STUDENT' AND OWNER='SCHEMA_1'   -- FOR ALL OWNERS
SELECT * FROM SYS.ALL_CONSTRAINTS WHERE CONSTRAINT_NAME = '<all-constraints>'


SELECT * FROM SYS.FOREIGN_KEYS -- REQUIRES PRIVILEGES

ALTER TABLE "<schema-name>"."<table-name>" MODIFY CONSTRAINT "<constraint-name>" DISABLE; -- DISABLE a constraint
ALTER TABLE "<schema-name>"."<table-name>" MODIFY CONSTRAINT "<constraint-name>" ENABLE;  -- Enable a constraint
ALTER TABLE "<schema-name>"."<table-name>" ADD CONSTRAINT "<constraint-name>" CHECK (<COLUMN_NAME> IN (0, 1)) ENABLE;  -- set a CHECK constraint
SELECT * FROM SYS.ALL_CONS_COLUMNS WHERE CONSTRAINT_NAME = "<constraint-name>" -- TELLS YOU COLUMN THE CONSTRAINT IS ON


-- In the column constraint_type, 
-- “R” is for the foreign key, 
-- “P” is for the primary key, 
-- “U” is for the uniqueness constraint, 
-- “C” is for the constraint check

-- GRANT ROLE ACCESS FOR ORACLE TABLE
GRANT SELECT ON CAQF_RESEARCH.<table-name> TO "<role-name>";  -- not sure about this


-- CHECK ROLES FOR FOR EXADATA TABLE OR VIEWS
SELECT * FROM ROLE_TAB_PRIVS WHERE OWNER=<tablespacename> AND TABLE_NAME='<tablename>';
SELECT * FROM ROLE_ROLE_PRIVS;   -- EMPTY
SELECT * FROM ROLE_SYS_PRIVS;   -- EMPTY

-- GRANT ROLE ACCESS FOR EXADATA TABLE OR VIEWS
GRANT SELECT ON <tablespace-name>.<table-name> TO "<role-name>";

-- choose any of the privelages
GRANT (select, insert, update, delete) ON <tablespace-name>.<table-name> TO "<role-name>";


-- REVOKE THE ABOVE ACCESS
REVOKE SELECT  ON <tablespace-name>.<table-name> FROM <role-name>;

-- CHECK ORACLE VERSION ...  currently using 19c on gcp
SELECT * FROM V$VERSION   -- e.g.  12c / 11g / 18c / 19c / 21c 
--Oracle Databasce 12c Enterprise Edition Release 12.1.0.2.0 --64bit Production
-- PL/SQL Release 12.1.0.2.0

-- META DATA TABLES REQUIRE AUTHORIZATION TO VIEW ...
Tables: dba_extents, dba_data_files


-- RETURN COLUMN AS A STRING
SELECT listagg(email, ',') WITHIN GROUP (ORDER BY email) as "Emails"  from EMAIL_TABLE
--   user1@email.com,user2@email.com,user3@email.com,



-- ========================================================================
-- USER_OBJECTS that are defined in your database
-- ========================================================================
SELECT *  FROM SYS.USER_OBJECTS ORDER BY OBJECT_TYPE;
SELECT DISTINCT OBJECT_TYPE  FROM SYS.USER_OBJECTS  -- LIST OF OBJECT_TYPES: (INDEX, SYNONYM, PACKAGE BODY, TRIGGER, PACKAGE, PROCEDURE, FUNCTION, LOB, SEQUENCE, TYPE, TABLE, VIEW)
-- LOB: (large objects) data types, such as CLOB, NCLOB, and BLOB, are used to store a large amount of data, such as text documents and images. BLOB. The BLOB data type is used to store large amounts of binary data.
-- SEQUENCES: used for auto increment IDs in the tables or other counters
-- TYPE:
-- SYNONYM:
-- PACKAGE:
-- PACKAGE BODY:
-- SEQUENCE: used for keeping an incremented value

-- ========================================================================
-- SEQUENCE OBJECTS IN THE DATABASE (USED FOR KEEPING AN INCREMEMNTED VALUE)
-- ========================================================================
SELECT * FROM SYS.ALL_SEQUENCES WHERE SEQUENCE_OWNER = <owner-name>
SELECT * FROM SYS.USER_SEQUENCES

-- Oracle SQL Developer: View -> Dbms Output -> '+' -> Connect to DB
-- LOOPS:
DECLARE
  x NUMBER := 0;
BEGIN
  LOOP
    DBMS_OUTPUT.PUT_LINE('Inside loop:  x = ' || TO_CHAR(x));
    x := x + 1;  -- prevents infinite loop
    EXIT WHEN x > 3;
  END LOOP;
  -- After EXIT statement, control resumes here
  DBMS_OUTPUT.PUT_LINE('After loop:  x = ' || TO_CHAR(x));
END;

-- RESULT:
--Inside loop:  x = 0
--Inside loop:  x = 1
--Inside loop:  x = 2
--Inside loop:  x = 3
--After loop:  x = 4


-- ========================================================================
-- TO Query Case Insensitve 
-- ========================================================================
ALTER SESSION SET NLS_COMP=LINGUISTIC;
ALTER SESSION SET NLS_SORT=BINARY_CI;


-- ========================================================================
-- NLS_DATE_FORMAT
-- ========================================================================
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';  
SELECT SYSDATE FROM DUAL;  -- 2023-02-15 16:40:36

ALTER SESSION SET NLS_DATE_FORMAT = 'HH24:MI:SS';
SELECT SYSDATE FROM DUAL;  -- 16:41:43

ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';
SELECT SYSDATE FROM DUAL;  -- 2023-02-15 16:42:31



-- ========================================================================
CREATE TABLE TMP_TABLE(
    ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    "1_COL" VARCHAR2(50) NOT NULL,    -- Column starting with integer requires quoted identifier (i.e. quotes around the identifier/column name)
     COL_2   VARCHAR2(50) NULL,       -- Does not require Quotations, NULL is default and not required
    "COL_3" VARCHAR2(50) NOT NULL,    -- Does not require Quotations
    "_COL_4" VARCHAR2(50),            -- requires quoted identifier if prefix underscore, no constraints set => NULLS allowed
    "KEYWORD" VARCHAR2(50) NOT NULL,   -- requires quoted identifier if use oracle keyword/reserved word
    "lowercase_name" VARCHAR(20))      -- requires quoted identifier to preserve the lower case and to be queried with lower case by "lowercase_name"
-- If column requires quotations then the access/insert commands require quotations and are case sensitive


CREATE TABLE TMP_TABLE(
    ID INTEGER GENERATED BY DEFAULT AS IDENTITY(START WITH 1 MAXVALUE 999999 MINVALUE 1 CACHE 20 NOORDER NOKEEP) NOT NULL,
    COL_1 VARCHAR2(500 BYTE) NOT NULL,
    CONSTRAINT TBL_PK PRIMARY KEY (ID)
);


-- ===========================================================================
-- TEMPORARY TABLE https://www.process.st/how-to/creating-a-temporary-table-in-oracle/
-- ===========================================================================

CREATE GLOBAL TEMPORARY TABLE table_name (
  column_1 datatype [constraint],
  column_2 datatype [constraint]
);

DROP table_name;   -- when you are done



DESCRIBE TMP_TABLE;  -- will return Schema, also DESC TMP_TABLE; works as a contraction
SELECT * FROM SYS.USER_TABLES WHERE TABLESPACE_NAME='SchemaOrDBName' AND TABLE_NAME = 'TMP_TABLE';       -- TABLE INFO / EXISTENCE CECK
SELECT * FROM SYS.ALL_TABLES  -- INCLUDES SYSTEM TABLES
select * FROM SYS.all_objects where object_name in ('<table-name>')   -- ALL OBJECTS, includes CREATED / LAST_DDL_TIME column
SELECT * FROM SYS.USER_TAB_COLUMNS WHERE TABLESPACE_NAME='SchemaOrDBName'  TABLE_NAME = 'TMP_TABLE';     -- COLUMN INFO




UPDATE <table-name> SET <column-name> = NULL
/*
# If you disable autocommit mode, then you have to explicitly commit every transaction. 
# After ever transactionally consistent set of DML statements (INSERT, UPDATE, and DELETE), 
# you'll need to do an explicit commit or an explicit 'ROLLBACK'.
*/
SHOW AUTOCOMMIT;    -- displays wheter you have autocommit mode on or not

COMMIT; --  commits DML statements
ROLLBACK; -- rollback DML statements

-- For Date Queries use TO_DATE & TO_TIMESTAMP
SELECT * FROM TBL WHERE DateColumn > TO_DATE('01/14/2022', 'MM/DD/YYYY')
SELECT * FROM TBL WHERE DateColumn > DATE'01/14/2022'  -- SAME AS ABOVE
SELECT * FROM TBL WHERE DateTimeColumn > TO_TIMESTAMP('01/14/2022 15:46:40', 'MM/DD/YYYY HH24:MI:SS')
SELECT * FROM TBL WHERE DateTimeColumn > TIMESTAMP'01/14/2022 15:46:40'

-- ====================================================================
-- Conversion Functions (https://www.techonthenet.com/oracle/functions)
-- ====================================================================
TO_CHAR()         -- number or date to a string 
TO_NUMBER()       -- string to a number
TO_DATE()         -- string to a date
TO_TIMESTAMP()    -- string to a timestamp

-- LIMIT 5
SELECT *  FROM TableName
FETCH FIRST 5 ROWS ONLY;

-- LIMIT 20, 10
SELECT *  FROM TableName
OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;

-- LIMIT 20%
SELECT * FROM TableName
FETCH FIRST 20 PERCENT ROWS ONLY;


-- WITH TIES, if you are ordering by a value you can retrieve the FIRST 'n' rows including 'tied' values
-- example below retrieves more than FIRST 3 rows since you included TIES
SELECT * from SalaryTable 
ORDER BY Salary DESC 
FETCH FIRST 3 ROWS With TIES;

-- ID    NAME       SALARY
-- ----------------------------------------
-- 3    Dhoni     16000
-- 1    Geeks     15000  
-- 6    Watson    10000  // This is Tied
-- 4    Finch     10000  // This is Tied



-- USER DEFINED VARIABLES
DECLARE
TmpVar varchar(20);
MY_ID varchar(20) := 'abce3udsa'

BEGIN
    SELECT ColumnValue into TmpVar FROM TableName
    WHERE ID = MY_ID;
END;


-- Naming an output column,  'As' is implicit.  Both commands below are the same
SELECT FUNC(Col1) AS NewColumn From Table1;
SELECT FUNC(Col1) NewColumn From Table1;



-- Since PL/SQL 20.2.0.175
DEFINE usr = 'YourName';
SELECT * FROM Table1 WHERE CreatedBy = '&usr';
SELECT * FROM Table2 WHERE CreatedBy = '&usr';

-- BEFORE PL/SQL 20.2 Use but only works for one line...
WITH MyTab AS (SELECT 'YourName' as usr FROM DUAL) 
SELECT * FROM Table1 T1 INNER JOIN mytab M ON T1.CreatedBy = M.usr;

SELECT * FROM Table1 INNER JOIN Table2 ON Table1.field = Table2.field   -- inner join example
SELECT * FROM Table1, Table2 WHERE Table1.field = Table2.field          -- same as the inner join, but older notation

SELECT * FROM Table1 CROSS JOIN Table2     -- cross join example
SELECT * FROM Table1, Table2               -- same as the cross join, but older notation

SELECT * FROM Table1 T1 
INNER JOIN Table2 T2  ON T1.<field> = T2.<field>
INNER JOIN Table3 T3  ON T2.<field> = T3.<field>


-- DISTINCT  for single column
SELECT DISTINCT column_1 FROM table;  

-- DISTINCT combination of columns ...
SELECT DISTINCT column_1, column_2, column_3 FROM  table_name;


-- TO COUNT DISTINCT rows try ..
SELECT COUNT(*) from (SELECT DISTINCT X, Y, Z FROM table_name)

-- UNIQUE CONSTRAINT ON COMBINATION OF COLUMNS
ALTER TableName ADD CONSTRAINT CnstrName UNIQUE(COL_3, COL_5, COL_7);

-- Note: DISTINCT is synonym of UNIQUE which is not SQL standard,  both are expensive keywords

-- REMOVE CONSTRAINTS 
ALTER TABLE TableName DROP CONSTRAINT CnstrName;

-- STRINGS MUST HAVE SINGLE QUOTES!!!!
INSERT INTO <table-name> (COL1, COL2) VALUES ('VALUE1', 'VALUE2');


-- WILL PROMPT TO BIND VALUES TO PARAMETERS X & Y FOLLOWING EXECUTION OF COMMAND
INSERT INTO <table-name> (COL1,COL2) VALUES (:X, :Y);
SELECT * FROM <table-name> WHERE COL1 = :X AND COL2 = :Y;
SELECT :X FROM DUAL;

-- COMPARE WITH THE &X BELOW WHICH IS DEFINED BEFORE, NOT BOUND AFTER EXECUTION
DEFINE X = 'ABC';
SELECT &X FROM DUAL;


-- KEYWORDS SYSDATE (datetime stamp) & USER (username)
INSERT INTO <table-name>  (COL1,COL2) VALUES (SYSDATE, USER);
INSERT INTO <table-name>  (COL1,COL2) VALUES (NULL, '');   -- NULL and empty string are treated the same in oracle and entered as NULL values

-- ADD ROWS FROM ANOTHER TABLE
INSERT INTO TableNameDest SELECT * FROM TableNameSource;

-- Insert Multiple Rows is significantly faster than consecutive inserts  (Oracle 23c)
INSERT INTO Messages (user_name, message_txt)  
VALUES ('ob1', 'message 3'),
	     ('ob2', 'message 4'),
	     ('ob3', 'message 5');

-- CREATE TABLE FROM EXISTING TABLE (CTAS=CREATE-TABLE-AS-SELECT)
CREATE TABLE TableNameNew AS (SELECT * FROM TableNameOld WHERE …);


-- SHOW CREATE TABLE
SELECT dbms_metadata.get_ddl('TABLE', '<schema-name>', '<table-name>' ) FROM dual;

-- RENAME TABLE
RENAME TABLE <old-table-name> TO <new-table-name>;        -- DID NOT WORK ON EXADATA
ALTER TABLE <old-table-name> RENAME TO <new-table-name>;  -- WORKED

-- ALTER DataType MODIFY
ALTER TABLE
   TableName
MODIFY
(
   ColumnName    VARCHAR2(255 CHAR)
);

-- ALTER nullable constraint
ALTER TABLE
   TableName
MODIFY
(
   ColumnName3 NULL,
   ColumnName4 NULL,
);

-- ALTER DataType ADD COLUMN
ALTER TABLE
   TableName
ADD
(
   ColumnName VARCHAR2(255 CHAR) NOT NULL
);


-- DROP COLUMNS
alter table
   table_name
drop
   (col_name1, col_name2); 

-- RENAME COLUMN
ALTER TABLE customers
  RENAME COLUMN customer_name TO cname;

-- ROW_NUMBER()   warning, requires TableName.*  not just * 
SELECT ROW_NUMBER() OVER (PARTITION BY EmployeeID ORDER BY OrderID DESC) as RowNumber, TableName.* FROM TableName

-- RANK()    warning, requires TableName.*  not just *
SELECT RANK() OVER (PARTITION BY COL1 ORDER BY COL2 DESC) AS RK, TableName.* FROM TableName

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


--REMOVE ALL DUPLICATES KEEP LAST ROW OF EACH GROUP - UNIQUENESS ON COL1/COL2/COL3
DELETE FROM MainTbl WHERE ID NOT IN
(SELECT MAX(ID) from MainTbl
GROUP BY COL1, COL2, COL3)


-- ALTERNATE REMOVE ALL DUPLICATE ENTRIES
CREATE TABLE TMP_TBL1 AS (SELECT ROW_NUMBER() OVER (PARTITION BY COL1, COL2, COL3 ORDER BY CREATED_ON DESC) AS ROW_NUM, MainTbl.ID FROM MainTbl);
DELETE FROM MainTbl WHERE ID IN (SELECT ID FROM TMP_TBL1 WHERE ROW_NUM > 1);
DROP TABLE TMP_TBL1;


-- Create View
-- not stored physically on the disk,  does not need updating. View changes with the original table.  it generates view with every query of the view.
CREATE VIEW <view-name>
AS SELECT * FROM <table_name>;

-- Materialized View :
-- for frequent querying, stored physically on the disk, must be manually updated or with trigger
CREATE MATERIALIZED VIEW MV_MY_VIEW
REFRESH FAST START WITH SYSDATE
   NEXT SYSDATE + 1
     AS SELECT * FROM <table_name>;


-- ===========================================================================
-- DROP TABLE and all associated foreign key constraints
-- https://docs.oracle.com/database/121/SQLRF/statements_9003.htm
-- there is no IF EXISTS command
-- ===========================================================================
DROP TABLE <table-name> CASCADE CONSTRAINTS;


-- ===========================================================================
-- CASE Statement https://www.techonthenet.com/oracle/functions/case.php
-- ===========================================================================
CASE [expression]

   WHEN condition_1 THEN result_1
   WHEN condition_2 THEN result_2
   ...
   WHEN condition_n THEN result_n

   ELSE result

END

e.g.

SELECT
status,
CASE status
WHEN 'a1' THEN 'Active'
WHEN 'a2' THEN 'Active'
WHEN 'a3' THEN 'Active'
WHEN 'i' THEN 'Inactive'
WHEN 't' THEN 'Terminated'
END AS StatusText
FROM stage.tst

-- ===========================================================================
-- UNION Query,  parenthesis are optional
-- ===========================================================================
(SELECT user_id FROM table_1)  UNION (SELECT user_id FROM table_2);
SELECT user_id FROM table_1 UNION SELECT user_id FROM table_2;  -- same as above

-- ===========================================================================
-- UNION vs UNION ALL.
-- ===========================================================================
SELECT supplier_id FROM suppliers
UNION     -- removes dupes (slower)
SELECT supplier_id FROM order_details;

SELECT supplier_id FROM suppliers
UNION ALL  -- does not remove dupes
SELECT supplier_id FROM order_details;


-- ===========================================================================
-- CTE (NESTED CTE QUERY)
-- ===========================================================================
WITH TBL1 AS (SELECT * FROM ...),
     TBL2 AS (SELECT * FROM TBL1),
	 TBL3 AS (SELECT * FROM TBL2)
SELECT * FROM TBL3


-- ===========================================================================
-- JSON_VALUE / JSON_TABLE
-- ===========================================================================

SELECT JSON_VALUE('{"x": "1",  "y": ["2", "3"}}', '$.y[0]') AS value  FROM DUAL; -- returns "2"
SELECT JSON_VALUE('{"x": "1",  "y": {"z": "1"}}}', '$.y.z') AS value  FROM DUAL;  -- returns "2"


SELECT y
FROM   JSON_TABLE(
         '{"x": "1", "y": {"z": "2"}}',
         '$'
         COLUMNS
           y VARCHAR2(4000) FORMAT JSON PATH '$.y'
       );
-- RETURNS {"z": "2"}

 SELECT z FROM JSON_TABLE('{"x": "1", "y": {"z": {"a": 5}}}', '$' COLUMNS z VARCHAR2(20) FORMAT JSON PATH '$.y.z');
 -- RETURNS {"a":5}


SELECT
  jt.company,
  jt.title
FROM
  JSON_TABLE(
    '{
        "past_work": [
            {"company": "COMPANY1", "title": "TITLE1"},
            {"company": "COMPANY2", "title": "TITLE2"}
        ]
     }',
    '$.past_work[*]'
      COLUMNS (
        company VARCHAR2(100) PATH '$.company',
        title   VARCHAR2(100) PATH '$.title'
      )
  )
    AS jt

-- RETURNS 
-- COMPANY	TITLE
-- COMPANY1	TITLE1
-- COMPANY2	TITLE2

SELECT
  jt.*
FROM
  JSON_TABLE(
    '{
        "XX_data":[
          {
            "employee_id": "E1",
            "full_name":   "E1  Admin",
            "past_work":   "N/A"
          },
          {
            "employee_id": "E2",
            "full_name":   "E2  Admin",
            "past_work": [
              {"company": "E2 PW1 C", "title": "E2 PW1 T"},
              {"company": "E2 PW2 C", "title": "E2 PW2 T"},
            ]
          },
        ]
     }',
    '$.XX_data[*]'
      COLUMNS (
        employee_id VARCHAR2(100) PATH '$.employee_id',
        full_name   VARCHAR2(100) PATH '$.full_name',
        past_work   VARCHAR2(100) PATH '$.past_work',
        NESTED PATH '$.past_work[*]'
          COLUMNS (
            past_work_company VARCHAR2(100) PATH '$.company',
            past_work_title   VARCHAR2(100) PATH '$.title'
          )
      )
  )
    AS jt
-- RETURNS:
-- EMPLOYEE_ID	FULL_NAME	PAST_WORK	PAST_WORK_COMPANY	PAST_WORK_TITLE
-- E1	E1  Admin	N/A	null	null
-- E2	E2  Admin	null	E2 PW1 C	E2 PW1 T
-- E2	E2  Admin	null	E2 PW2 C	E2 PW2 T    


-- ===========================================================================
-- NULLIF function https://www.techonthenet.com/oracle/functions/nullif.php
-- ===========================================================================
-- compares expr1 and expr2. If expr1 and expr2 are equal, the NULLIF function returns NULL. Otherwise, it returns expr1
NULLIF(expr1, expr2)


-- ===========================================================================
-- CAST Function (https://www.techonthenet.com/oracle/functions/cast.php)
-- ===========================================================================
-- 'dual' is a built-in table and is required in the command
SELECT CAST('22-Aug-2003' AS varchar2(30)) from dual;  -- 22-Aug-2003
SELECT CAST(19740220 as char(8)) from dual;            -- 19740220


-- ===========================================================================
-- Date/Time Functions  https://www.oracletutorial.com/oracle-date-functions/
-- ===========================================================================
SELECT LAST_DAY('20-Feb-1974') from dual; -- returns date of last day of the month = 28-Feb-1974
SELECT ADD_MONTHS(date1, number_months) from dual
SELECT NEXT_DAY('01-Aug-03', 'TUESDAY') from dual; -- NEXT_DAY function returns the first weekday that is greater than a date.
SELECT NEW_TIME (TO_DATE ('2003/11/01 01:45', 'yyyy/mm/dd HH24:MI'), 'AST', 'MST')  -- Converts from time zones  AST->MST
SELECT EXTRACT(YEAR FROM DATE '2003-08-22')  from dual; -- Result: 2003
SELECT EXTRACT(MONTH FROM DATE '2003-08-22') from dual; -- Result: 8
SELECT EXTRACT(DAY FROM DATE '2003-08-22') from dual;   -- Result: 22
SELECT DISTINCT tzname FROM V$TIMEZONE_NAMES;  -- List timezones
SELECT TZ_OFFSET('US/Michigan') from dual;  -- Result: '-05:00'
SELECT TIMESTAMP'1962-09-23 03:23:34.234' FROM DUAL;  -- Space allowed after TIMESTAMP
SELECT TO_TIMESTAMP('01/14/2022 15:46:40', 'MM/DD/YYYY HH24:MI:SS') FROM DUAL;
SELECT TRUNC(TIMESTAMP'1962-09-23 03:23:34.234') FROM DUAL;  --RETURNS DATE ONLY
SELECT TRUNC(SYSDATE-5) FROM DUAL;   -- use for comparison  WHERE CREATE_DATA <= TRUNC(SYSDATE-5)   created within 5 days
SELECT DATE'1974-02-20' FROM DUAL;   -- SPACE ALLOWED AFTER DATE

SELECT SYSDATE,                         -- 14-JUN-22
       CURRENT_DATE,                    -- 14-JUN-22
       SYSTIMESTAMP,                    -- 14-JUN-22 11.20.14.119303000 AM -05:00
       sys_extract_utc(SYSTIMESTAMP),   -- 14-JUN-22 06.20.14.119303000 AM
       CURRENT_TIMESTAMP,               -- 14-JUN-22 12.20.14.119305000 PM AMERICA/NEW_YORK
       LOCALTIMESTAMP,                  -- 14-JUN-22 12.20.14.119305000 PM
       DBTIMEZONE,                      -- -05:00
       SESSIONTIMEZONE                  -- America/New_York
from dual;


-- ===========================================================================
-- REGEXP_LIKE()  -  regex comparison, extension of 'LIKE'
-- ===========================================================================
SELECT * FROM my_table

WHERE REGEXP_LIKE(column_1, '^my_string$', 'i');  -- i (ignore case)


-- ===========================================================================
-- SUBSTR(COL, START, [END])   - returns a substring
-- ===========================================================================
SELECT SUBSTR('abc',2, 3) FROM DUAL;   -- RETURNS 'bc'

-- ===========================================================================
-- REGEXP_SUBSTR()  -- returns substring matching regex
-- ===========================================================================
SELECT REGEXP_SUBSTR('STRING_EXAMPLE','[^_]+',1,1) AS output from DUAL;  -- returns 'STRING'


-- ===========================================================================
-- INSTR(fullstr, substr)  - returns positoin of a substr
-- ===========================================================================
SELECT INSTR('xabcx','abc') FROM DUAL;   -- RETURNS 2

-- ===========================================================================
-- REGEXP_INSTR()   -- returns where regex starts
-- ===========================================================================
SELECT REGEXP_INSTR('xx24xx794xx','\d{3}') FROM DUAL; -- returns 7

-- ===========================================================================
-- REPLACE()   -- replaces where string matches
-- ===========================================================================
SELECT REPLACE('xx24xx794xx','794', 'abc') FROM DUAL; -- returns xx24xxabcxx


-- ===========================================================================
-- REGEXP_REPLACE()   -- replaces where regex matches
-- ===========================================================================
SELECT REGEXP_REPLACE('xx24xx794xx','\d{3}', 'abc') FROM DUAL; -- returns xx24xxabcxx


-- ===========================================================================
-- RPAD(string1, padded_length [, pad_string])   -- pads string to the right
-- ===========================================================================
SELECT RPAD('xxxx', 7, 'P') FROM DUAL;   -- returns xxxxPPP


-- ===========================================================================
-- LPAD(string1, padded_length [, pad_string])   -- pads string to the left
-- ===========================================================================
SELECT LPAD('xxxx', 7, 'P') FROM DUAL;   -- returns PPPxxxx

-- ===========================================================================
-- NVL()
-- ===========================================================================
SELECT NVL(COLUMN_NAME, 0) FROM TABLE_NAME   -- replaces null with zero
SELECT NVL(SUBSTR('ABC_blah', 0, INSTR('ABC_blah', '_')-1), 'ABC_blah') AS output  FROM DUAL;  -- returns 'ABC'


-- ===========================================================================
-- UID, USER  built-in values useful for inserts
-- ===========================================================================
SELECT UID, USER FROM dual; --  14   obez


-- ===========================================================================
-- COALESCE Function (https://www.techonthenet.com/oracle/functions/coalesce.php)
-- ===========================================================================
-- COALESCE(exp1, exp2, exp3)  all expressions must be same data-type.  
-- returns first non-null value from set exp1, exp2, exp3  or null if they are all null
SELECT COALESCE( address1, address2, address3 ) AS address_column  FROM suppliers;
SELECT SUM COALESCE(Col1, 0) as Total_Col1 FROM TableName   -- this will replace null values with Zero in the sum


-- ===========================================================================
-- DECODE Function (https://www.techonthenet.com/oracle/functions/decode.php)
-- ===========================================================================
-- will replace column value using a dictionary, note default is 'Gateway'
SELECT DECODE(supplier_id, 10000, 'IBM', 10001, 'Microsoft', 10002, 'Hewlett Packard', 'Gateway') AS supplier_name
FROM suppliers;


-- ===========================================================================
-- GROUP ID Function (https://www.techonthenet.com/oracle/functions/group_id.php)
-- ===========================================================================
-- assigns a number to each group
SELECT SUM(salary), department, bonus, GROUP_ID()
FROM employees
WHERE bonus > 100
GROUP BY department,
ROLLUP (department, bonus)
HAVING GROUP_ID() < 1;

-- ===========================================================================
-- ROW NUM (https://www.techonthenet.com/oracle/functions/rownum.php)
-- ===========================================================================
-- generates row number 
SELECT ROWNUM, customers.* FROM customers WHERE customer_id > 4500 ORDER BY last_name;;

-- ROWNUM   CUSTOMER_ID   LAST_NAME   FIRST_NAME   FAVORITE_WEBSITE
-- ------   -----------   ---------   ----------   ---------------------
--      4          8000   Anderson    Paige
--      2          6000   Ferguson    Samantha     www.bigactivities.com
--      5          9000   Johnson     Derek        www.techonthenet.com
--      3          7000   Reynolds    Allen        www.checkyourmath.com
--      1          5000   Smith       Jane         www.digminecraft.com

-- ===========================================================================
-- TRUNCATE vs DELETE
-- ===========================================================================
TRUNCATE TABLE <table_name>; -- USES AUTOCOMMIT and can not be rolled back, no WHERE commands

DELETE FROM <table_name>;    -- Same as above but requires COMMIT; allows WHERE command
COMMIT;

-- SQL Query to return N rows from dual
SELECT LEVEL AS ID, 'ROW-' || LEVEL AS ROW_NUM FROM DUAL CONNECT BY LEVEL <= 5;

--ID	ROW_NUM
--1	    ROW-1
--2	    ROW-2
--3	    ROW-3
--4	    ROW-4
--5	    ROW-5


-- ===========================================================================
-- String/Char Functions (https://www.techonthenet.com/oracle/functions/)
-- ===========================================================================
ASCII
ASCIISTR
CHR
COMPOSE
CONCAT
Concat with ||
CONVERT
DECOMPOSE
DUMP
INITCAP(str) -- capitalize
INSTR(fullstring, substring)  -- see above
INSTR2
INSTR4
INSTRB
INSTRC
LENGTH  -- as expected
LENGTH2
LENGTH4
LENGTHB
LENGTHC
LOWER(str)   -- as expected
LPAD -- see above
LTRIM(str)  -- as expected
NCHR
REGEXP_INSTR -- see above
REGEXP_REPLACE -- see above
REGEXP_SUBSTR -- see above
REPLACE  -- see above
RPAD  -- see above
RTRIM  -- as expected
SOUNDEX
SUBSTR(COL, START, [END])   -- see above
TRANSLATE
TRIM(str)    -- as expected
UPPER(str)   -- as expected
VSIZE


-- ===========================================================================
-- Numeric/Math Functions  (https://www.techonthenet.com/oracle/functions/)
-- ===========================================================================
ABS
ACOS
ASIN
ATAN
ATAN2
AVG
BITAND
CEIL
COS
COSH
COUNT
EXP
FLOOR
GREATEST
LEAST
LN
LOG
MAX
MEDIAN
MIN
MOD
POWER
REGEXP_COUNT
REMAINDER
ROUND (numbers)
ROWNUM
SIGN
SIN
SINH
SQRT
SUM
TAN
TANH
TRUNC (numbers)
