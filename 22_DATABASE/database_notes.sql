-- SQL keys are used to uniquely identify rows in a table.
-- SQL keys can either be a single column or a group of columns.
-- Super key is a single key or a group of multiple keys that can uniquely identify tuples in a table.
-- Super keys can contain redundant attributes that might not be important for identifying tuples.
-- Candidate keys are a subset of Super keys. They contain only those attributes which are required to uniquely identify tuples.
-- All Candidate keys are Super keys. But the vice-versa is not true.
-- Primary key is a Candidate key chosen to uniquely identify tuples in the table.
-- Primary key values should be unique and non-null.
-- There can be multiple Super keys and Candidate keys in a table, but there can be only one Primary key in a table.
-- Alternate keys are those Candidate keys that were not chosen to be the Primary key of the table.
-- Composite key is a Candidate key that consists of more than one attribute.
-- Foreign key is an attribute which is a Primary key in its parent table but is included as an attribute in the host table.
-- Foreign keys may accept non-unique and null values.

-- Consider an SQL table has a column VALUE. You can consider VALUE = function(Composite-key-set)


-- SINGLE QUOTES FOR STRINGS, DOUBLE QUOTES FOR COLUMN NAMES
-- Oracle made the design decision that empty strings in VARCHAR/VARCHAR2 columns were NULL

-- DSN (Data Source Name) attributes may include, but are not limited to:
--  the name of the data source
--  the location of the data source
--  the name of a database driver which can access the data source
--  a user ID for data access (if required)
--  a user password for data access (if required)

-- ================================================================================================================================================================
-- TNS (Transparent Network Substrate) Connection via .ora files containing nested dictionaries
-- ================================================================================================================================================================
--  <oracle-home>/network/admin/tnsnames.ora  (client-side)
--  Contains DSN data used by the system to connect to oracle database.
    --  Using this, a client can fetch server associated information transparently
--  It contains the following information:
--    1. PROTOCOL, 2. HOST IP ADDRESS, 3. PORT NUMBER, 4. SID or SERVICE_NAME
--    E.g
----        mydb =
--              (DESCRIPTION =
--                  (ADDRESS = (PROTOCOL = TCP)(HOST = 10.35.15.1)(PORT = 1521))
--                  (CONNECT_DATA = (SID = mydb))

--  <oracle-home>/network/admin/sqlnet.ora (server-side)  Contains location of 'wallet' cwallet.sso file
--  <oracle-home>/network/admin/listener.ora (server-side)


-- ================================================================================================================================================================
-- DDL - Data Definition Language: statements used to define the database structure or schema. (AUTO COMMIT) Some examples:
-- ================================================================================================================================================================
-- CREATE - to create objects in the database
-- ALTER - alters the structure of the database
-- DROP - delete objects from the database
-- TRUNCATE - remove all records from a table, including all spaces allocated for the records are removed
-- COMMENT - add comments to the data dictionary
-- RENAME - rename an object

-- ================================================================================================================================================================
-- DML - Data Manipulation Language: statements used for managing data within schema objects. (NOT AUTO COMMIT) Some examples:
-- ================================================================================================================================================================
-- SELECT - retrieve data from the a database
-- INSERT - insert data into a table
-- UPDATE - updates existing data within a table
-- DELETE - deletes all records from a table, the space for the records remain
-- MERGE - UPSERT operation (insert or update)
-- CALL - call a PL/SQL or Java subprogram
-- EXPLAIN PLAN - explain access path to the data
-- LOCK TABLE - controls concurrency

-- ================================================================================================================================================================
-- DCL - Data Control Language. Some examples: COMMIT NOT REQUIRED
-- ================================================================================================================================================================
-- GRANT - gives user's access privileges to database
-- REVOKE - withdraw access privileges given with the GRANT command
-- SEE https://www.techonthenet.com/oracle/grant_revoke.php

-- ================================================================================================================================================================
-- TCL - Transaction Control: statements used to manage the changes made by DML statements. It allows statements to be grouped together into logical transactions.
-- ================================================================================================================================================================
-- COMMIT - save work done
-- SAVEPOINT - identify a point in a transaction to which you can later roll back
-- ROLLBACK - undo the modification I made since the last COMMIT
-- SET TRANSACTION - Change transaction options like isolation level and what rollback segment to use
-- SET ROLE - set the current active roles

-- RDBMS emphasizes ACID properties
--     Atomicity - all steps of transaction must complete or no transaction at all
--     Consistency - table constraints enforced. Isolated transactions are considered to be “serializable”, in a distinct order without any transactions occurring in tandem.
--     Isolation - concurrent executions are safe,
--     Durability - commited transactions must be persisted in non-volatile memory
--     Atomicity / Durability - come at the expense of high availability


# CRUD Operations = Create, Read, Update, Delete

-- ================================================================================================================================================================
-- TRANSACTIONAL-DATABASE vs ANALYTICAL-DATABASE
-- ================================================================================================================================================================
-- Transactional workload concentrates on many users and CRUD operations on usually one object/row at a time.
-- Emphasis on ACID integrity and throughput,  i.e. processing many operations per second
-- Examples of Transactional DBs are PostgreSQL, MySQL, MS SQL Server, Oracle

-- Analytical workloads: read-only complex aggregation queries large numbers of objects/rows, emphasis on managing big-data
-- Examples of Analytical Technologies are data warehousing tools e.g. Redshift (AWS), Biquery (Google Cloud), Snowflake and the Map-Reduce tech
-- Hive/HDFS/Spark

-- ================================================================================================================================================================
-- SYNONYMS
-- ================================================================================================================================================================
-- There are two major uses of synonyms:

-- 1. Object invisibility: Synonyms can be created to keep the original object hidden from the user.
--    Provides an alternative name for another database object, referred to as the base object, that can exist on a local or remote server.
-- 2. Location invisibility: Synonyms can be created as aliases for tables and other objects that are not part of the local database.
--    Provides a layer of abstraction that protects a client application from changes made to the name or location of the base object.

-- ================================================================================================================================================================
-- Oracle,
-- DB2 (IBM),
-- SQL Server (Microsoft), RDBMS is only vertically scalable i.e increasing RAM.  Can create tables with
--            MEMORY-OPTIMIZED feature which keeps a duplicate of the table for faster updates (locking is not required)

-- MongoDB   NO SQL Data is stored in the form of JSON style documents. Faster, dynamic queries,  horizontally scalable
--           i.e we can add more servers (sharding) but RDBMS is only vertically scalable i.e increasing RAM.
--           emphasizes on the CAP theorem (Consistency, Availability, and Partition tolerance)
--           RDBMS emphasizes ACID properties

-- PostgreSQL (Open-source) considered the best option for reliability - ACID (atomicity, consistency, isolation, durability) compliant,
--            and better than MySQL to be upgradable to Oracle,
--            can not use "memory optimized tables"

-- MySQL (Open-source) but owned by Oracle, diverted in syntax from the SQL standards, consumes less CPU than Postgres
--       good for defragmentation and indexing
--       can use "memory optimized tables"
--       more popular than Postgres and therefore more online support

-- SQLite (runs without a server - used for cellphone database), small scale,

-- MariaDB (Open-source),

-- Horizontal Scaling => Increase Servers
-- Vertical Scaling => Increase RAM

-- ======================================================================================================================
-- Normal Forms
-- ======================================================================================================================

-- 1NF: Each table cell should contain a single value. Each record needs to be unique.
-- 2NF: 1NF + Single Column Primary Key
-- 3NF: 2NF + No transitive functional dependencies (two non-key columns have transitive dependencies)

-- BCNF: (Boyce-Codd Normal Form) only one column is a candidate key
-- 4NF:
-- 5NF:
-- 6NF:

-- ======================================================================================================================
-- Transitive Dependency
-- ======================================================================================================================
-- X -> Z is a transitive dependency if the following three functional dependencies hold true:
-- X->Y, Y does not ->X, Y->Z
-- {Book} ->{Author} (if we know the book, we knows the author name, assume every book has one author)
-- {Author} does not -> {Book} or would be one-to-one mapping between author-book (an author can write many books)
-- {Author} -> {Author_age}
-- e.g. book_id, book_name, author_id, author_name, author_age
-- should split to
-- book_id, book_name, author_id (foreign-key)
-- author_id, author_name, author_age

-- Operational Data is 3NF Normalized to reduce data redundancy to avoid issues with insert/delete/update anomalies, improving data integrity.
-- Data Warehouses use dimensional models.  With fewer denormalized tables, separate for each business process, for faster retrieval and simplicity, better for reporting.
-- Since there are duplicate data bitmap indexing is effective for dimensional models

-- =============================================================================================================
-- TYPES OF JOINS
-- =============================================================================================================
-- INNER JOIN:         intersect of values joining on a column (CROSS PRODUCT WITH A SHARED COLUMN VALUE CONDITION)
-- LEFT OUTER JOIN:    nulls on the right side if right table has no joining value
-- RIGHT OUTER JOIN:   nulls on the left side if right table has no joining value
-- FULL OUTER JOIN:    union of both results above
-- CROSS JOIN:         not joining on a column, rather a cartesian product of all rows in both tables
-- SELF JOIN:          join table with itself with any conditions you set




