# requires pip install cx_oracle
# https://cx-oracle.readthedocs.io/
# c.f. with syntax for sqlite3
import cx_Oracle
import datetime

# Connect Descriptor Strings are commonly stored in a tnsnames.ora. if not you can set it here
dsn = """(DESCRIPTION=
             (FAILOVER=on)
             (ADDRESS_LIST=
               (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
               (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521)))
             (CONNECT_DATA=(SERVICE_NAME=sales.example.com)))"""

# I THINK - Transparent Network Substrate (TNS) used interchangeably with ODBC Data Source Name (DSN)

try:
    conn = cx_Oracle.connect(user="hr", password="welcome", dsn="CONNECTION_NAME") # METHOD 1 using TNS/DSN (i.e. the Connection Identifier)
    conn = cx_Oracle.connect(user="hr", password="welcome", dsn="CONNECTION_NAME", encoding="UTF-8", threaded=True, mode=cx_Oracle.SYSDBA)
    conn = cx_Oracle. connect('usr', 'psswd', f'{HOST}:{PORT}/{DATABASE_NAME}') 
    conn = cx_Oracle.connect( 'username/password@localhost:PORT/DB_NAME')
    print(conn.version)
    cur = conn.cursor()

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# ALTERNATIVELY
# dsn = cx_Oracle.makedsn(host=HOST, port=PORT,service_name=SERVICE_NAME, sid=USER)
# with cx_Oracle.connect(user=USER, password=PASSWORD, dsn=dsn, encoding="UTF-8") as connection:
#         cur = connection.cursor()



# fetchall rows
cur.execute('select * from employee where salary > :sal', {'sal': 50000})
rows = cur.fetchall()

# fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
cur.execute("""SELECT first_name, last_name
               FROM employees
               WHERE department_id = :did AND employee_id > :eid""", did=50, eid=190)
rows = cur.fetchmany(3)

# fetchone() is used fetch one record from top of the result set
cur.execute('select * from employee')
rows = cur.fetchone()


# BIND BY ORDER
data = [[10007, 'Vikram', 48000.0], [10008, 'Sunil', 65000.1], [10009, 'Sameer', 75000.0]]
cur.executemany('insert into employee values (:1,:2,:3)', data)
cur.commit()  # required for insert/update/delete


# BIND BY NAME
sql = "INSERT INTO dept (deptno, dname, loc) VALUES (:deptno, :dname, :loc)"

try:
  cur.execute (sql, deptno=50, dname='MARKETING', loc='LONDON')
except cx_Oracle.DatabaseError:
  print ('Failed to insert row')


sql = "INSERT INTO TMP_TBL (C1, C2) VALUES (:C1, :C2)"
cur.execute (sql, C1=datetime.datetime(2025, 1, 9, 14, 21, 16, 299202), C2='SUCCESS')
cur.execute (sql, {'C1': datetime.datetime(2025, 1, 9, 14, 21, 16, 299202), 'C2': 'SUCCESS'})  # same as above

conn.commit ()


cur.close()
conn.close()



# SessionPool Object
# https://cx-oracle.readthedocs.io/en/latest/api_manual/session_pool.html
# cx_Oracle’s connection pooling lets applications create and maintain a pool of connections to the database.
# Connection pooling is important for performance when applications frequently connect and disconnect from the database.

pool = cx_Oracle.sessionPool(dsn='DEV_REGISTRY', homogeneous=False, externalauth=True, min=3, max=100, threaded=True)
conn = pool.aquire()
cur = conn.cursor()
cur.execute(sql_query)

pool.release(conn)
pool.close()


# Parameters for pooling:
# max_overflow=25     – the number of connections to allow in connection pool “overflow”, that is connections that can be opened above and beyond the pool_size setting, which defaults to five. this is only used with QueuePool.
# pool_size=5
# pool_recycle=-1     –this setting causes the pool to recycle connections after the given number of seconds has passed. It defaults to -1, or no timeout. For example, setting to 3600 means connections will be recycled after one hour
# pool_timeout=60     –number of seconds to wait before giving up on getting a connection from the pool. This is only used with QueuePool.
# pool_use_lifo=True  –use LIFO (last-in-first-out) when retrieving connections from QueuePool instead of FIFO (first-in-first-out). Using LIFO, a server-side timeout scheme can reduce the number of connections used during non- peak periods of use. When planning for server-side timeouts, ensure that a recycle or pre-ping strategy is in use to gracefully handle stale connections