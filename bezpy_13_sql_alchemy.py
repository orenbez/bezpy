# ======================================================================================================================
# sqlalchemy - Universally manage various databases
# ======================================================================================================================
# TRY THIS: https://towardsdatascience.com/pandas-equivalent-of-10-useful-sql-queries-f79428e60bd9
# Import data using SQL Alchemy so that you can control different types of database with the same commands
# FULL Resource is here ... https://www.tutorialspoint.com/sqlalchemy/
# ======================================================================================================================
from sqlalchemy import create_engine, inspect # Oracle, SQL Server, MySql, SqlLite
from sqlalchemy.types import Integer, String, BigInteger, SmallInteger, DateTime
from sqlalchemy.orm import sessionmaker
# import sqlalchemy_pervasive  # not part of sqlalchemy
import pypyodbc
#import mysql     # Tools for Visual Studio 2017 was required to download from here https://visualstudio.microsoft.com/downloads/
import psycopg2  # for Postgres database
import sys


# ======================================================================================================================
# ON YOUR LOCAL PC YOU NEED
# 1) "pip install mysql-connector" to get the mysql drivers to work !!!!!!!!!!!!
# 2) Microsoft® ODBC Driver 13 for SQL Serve Download https://www.microsoft.com/en-us/download/details.aspx?id=50420
# 3) "pip install pyodbc"
# ======================================================================================================================

# ======================================================================================================================
# To list all data types use 'dir(sqlalchemy.types)'
# 'ARRAY', 'BIGINT', 'BINARY', 'BLOB', 'BOOLEAN', 'BigInteger', 'Binary', 'Boolean', 'CHAR', 'CLOB', 'Concatenable',
# 'DATE', 'DATETIME', 'DECIMAL', 'Date', 'DateTime', 'Enum', 'FLOAT', 'Float', 'INT', 'INTEGER', 'Indexable', 'Integer',
# 'Interval', 'JSON', 'LargeBinary', 'MatchType', 'NCHAR', 'NULLTYPE', 'NUMERIC', 'NVARCHAR', 'NullType', 'Numeric',
# 'PickleType', 'REAL', 'SMALLINT', 'STRINGTYPE', 'SchemaType', 'SmallInteger', 'String', 'TEXT', 'TIME', 'TIMESTAMP',
# 'Text', 'Time', 'TypeDecorator', 'TypeEngine', 'Unicode', 'UnicodeText', 'UserDefinedType', 'VARBINARY', 'VARCHAR',
# 'Variant', '_Binary'
# ======================================================================================================================

# sqlalchemy    SQL Server
# BigInteger    = BIGINT
# Integer       = INT
# SmallInteger  = SMALLINT
# String(n)     = ASCII strings - VARCHAR(n)
# String(100)   = VARCHAR(100)
# String        = VARCHAR(max)
# Unicode()     = Unicode string - VARCHAR or NVARCHAR depending on database
# Boolean       = BOOLEAN, INT, TINYINT depending on db support for boolean type
# DateTime      = DATETIME or TIMESTAMP returns Python datetime() objects.
# Date          = DATE
# Float()       = floating point values
# Numeric()     = precision numbers using Python Decimal()

#connection string format... 'dialect[+driver]://user:password@hostmane/path_to_db_name[?key=value]
e1 = create_engine('sqlite:///mydata/importing_sqlite.db', echo=True) #echo=True will echo database interaction to the screen

# print(e1.table_names())  # ['posts', 'tags', 'users']
inspector = inspect(e1)             # not to be confused with the built-in 'inspect' library
print(inspector.get_table_names())  # Replaces deprecated  e1.table_names()


print(e1.url)            # sqlite:///mydata/importing_sqlite.db
print(e1.dialect)        # <sqlalchemy.dialects.sqlite.pysqlite.SQLiteDialect_pysqlite object at 0x00000228C1D92490>
print(e1.driver)         # pysqlite
x = e1.execute("SELECT * FROM tags")  #### can also use session.execucte(sql)
x.fetchall()  # returns rows, also
# x.fetchone()
# x.fetchmany()
# x.rowcount # returns number of affected rows
# x.returns_rows # boolean if rows are present
# x.first() # returns next row of data and closes result set
# x.next()  # returns next row of data WARNING: x.next() discontinued in 1.4.14, use 'fetchone()' or first()
# x.keys()  # returns column names
# x.scalar() # returns first column first row data and closes result set

# With engine.execute() you can INSERT & DELETE.  But can't do SELECT * INTO  or DROP TABLE,  use session.execute instead


# ======================================================================================================================
# SQL SERVER
# ======================================================================================================================
e3 = create_engine("mssql+pyodbc://ro:Tsc7354%40!@192.168.150.17:1433/WangExport?driver=SQL+Server+Native+Client+11.0", echo=True)

# ======================================================================================================================
# MySQL
# ======================================================================================================================
e = create_engine('mysql+mysqlconnector://tsc:YtBkIXYskh8eRMtExC27nGWuHrLPzm3x@tscdev.cur42hqulbrf.us-east-1.rds.amazonaws.com:3306/tscdev', echo=True)
##"Driver={MySQL ODBC 8.0 Unicode Driver};"
##"Server=tscdev.cur42hqulbrf.us-east-1.rds.amazonaws.com;"
##"Database=tscdev;"
##"User=tsc;" 
##"Password=YtBkIXYskh8eRMtExC27nGWuHrLPzm3x;"


# ======================================================================================================================
# PostgreSQL
# ======================================================================================================================
e = create_engine('postgresql+psycopg2://postgres:badge7383@localhost:5432/Socratica')
# 'USER': 'postgres',  'PASSWORD': 'badge7383',

# ======================================================================================================================
# TRINO
# ======================================================================================================================
e = create_engine('trino://<username>:<password>@<host>:<port>/catalog/[schema]', connect_args={'extra_credential': [('username', 'user'), ('password', 'pswd')]})
# Note: /catalog/[schema] is optional
# ======================================================================================================================



# ======================================================================================================================
# Connect to your database of choice
# ======================================================================================================================
#engine_sqlite = create_engine('sqlite:///backups/importing_sqlite.db')
#engine_sqlite = create_engine('sqlite:///C:\\sqlitedbs\\school.db')
#engine_postgresql = create_engine('postgresql://user:password@localhost:5432/database_name')
#engine_mysql = create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/database_name')
#engine_mssqlserver = create_engine("mssql+pyodbc://ro:Tsc7354%40!@192.168.150.17:1433/WangExport?driver=SQL+Server+Native+Client+11.0")  ###<--- DEPRECATED DRIVER
#engine_mssqlserver = create_engine("mssql+pyodbc://ro:Tsc7354%40!@192.168.150.17:1433/WangExport?driver=ODBC+Driver+13+for+SQL+Server")  ###<--- NEW DRIVER
#engine_psql = create_engine("psql://192.168.150.142/CYMATSC?driver=Pervasive+ODBC+Unicode+Interface"

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'your_username'  #enter your username
PASSWORD = 'your_password'  #enter your password
HOST = 'subdomain.domain.tld'  #enter the oracle db host url
PORT = 1521  # enter the oracle port number
SERVICE = 'your_oracle_service_name'   # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = f'{DIALECT}+{SQL_DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/?service_name={SERVICE}'
#engine_oracle = create_engine(ENGINE_PATH_WIN_AUTH)
# also can use create_mock_engine(conn_string) for mocking

# ======================================================================================================================
# For table changes you need to commit. to do that use session not engine
# ======================================================================================================================
conn_string = "mssql+pyodbc://ro:Tsc7354%40!@192.168.150.17:1433/WangExport?driver=ODBC+Driver+13+for+SQL+Server"

engine = create_engine(conn_string)

conn=engine.connect()
conn.execute('SELECT * FROM TABLE')
conn.close()

Session = sessionmaker(bind=engine)
session = Session()
session.execute('exec SP_UPDATE_STUFF') # For Stored Procedure
session.commit()
session.close() # releases resources

# Session.add()
# Session.add_all()
# Session.bulk_save_objects()
# Session.bulk_insert_mappings()


# HOW TO DETERMINE THE conn_string URL
from sqlalchemy.engine.url import URL

db = {'drivername': '{MySQL ODBC 8.0 Unicode Driver}',
      'username': 'root',
      'password': 'computerguy$$323',
      'host': '198.251.79.44',
      'port': '3306',
     'database': 'ecusad_test',}

db = {'drivername': '{SQL Server}',
      'username': 'ro',
      'password': 'Tsc7354@!',
      'host': '192.168.150.17',
      'port': '1433'}
# PostgreSql
db = {'drivername': 'postgres',
               'username': 'postgres',
               'password': 'postgres',
               'host': '192.168.99.100',
               'port': 5432}

## sqlalchemy does not work for psql
##db = {'drivername' : '{Pervasive ODBC Unicode Interface}',
##      'host'       : '192.168.150.142',
##      'database'   : 'CYMATSC',}
      

print(URL.create(**db))  # didn't seem to work for SQL SERVER


# ======================================================================================================================
# READ SQL->DF, WRITE DATAFRAME TO SQL
# ======================================================================================================================
import pandas as pd
engine = e3
sql_query = 'SELECT * FROM TMP'
sql_table_name = 'TMP'



#query_result = pd.read_sql(sql_query, engine)

#import to dataframe specifying columns
#df = pd.read_sql_table('tableName',engine, index_col='idx_col', columns=['idx_col','col2','col3')

 # chunksize : int, default None
 #        If specified, return an iterator where `chunksize` is the
 #        number of rows to include in each chunk.
 # Sets the column ROWID to the index of the dataframe, otherwise use index_col=None
x = pd.read_sql(sql_query, con=engine, index_col='RowID', chunksize=None)  # QUERY
y = pd.read_sql_table(sql_table_name,engine, index_col='RowID', columns=['RowID','Message']) # IMPORTS FULL TABLE FOR SPECIFIED COLUMNS

# ======================================================================================================================
# to_sql()  DOES NOT NEED A COMMIT STATEMENT
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# ======================================================================================================================
# index=True (default is True) (uses dataFrame index as the index column - must be integer or big int)
# if_exists='fail' raises a ValueError and is the default.
# if_exists='replace' drops the table and inserts new values.
# if_exists='append' inserts new values into the table.
# schema=None Specify the schema (if database flavor supports this e.g. PostgreSQL). If None, use default schema.  
# chunksize=5000 is optimal chunksize for large data inserts in combination with method='multi'
# method='multi'  Pass multiple values in a single INSERT clause. (default is None)
#     Note: method='multi' may slow down insertions on traditional RDBMS's when loading into tables with many columns
# method=<callable>  callable with signature (pd_table, conn, keys, data_iter) see example below

# CREATES TABLE USING index 0,1,2
df = pd.DataFrame(data = [['Alex',10,'long description of Alex here'],
                          ['Fred',12, 'Long description of Fred'],
                          ['Dave',13, 'lots of details about Dave']], columns=['Name','Age','Description'], )
df.to_sql('NEW_TABLE_1', engine, schema=None, if_exists='replace', index=False, index_label=None, chunksize=None,
                                                                        dtype={'Name':String(100),
                                                                               'Age':Integer,
                                                                               'Description':String})

#### WARNING the default datatype is 'TEXT' which is a pain to work with and deprecated.
###          for  'TEXT' need to use 'LIKE' instead of '=' in sql query
###          you can also use type 'String' for everything like this dtype={i:String for i in claim_index}

# APPEND TO TABLE
df = pd.DataFrame(data = [['Steve',40],['Jane',42],['Andrew',44]], columns=['Name','Age'],)
df.to_sql('NEW_TABLE_2', engine, schema=None, if_exists='append', index=True, index_label=None, chunksize=None, dtype=None) # DOES NOT NEED COMMIT!!!!!!

# Note: index=True will create an [index] column, rename using index_label='idx_column'  which is better
# if you are setting the dtype=  then use 'index': Integer as example below
# if you have the table already created with index as special type IDENTITY(1,1) then set index=False and remove from dtype


# this is for index=True index_label=None,
dtype_web_policy = {'index': Integer,
                    'UserID': BigInteger,
                    'PolicySymbol': String(3),
                    'PolicyID': Integer,
                    'PolicySuffix': String(2),
                    'Effective': SmallInteger,
                    'Active': SmallInteger,
                    'Renewal': SmallInteger,
                    'OptIn': SmallInteger,
                    'DateStamp': DateTime}

# for index=True, index_label='idx_column'
# dtype_web_policy = {'idx_column': Integer, 'UserID': BigInteger, ...

# for index=False
# dtype_web_policy = {'UserID': BigInteger, ...



# Example of method=<callable>
# import postgres specific insert
from sqlalchemy.dialects.postgresql import insert

def to_sql_on_conflict_do_nothing(pd_table, conn, keys, data_iter):
    # This is very similar to the default to_sql function in pandas
    # Only the conn.execute line is changed
    data = [dict(zip(keys, row)) for row in data_iter]
    conn.execute(insert(pd_table.table).on_conflict_do_nothing(), data)

conn = engine.connect()
df.to_sql("some_table", conn, if_exists="append", index=False, method=to_sql_on_conflict_do_nothing)

# ======================================================================================================================
# also see non-standard library sqlparse which wich format, parse, split sql commands
# ======================================================================================================================

