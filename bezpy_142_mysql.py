# ======================================================================================================================
# see bezpy_10_pypyodbc.com
import pypyodbc

# prints list of ODBC driver names
print(pypyodbc.drivers())

# REMOTE MYSQL SERVER CONNECTION STRING
# WARNING: by default MYSQL does not allow remote connections
# WARNING: for SSH db connections see bezPy16_ssh_tunnel.py
conn = pypyodbc.connect("Driver={MySQL ODBC 8.0 Unicode Driver};"
                        "Server=tscdev.cur42hqulbrf.us-east-1.rds.amazonaws.com;"
                        "Database=tscdev;"
                        "User=tsc;" 
                        "Password=YtBkIXYskh8eRMtExC27nGWuHrLPzm3x;")

cr = conn.cursor()
SQLCommand ="""SELECT * FROM Products"""
x = cr.execute(SQLCommand)
cr.commit()  # commits database changes for UPDATES/INSERTS/DELETES - else will rollback
cr.close()
conn.close()

# ======================================================================================================================
# Alternatively use mysql-connector-python
# https://www.w3schools.com/python/python_mysql_getstarted.asp

# Requires pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="yourusername",
                               password="yourpassword",
                               database = "mydatabase")

cr = mydb.cursor()

# SELECT STATEMENT
cr.execute("SELECT name, address FROM customers")
result = cr.fetchall()   # also cr.fetchone()
for x in result:
  print(x)



# INSERT ROW
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cr.execute(sql, val)
mydb.commit() # for UPDATES/INSERTS/DELETES


# INSERT MANY ROWS
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
cr.executemany(sql, val)
mydb.commit()
print(cr.rowcount, "was inserted.")


# ======================================================================================================================
# Alternatively use pymysql
import pymysql # requires `pip install pymysql`
connection_string = dict(host='localhost', user='root', password='pass')
conn = pymysql.connect(*connection_string)
cr = conn.cursor
cr.execute('SHOW DATABASES')
db_list = [db for db in cr]
cr.close()
conn.close()