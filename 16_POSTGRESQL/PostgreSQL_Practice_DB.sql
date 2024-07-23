-- see bezpy_66_PostgreSQL.py
--  https://www.postgresql.org/docs/14/datatype.html
-- Windows Service is "postgresql-x64-13".   if you can't delete due to open connections then restart service.
--  USE https://dbfiddle.uk/  to practice queries
/*   instead of ...
        column_name IDENTITY(1,1),
     use ...
        column_name  INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),  */


/* Use quotations around table name if you need upper case letters but BETTER use lower */
/* If you have uppercase chars in table names you will need quotations for every query */
/* Without quotations will assume lowercase for your table names */

CREATE TABLE "Earthquakes" (  earthquake_id int PRIMARY KEY,
                            occurred_on   timestamp  NOT NULL,
                            latitude real,
                            longitude real,
                            depth int,
                            magnitude real,
                            calculation_method varchar(10),
                            network_id varchar(100),
                            place varchar(500),
                            cause varchar(100) );


/* Use the LIMIT OFFSET operator */
SELECT  * From "Earthquakes" LIMIT 2 ;
SELECT  * From "Earthquakes" LIMIT 2  OFFSET 5:

/* no quotation marks for lower case */
 CREATE TABLE messages
( message_id  INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,  
  user_name VARCHAR(10),
  message_txt  VARCHAR(500));
  
  
  -- Using DEFAULT keyword only if entering a single row of data
  INSERT INTO Messages (message_id, user_name, message_txt)  VALUES (DEFAULT, 'ob', 'this is a message');
  
  -- Without DEFAULT keyword - note using single quotes for strings
  INSERT INTO Messages (user_name, message_txt)  VALUES ('ob', 'this is another message');
  
  -- Insert Multiple Rows is significantly faster than consecutive inserts
  INSERT INTO Messages (user_name, message_txt)  
  VALUES ('ob', 'message 3'),
  	     ('ob', 'message 4'),
		 ('ob', 'message 5');
  
-- CONCAT keyword to concatenate strings
SELECT CONCAT('user_', user_name) as user_nm, message_txt FROM Messages
  

  
-- SQL JOINS, bracketed words are optional for clarity
(INNER) JOIN: Returns records that have matching values in both tables.  Equivalent to cross join but with conditions
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

-- CROSS JOIN operator   (CROSS APPLY in some SQL systems)
-- Returns the Cross Product of the two tables without consideration of any column to join only
-- For every row in Messages it will be Joined with every row in Earthquakes
SELECT * FROM Messages CROSS JOIN Earthquakes    -- Better to be explicit with CROSS notation
SELECT * FROM Messages, Earthquakes              -- SAME AS ABOVE, older notation for cross join


--  COALESCE Function
SELECT COALESCE(<subquery>, 0) -- returns first non-null response in list so if subquery returns null then will return 0

-- Primary Key
CREATE TABLE contacts (
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT,
   contact_name VARCHAR(255) NOT NULL,
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
   CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

-- Foriegn Key Constraints
CREATE TABLE buyer_fees (buyerfees_id smallint GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1)  PRIMARY KEY,
                            buyer_id smallint NOT NULL,
                            country_id smallint NOT NULL,
					   		effectivedate date NOT NULL,
					   		buyercost money NOT NULL,
						CONSTRAINT fk_buyer_id FOREIGN KEY(buyer_id) REFERENCES buyer(buyer_id),
						CONSTRAINT fk_country_id FOREIGN KEY(country_id) REFERENCES Country(country_id)
						);

-- UNIQUE Constraint for two columns
CREATE TABLE country (country_id smallint GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
                            code   char(2)  NOT NULL,
                            country_name   varchar(100)  NOT NULL,
							UNIQUE(code),
							UNIQUE (country_name);

-- UNIQUE constraint for combination
CREATE TABLE country (country_id smallint GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
                            code   char(2)  NOT NULL,
                            country_name   varchar(100)  NOT NULL,
							UNIQUE(code,country_name);

-- Create database if not exists
SELECT 'CREATE DATABASE <your db name>' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '<your db name>')\gexec
-- \gexec sends the current query buffer to the server, then treats each column of each row of the query's output
-- (if any) as a SQL statement to be executed. \gexec cannot be used with the -c option in psql.


-- Create table if not exists
CREATE TABLE IF NOT EXISTS "table_name" (
    "column1" DATA_TYPE,
    "column2" DATA_TYPE,
    "column3" DATA_TYPE,
    ...
);

-- Index any columns that are used a lot in WHERE, ORDER BY, and GROUP BY clauses including integers
-- Indexing, cost memory and insert/update time but speed up searches on non-integer columns
CREATE INDEX <index_name> ON <table_name> (<column_name)
CREATE INDEX idx_POLICY_SUFFIX ON POLICY_COVERAGE (POLICY_SUFFIX);

-- Multi-Column Index, the order matters, sorting first by the last_name
CREATE INDEX idx_last_first ON person (last_name, first_name);


-- also see pg_tables

-- Materialized View for frequent querying
 CREATE MATERIALIZED VIEW MV_MY_VIEW
 [ WITH (storage_parameter [= value] [, ... ]) ]
    [ TABLESPACE tablespace_name ]
     AS SELECT * FROM <table_name>;