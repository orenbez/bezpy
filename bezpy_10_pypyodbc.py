# used https://www.youtube.com/watch?v=VZMiDEUL0II&t=16s
# used https://www.youtube.com/watch?v=VkMXJvaWeTE&t=1450s
# used https://code.google.com/archive/p/pyodbc/wikis/GettingStarted.wiki
import sys
import pypyodbc        # requires `pip install pypyodbc`

# prints list of ODBC driver names
print(pypyodbc.drivers())

# REMOTE MYSQL SERVER CONNECTION STRING
# WARNING: by default MYSQL does not allow remote connections
# WARNING: for SSH db connections see bezPy16_ssh_tunnel.py
conn_mysql = pypyodbc.connect("Driver={MySQL ODBC 8.0 Unicode Driver};"
                              "Server=tscdev.cur42hqulbrf.us-east-1.rds.amazonaws.com;"
                              "Database=tscdev;"
                              "User=tsc;" 
                              "Password=YtBkIXYskh8eRMtExC27nGWuHrLPzm3x;")
                             #"Provider=MSDASQL;"   # didn't need
                             #"Option=3;"           # didn't need


# REMOTE PERVASIVE SQL CONNECTION STRING
conn_psql = pypyodbc.connect('Driver={Pervasive ODBC Interface};ServerName=192.168.150.142;DBQ=CYMATSC;')

 

# LOCAL SQL SERVER CONNECTION STRING
# Note that the parameters of connection string are unique to the API for SQL SERVER.  
# they will differ for each DB system.
conn_sqlserver = pypyodbc.connect('Driver={SQL Server Native Client 11.0};'
                                  'Server=(LocalDB)\orendb;'
                                  'Database=Practice;'
                                  'Trusted_Connection=yes;')

conn = conn_sqlserver

cr = conn.cursor()
SQLCommand ="""SELECT * FROM Products"""
x = cr.execute(SQLCommand)
column_names = [i[0] for i in x.description]

row = cr.fetchone()
while row:
    print(row)
    row = cr.fetchone()


# NON-LOCAL SQL SERVER CONNECTION STRING
conn = pypyodbc.connect('Driver={SQL Server};'
                              'Server=192.168.150.17;'
                              'Database=WangExport;'
                              'uid=sa;pwd=Welcome1')
cr = conn.cursor()




SQLCommand ="""SELECT POLICY_SYMBOL, POLICY_NUMBER, POLICY_SUFFIX
               FROM [WangExport].[dbo].[POLICY_POLICY]
               WHERE POLICY_NUMBER = 100581"""

SQLCommand2 = """SELECT TOP (4) [DA_NAM_SYMBOL]
                        ,[DA_NAM_ACCOUNT]
                        ,[DA_NAM_SUFFIX]
                 FROM [WangExport].[dbo].[POLICY03_NAME]
                 WHERE DA_NAM_ADDR_ZIP1 = 11743"""


SQLCommand3 = """SELECT  [DA_NAM_SYMBOL] ,[DA_NAM_ACCOUNT] ,[DA_NAM_SUFFIX]
                 FROM [WangExport].[dbo].[POLICY03_NAME]
                 WHERE DA_NAM_ACCOUNT = ? and DA_NAM_SUFFIX = ?"""


# ======================================================================================================================
# Uses the cursor itself as an iterator
# ======================================================================================================================
cr.execute(SQLCommand)
for row in cr:
    print(row[0],row[1],row[2])  #NOTE: Can Use row.POLICY_SYMBOL instead of row[0]
    print(row)


#RETURNS:
#HOP 100581 31
#('HOP', '100581', '31')
#HOP 100581 32
#('HOP', '100581', '32')
#HOP 100581 33
#('HOP', '100581', '33')

# ======================================================================================================================
# fetchone() ACCESS NEXT ROW, else returns None
# ======================================================================================================================
cr.execute(SQLCommand2)
row = cr.fetchone()
if row:
     print(row) # returns first tuple.row

#RETURNS: ('AP ', '100044', '13')


while True:  #loops through rest of the rows
    row = cr.fetchone()
    if row:
        print(row)
    else:
        break

#RETURNS: ('AP ', '100044', '14')
#         ('AP ', '100044', '15')
#         ('AP ', '100044', '16')

# ======================================================================================================================
# fetchall() all remaining rows in a list. If there are no rows, an empty list is returned (uses up memory)
# ======================================================================================================================
cr.execute(SQLCommand2)
rows = cr.fetchall()  # returns a list of tuples

for row in rows:
   print(row)

#RETURNS: ('AP ', '100044', '13')
#         ('AP ', '100044', '14')
#         ('AP ', '100044', '15')
#         ('AP ', '100044', '16')

# ======================================================================================================================
# fetchmany(5) fetches next five rows
# ======================================================================================================================




# ======================================================================================================================
# pass parameters as a LIST, TUPLE, or ROW  to replace the '?'s in the query in sequence
# ======================================================================================================================
cr.execute(SQLCommand3,[104841,16])
for row in cr:
    print(row)
#RETURNS: ('AP ', '104841', '16')

sys.exit()


# ======================================================================================================================
# DELETE OR INSERT uses the rowcount value
# ======================================================================================================================
cr.execute("DELETE FROM [WangExport].[dbo].[POLICY03_NAME] WHERE DA_NAM_ACCOUNT = ?", [104845])
print (cr.rowcount, 'rows have been deleted') # only works for UPDATES/INSERTS/DELETES
                                              # for other queries use print(len(rows))
cr.commit()  # commits database changes for UPDATES/INSERTS/DELETES - else will rollback

cr.execute("exec SP_TmpOren") # this executes stored procedure
cr.commit()  # commits database changes for UPDATES/INSERTS/DELETES
             # commit() is NECESSARY - even if INSERT action performed in stored procedure and not
             # explicitly in the cr.execute(sql) command

cr.execute("exec SP_TmpOren2") # this executes stored procedure which performs SELECT command
rows = cr.fetchall()  # this will give an error if there is an INSERT/UPDATE/DELETE command in SP
                      # pypyodbc.ProgrammingError:

# if you need to perform an insert followed by an sql query request then you MUST!!!! break it up
# You can not stick the SELECT statement at the end of the stored procedure and do it in one go.
cr.execute("exec SP_TmpOren") # INSERT COMMAND
cr.commit()
cr.execute("SELECT * FROM  [dbo].[TmpOren]")
rows = cr.fetchall()  


 
# ======================================================================================================================
# executescript() - will execute multiple commands in one go e.g.
# ======================================================================================================================
#cr.executescript("""DROP TABLE IF EXISTS pets;
#                        CREATE TABLE pets (ID INT, NAME TEXT);
#                        INSERT into name VALUES(1,'cat');
#                        INSERT into name VALUES(2,'dog');
#                        SQL STAMENT4; SQL STATMENT5;""")
#cr.commit() #- commits database changes for UPDATES/INSERTS


# ======================================================================================================================
# executemany() - will execute multiple commands as follows
# ======================================================================================================================
# cursor.executemany("INSERT INTO PETS VALUES (?,?)", ((3,'hamster'),(4,'pig')))
# cursor.commit() - commits database changes for UPDATES/INSERTS


# ======================================================================================================================
# connection.rollback() - performs rollback
# ======================================================================================================================

cr.close()
conn.close()
