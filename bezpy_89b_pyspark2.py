# https://sparkbyexamples.com/pyspark-tutorial/
import numpy as np
import pandas as pd
import pyspark
from pyspark.sql import DataFrameWriter   # <-- can use this to connect another database via JDBC
from pyspark.sql import SparkSession, DataFrame   # <---- can use this to connect another database via JDBC


from pyspark.sql.types import StructType, StructField, StringType, IntegerType

data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54], ['Ann', 34]]

# Create the pandas DataFrame
pdf = pd.DataFrame(data, columns=['Name', 'Age'])



# ======================================================================================================================
# Spark environment variables are set in the file spark.conf 
# configurations can be set in ...
# ======================================================================================================================
conf = pyspark.SparkConf()
conf.set('spark.app.name', 'app_name')               # sets config variable
conf.set('spark.sql.catalogImplementation', 'hive')  # allows you to create local hive tables 
ss = pyspark.sql.SparkSession.builder.config(conf=conf).getOrCreate()
ss.conf.get('spark.app.name')                # returns 'app_name'
ss.conf.isModifiable('spark.app.name')       # returns False if the env. variable is static
ss.conf.set('spark.app.name', 'app_name2')   # after initialization




# ======================================================================================================================
# Create data frame from list of tuples
# ======================================================================================================================
df = ss.createDataFrame([(1,2,3),(4,5,6)], ['Col1', 'Col2', 'Col3'])  # instance of pyspark.sql.DataFrame
df.show()
# +----+----+----+
# |Col1|Col2|Col3|
# +----+----+----+
# |   1|   2|   3|
# |   4|   5|   6|
# +----+----+----+

# ======================================================================================================================
# Creates temp wiew which you can query
# ======================================================================================================================
df.createOrReplaceTempView("view_name") # creates View or local table
ss.sql("Select * from view_name Where Col1 = 4").show() # queries local view created
# +----+----+----+
# |Col1|Col2|Col3|
# +----+----+----+
# |   4|   5|   6|
# +----+----+----+

# Also try ...
# Dataset.sqlContext.sql(query)

# ======================================================================================================================
# Two spark options to save data to a table  SaveAsTable (creates table) & insertInto (existing table)
# ======================================================================================================================

# currently below line gives error .. This version of %1 is not compatible with the version of Windows you're running.
# ss.catalog.listTables(dbName=None)   # returns list of hive tables as spark table objects, optional parameter dbName

# I think you need Apache Hive running for this ...
#df.write.saveAsTable(name='table_name')

ddl = """CREATE TABLE Customers (CustomerID    int ,
                                 CustomerName  varchar(255) NOT NULL,	
                                 Country       varchar(255));"""

# ss.sql(ddl)

df2 = ss.createDataFrame([(7,8,9),(10,11,12)], ['Col1', 'Col2', 'Col3'])
#df2.write.insertInto(tableName='table_name', overwrite=False)  # appends rows from df2 to existing table


# ======================================================================================================================
# Convert pandas -> spark dataframe
# ======================================================================================================================
sdf1 = ss.createDataFrame(pdf)  # will infer data types
sdf1.printSchema()
sdf1.show()

sdf2 = ss.createDataFrame(pdf.astype(str))  # will set both columns as strings

# Will set according to defined schema for each column StructField(column_name, type, nullable)
my_schema = StructType([StructField("First Name", StringType(), True), StructField("Age", IntegerType(), False)])
sdf3 = ss.createDataFrame(pdf, schema=my_schema)
sdf3.printSchema()
sdf3.show()


# Enable Apache Arrow to convert Pandas to PySpark DataFrame
# ss.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
# spdf4 = ss.createDataFrame(pdf)
# spdf4.printSchema()
# spdf4.show()  # This is giving an error

pdf2 = sdf3.select("*").toPandas()  # Convert PySpark DataFrame to Pandas
sdf3.toPandas()          # Convert PySpark DataFrame to Pandas
sdf3.toJSON()            # Convert PySpark DataFrame to JSON
# sdf3.toDF()            # NOT SURE YET?  pyspark.sql.utils.IllegalArgumentException: requirement failed: The number of columns doesn't match.
sdf3.toLocalIterator()   # returns generator for rows



# ======================================================================================================================
# cache/persist commands work for sdf or rdd
# ======================================================================================================================
# DISK storage here does not mean HDFS it means local grid server memory
from pyspark import StorageLevel
# Persists the DataFrame with the default storage level (MEMORY_AND_DISK).
sdf3.cache()    # persists dataframe in memory if possible, does not take parameters.  Only do when necessary for smaller dataframes
sdf3.persist(StorageLevel.MEMORY_ONLY)          # Same as .cache() above, RDD is stored as deserialized Java object in JVM
sdf3.persist(StorageLevel.MEMORY_AND_DISK)      # more specific control over the behavior than .cache() method
sdf3.persist(StorageLevel.MEMORY_ONLY_SER)      # MEMORY ONLY and stores RDD as serialized Java object (one byte-array per partition)
sdf3.persist(StorageLevel.MEMORY_AND_DISK_SER)  # drops partitions that don't fit to memory, to disk
sdf3.persist(StorageLevel.DISK_ONLY)            # stored only on disk
sdf3.persist(StorageLevel.OFF_HEAP)             #

# pyspark automatically monitors cache and drops out cached partitions based on lru (least-recently-used) method
sdf3.unpersist()  # can be used to MANUALLY remove data from cache

# ======================================================================================================================



# ======================================================================================================================
# apply methods to columns using UDF (User Defined Functions)
# ======================================================================================================================
from pyspark.sql.types import FloatType
from pyspark.sql.functions import col, udf, sum
udf_add = udf(lambda z: z + 0.1, FloatType())

pdf = pd.DataFrame({'Col1': [1, 1], 'Col2': [2, 2]})
sdf4 = ss.createDataFrame(pdf)


sdf4.show()
# +----+----+
# |Col1|Col2|
# +----+----+
# |   1|   2|
# |   1|   2|
# +----+----+

sdf4.select(col("Col1"), col("Col2"), udf_add("Col1").alias("Col3")).show()
sdf4.select("Col1", "Col2", udf_add("Col1").alias("Col3")).show()  # Same as above
# +----+----+----+
# |Col1|Col2|Col3|
# +----+----+----+
# |1   |2   |1.1 |
# |1   |2   |1.1 |
# +----+----+----+


sdf4.filter(col('Col2').isNull()).show()
# +----+----+
# |Col1|Col2|
# +----+----+
# +----+----+

sdf4.filter(col('Col2').isin([2, 3])).show()
# +----+----+
# |Col1|Col2|
# +----+----+
# |   1|   2|
# |   1|   2|
# +----+----+



# sum rows and columns
sdf4.select((sum("Col2") + sum("Col1")).alias('sum')).show()
# |sum|
# +---+
# |  6|
# +---+


# ======================================================================================================================
# Return a Row
# ======================================================================================================================
sdf4.select((sum("Col2") + sum("Col1")).alias('sum')).collect()[0]
# Row(sum=6)

# ======================================================================================================================
# Get a particular cell dataframe.collect()[row_index][column_index]
# ======================================================================================================================
sdf4.select(sum("Col2")+sum("Col1")).collect()[0][0]
# 6

# ======================================================================================================================
# adding a literal value with 'lit' to all rows of a new column
# ======================================================================================================================
from pyspark.sql.functions import lit
sdf4.select("Col1", "Col2", lit(3).alias("Col3")).show()
# +----+----+----+
# |Col1|Col2|Col3|
# +----+----+----+
# |   1|   2|   3|
# |   1|   2|   3|
# +----+----+----+


# ======================================================================================================================
# Handling Null Types
# ======================================================================================================================

data = [("James","CA",np.NaN),
        ("Julia","",None),
        ("Ram",None,200.0),
        ("Ramya","NULL",np.NAN)
]
df =ss.createDataFrame(data,["name", "state", "number"])
df.show()

# +-----+-----+------+
# | name|state|number|
# +-----+-----+------+
# |James|   CA|   NaN|
# |Julia|     |  null|
# |  Ram| null| 200.0|
# |Ramya| NULL|   NaN|
# +-----+-----+------+

df.filter(df.state.isNull()).show()   # reads None value as null
# +----+-----+------+
# |name|state|number|
# +----+-----+------+
# | Ram| null| 200.0|
# +----+-----+------+

df.filter(df['number'].isNull()).show()  # does not read np.NaN as null
# +-----+-----+------+
# | name|state|number|
# +-----+-----+------+
# |Julia|     |  null|
# +-----+-----+------+


# using the isnull, isnan function
from pyspark.sql.functions import col, isnan, isnull, when, count
df.select(isnull(df.state)).show()
# +---------------+
# |(state IS NULL)|
# +---------------+
# |          false|
# |          false|
# |           true|
# |          false|
# +---------------+

df.select(isnan(df.number)).show()
# +-------------+
# |isnan(number)|
# +-------------+
# |         true|
# |        false|
# |        false|
# |         true|
# +-------------+


# find them all  'None', 'NULL, '', null/None, np.nan
df.select([count(when(col(c).contains('None') | col(c).contains('NULL') |  (col(c) == '' ) |  isnull(c) | isnan(c), c)).alias(c) for c in df.columns]).show()
# +----+-----+------+
# |name|state|number|
# +----+-----+------+
# |   0|    3|     3|
# +----+-----+------+

# Note that col(c).isNull() is equivalent to isnull(c)


# ======================================================================================================================
# Convert string column to timstamp or date column
# ======================================================================================================================

from pyspark.sql.functions import to_timestamp, to_date
df = ss.createDataFrame([('1969-12-31 19:00:00', '1900-01-01')], ['col_timestamp', 'col_date'])
df.select(to_timestamp(df.col_timestamp, 'yyyy-MM-dd HH:mm:ss'), to_date(df.col_date, 'yyyy-MM-dd')).collect()
# [Row(to_timestamp(`col_timestamp`, 'yyyy-MM-dd HH:mm:ss')=datetime.datetime(1969, 12, 31, 19, 0), to_date(`col_date`, 'yyyy-MM-dd')=datetime.date(1900, 1, 1))]

# Earliest timestamp allowed seems to be '1969-12-31 19:00:00' == datetime.fromtimestamp(0)
df = ss.createDataFrame([('1969-12-31 18:59:59',)], ['col_timestamp'])
# df.select(to_timestamp(df.col_timestamp, 'yyyy-MM-dd HH:mm:ss')).collect() - gives error as you have gone below zero epoch time
pause = True
# When is this exception raised?  pyspark.sql.utils.AnalysisException

# ======================================================================================================================
# spark deepcopy()  - works directly for pandas df. But do this for spark dataframe
# ======================================================================================================================
from copy import deepcopy


df_original = ss.createDataFrame([[1,2], [3,4]], ['a', 'b'])
_schema = deepcopy(df_original.schema)
X2 = df_original.rdd.zipWithIndex().toDF(_schema)  # copied dataframe
X2 = ss.createDataFrame(df_original.rdd.map(lambda x: x), schema=df_original.schema)  # alternative method