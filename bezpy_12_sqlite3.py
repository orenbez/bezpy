# Import data from SQLite db using sqlite3,
# DOES NOT require any db server to manage data, only to import the library sqlite3
# Written in C, runs fast

# DB Browser for SQLite: This is a GUI and can be downloaded from here https://sqlitebrowser.org/dl/
# CLI for windows can be downloaded here https://sqlite.org/cli.html

# Here is the query language that is understood by sqlite: https://www.sqlite.org/lang.html
# Tutorial here: https://www.tutorialspoint.com/sqlite/sqlite_syntax.htm
# https://support.quest.com/toad-data-point/kb/109217/how-to-connection-to-sqlite-database


import os
import sqlite3  # included in the standard library
import pandas as pd

sqlite3.sqlite_version   # RETURNS VERSION

conn = sqlite3.connect(r'.\mydata\importing_sqlite.db')   # db will be created if path does not exist
cr = conn.cursor()


try:
    cr.execute("PRAGMA integrity_check")
except sqlite3.DatabaseError:
    print('File is an invalid type')
    conn.close()
# you can use a quicker integrity test with "PRAGMA quick_check, except that it does not verify that the contents of
# each index is in sync with its source-table data.


cr.execute("SELECT name FROM sqlite_master WHERE type = 'table'")    # conn.execute also works
cr.fetchall()  # lists all tables [('posts',), ('users',), ('tags',)]

cr.execute("SELECT name FROM sqlite_master WHERE type = 'table'")    # conn.execute also works
cr.execute("SELECT name FROM sqlite_master WHERE type = {?}", 'table')    # using placeholders

result = cr.execute('SELECT Id, Score, Tags FROM posts limit 3')

# result is a cursor object that behaves as an iterator, but you can simply use the cr
# cr.execute returns the same cursor object 'cr' so you can simply use that instead

# result
# >>> <sqlite3.Cursor at 0x16f87e873b0>
# cr
# >>> <sqlite3.Cursor at 0x16f87e873b0>


cr.execute('SELECT Id, Score, Tags FROM posts limit 3').fetchall()
# [('5', '9', '<machine-learning>'), ('7', '4', '<education><open-source>'), ('9', '5', None)]

# read query straight into data frame
df = pd.read_sql("SELECT * FROM posts;", conn)
# >>> df.columns - RETURNS COLUMNS
# >>> df.head() - RETURNS HEAD OF DATA 

#========================================================================

db_path = r'.\mydata\bad_name_sqlite.db'

# Delete database if exists
if os.path.exists(db_path):
    os.remove(db_path)

# conn = sqlite3.connect(":memory:")  # This will create a temp database in RAM


# this db does not exist but won't give error, will generate a new .db file
conn = sqlite3.connect(db_path)
cr = conn.cursor()
cr.execute("""PRAGMA foreign_keys=ON;""")

# turns on foreign keys if any set, default mode is OFF
# full list of pragmas are here https://www.sqlite.org/pragma.html

# ======================================================================================================================
# DATA TYPE CLASSES see here  https://www.sqlite.org/datatype3.html
# ======================================================================================================================
# NULL: The value is a NULL value.
# INTEGER:  The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
# REAL: The value is a floating point value, stored as an 8-byte IEEE floating point number.
# TEXT: The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
# BLOB: The value is a blob (bytes) of data, stored exactly as it was input, it is a catchall type, used for e.g. images/binary
# ======================================================================================================================
# For DATE/DATETIME see https://www.sqlitetutorial.net/sqlite-date/,
#                       https://www.sqlite.org/datatype3.html#date_and_time_datatype
# ======================================================================================================================


cr.execute("""DROP TABLE IF EXISTS employee;""")  # Not required since you have already deleted the whole db above

cr.execute("""CREATE TABLE IF NOT EXISTS employee(
               Id       INTEGER PRIMARY KEY AUTOINCREMENT,
               Name     TEXT NOT NULL,
               Age      INT NOT NULL,
               Address  TEXT,
               Salary   REAL);""")

# Note: The preferred storage class for a column is called its "affinity". CHAR(30) is treated like TEXT in sqlite3
# this is so that sqlite works with other db structures.  Address field will NOT be restricted to 30 chars
# Note 12/21/2018, I am not clear on the affinity type 'NUMERIC'

cr.execute("""INSERT INTO employee (Name,Age,Address,Salary) VALUES ('Paul', 32, 'California', 20000.00);""")
cr.execute("""INSERT INTO employee (Name,Age,Address,Salary) VALUES ('Allen', 25, 'Texas', 15000.00);""")
cr.execute("""INSERT INTO employee (Name,Age,Address,Salary) VALUES ('Teddy', 23, 'Norway', 20000.00);""")

# Insert with positional method with tuples
cr.execute("INSERT INTO employee (Name,Age,Address,Salary) VALUES (?, ?, ?, ?)", ('Kim', 22, 'South-Hall', 45000.00))

# Insert with positional method with multiple tuples
cr.executemany("INSERT INTO employee (Name,Age,Address,Salary) VALUES (?, ?, ?, ?)",
                                                    [('Mark', 25, 'Rich-Mond ',65000.00),
                                                    ('David', 27, 'Texas',85000.00 )])



# Insert with dictionary method
cr.execute("INSERT INTO employee (Name,Age,Address,Salary) VALUES (:Name, :Age, :Address, :Salary)",
                              {'Name': 'James',  'Age': 22, 'Address': 'Houston', 'Salary': 10000.00})
conn.commit()   # must be on the connection object


# cr.execute("""COMMIT;""")  # This is an alternative
# cr.commit()  # this is not recognized

cr.execute('SELECT * FROM employee')
cr.fetchone()   # returns tuple with next result: (1, 'Paul', 32, 'California', 20000.0)
cr.fetchmany(2) # returns next two results [(2, 'Allen', 25, 'Texas', 15000.0), (3, 'Teddy', 23, 'Norway', 20000.0)]
cr.fetchall()   # returns the rest:  [(4, 'Mark', 25, 'Rich-Mond ', 65000.0), (5, 'David', 27, 'Texas', 85000.0), ...

cr.execute("""CREATE TABLE email(Id          INTEGER PRIMARY KEY AUTOINCREMENT,
                                 EmployeeId  INTEGER NOT NULL,
                                 Email       TEXT NOT NULL,
                                 FOREIGN KEY(EmployeeId) REFERENCES employee(Id) ON DELETE CASCADE);""")
# ON DELETE CASCADE => rows in 'email' will be deleted when the corresponding employee row is deleted

cr.execute("""INSERT INTO email (EmployeeID, Email) VALUES ( 6, 'kim@gmail.com');""")
cr.execute("""INSERT INTO email (EmployeeID, Email) VALUES ( 7, 'james@gmail.com');""")
# cr2.execute("""INSERT INTO email (EmployeeID, Email) VALUES ( 8, 'unknown@gmail.com');""")
# this gives ... sqlite3.IntegrityError: FOREIGN KEY constraint failed
conn.commit() # Required for inserts, not for CREATE, or DROP TABLE


cr.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
print(cr.fetchall()) # returns [('employee',), ('sqlite_sequence',), ('email',)]

# 'sqlite_sequence' is an auto generated table keeps track of all other tables and number of records
# Note: sqlite_sequence only appears under certain conditions.
cr.execute("SELECT * FROM sqlite_sequence;")
print(cr.fetchall()) # returns [('employee', 7), ('email', 1)]


# Execute multiple queries at ones like this or by reading a file
# sql_script = """CREATE TABLE ...
#                 <query1>;
#                 <query2;
#                 COMMIT;"""
# cr.executescript(sql_script)

cr.close()
conn.close()


# UNION COMMAND
query_1 = "SELECT * FROM TBL_1"
query_2 = "SELECT * FROM TBL_2"
cr.execute(f"""{query_1} UNION {query_2}""")
# cr.execute(f"""({query_1}) UNION ({query_2})""")   # will fail for sqlite


# Command Line Interface
# C:\...\sqlite3 .\<path>\test.db    -- opens database or creates if doesn't exist
# sqlite> .help                      -- usage hints
# sqlite> .schema                    -- returns table schema
# sqlite> .schema customers          -- print the schema for a specific table by supplying its name
# sqlite> .tables                    -- returns list of tables
# sqlite> .databases                 -- List names and files of attached databases
# sqlite> create table customers(name text, age int);                 -- create new table
# sqlite> insert into customers values('Erik', 40);
# sqlite> insert into customers values('Mary', 53);
# sqlite> select * from customers  limit 1;                            -- query table
# sqlite> select * from TABLE limit START_ROW, NUMBER_OF_ROWS;         -- query table
# sqlite> .quit                                                        -- exit program