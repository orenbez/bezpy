# https://youtu.be/_C8kWso4ne4?t=984
# Setup: https://docs.google.com/document/d/1Pqke7DnVUZbMdereIivic-UvfvTJ9ENAsnk_tfkN0EY/edit
import pyspark   # requires pip install pypark==<version-to-match-Apache-Spark>
import pandas as pd
from pyspark.sql import SparkSession

# 1) pyspark.sql.SparkSession vs. pyspark.SparkContext
# 2) Resilient Distributed Dataset (RDD) API Vs. Spark DataFrames API  Vs. Spark DataSet API (not used in python)


# rdd.collect()
# rdd.getStorageLevel()  # returns object detailing storage policy
# rdd.isEmpty()   # Returns true if and only if the RDD contains no elements at all

from pyspark.ml.feature import Imputer  # In statistics, imputation is the process of replacing missing data with substituted values
from pyspark.ml.feature import VectorAssembler  # combine multiple columns into a single vector column
from pyspark.ml.feature import StringIndexer   # will index a string 'categorical-column' into a numerical column
from pyspark.ml.regression import LinearRegression

file1 = r'.\pyspark\test1.csv'
file2 = r'.\pyspark\test2.csv'
file3 = r'.\pyspark\test3.csv'
file4 = r'.\pyspark\test4.csv'


# PANDAS DATAFRAME
pdf = pd.read_csv(file1)
#         Name  age  Experience  Salary
# 0      Krish   31          10   30000
# 1  Sudhanshu   30           8   25000
# 2      Sunny   29           4   20000

# CREATE SPARK-SESSION
ss = SparkSession.builder.getOrCreate()  # This is a sparksession object
# ss.stop()  # this will end the spark session

# Sets master URL & appName for the spark session
# ss = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()


ss.version # '3.0.3'
#  ss.master #  local[*]   ??? no such property
# Read from raw file
sdf = ss.read.csv(file1) # this is a pyspark dataframe

# Validate that you have a spark datafram
assert isinstance(sdf, pyspark.sql.DataFrame)

sdf.show()
# +---------+---+----------+------+
# |      _c0|_c1|       _c2|   _c3|
# +---------+---+----------+------+
# |     Name|age|Experience|Salary|
# |    Krish| 31|        10| 30000|
# |Sudhanshu| 30|         8| 25000|
# ...

# Read header line into dataframe
sdf = ss.read.option('header', 'true').csv(file1) # Assumes all columns string
sdf = ss.read.option('header', 'true').csv(file1, inferSchema=True)  # infers data type for each column
sdf = ss.read.csv(file1, header=True, inferSchema=True)  # Same as above
# ss.read.format("json").options(**options).load("examples/src/main/resources/people.json")   # read from json file to dataframe

sdf # To display colums/formats
# DataFrame[Name: string, age: int, Experience: int, Salary: int]

sdf.show()
sdf.show(truncate=False)   # no truncations
# +---------+---+----------+------+
# |     Name|age|Experience|Salary|
# +---------+---+----------+------+
# |    Krish| 31|        10| 30000|
# |Sudhanshu| 30|         8| 25000|
# |    Sunny| 29|         4| 20000|
# |     Paul| 24|         3| 20000|
# |   Harsha| 21|         1| 15000|
# |  Shubham| 23|         2| 18000|
# +---------+---+----------+------+

sdf.columns # Returns Columns as list
# ['Name', 'age', 'Experience', 'Salary']

sdf.count() # Returns number of rows

print((sdf.count(), len(sdf.columns)))  # equivalent to pandas data frame df.shape

sdf.show(2)  # shows top 2 lines only
# +---------+---+----------+------+
# |     Name|age|Experience|Salary|
# +---------+---+----------+------+
# |    Krish| 31|        10| 30000|
# |Sudhanshu| 30|         8| 25000|
# +---------+---+----------+------+

sdf.head(2) # Returns list of pyspark Row object     
# [Row(Name='Krish', age=31, Experience=10, Salary=30000),
#  Row(Name='Sudhanshu', age=30, Experience=8, Salary=25000)]
sdf.tail(2)


sdf.first() # Returns first row as row object Row(Name='Krish', age=31, Experience=10, Salary=30000)    (No sdf.last())
sdf.first().Name  # Krish
sdf.first()['Name'] # Krish

sdf.printSchema() # compare with df.info()
# root
#  |-- Name: string (nullable = true)
#  |-- age: integer (nullable = true)
#  |-- Experience: integer (nullable = true)
#  |-- Salary: integer (nullable = true)


# dfs['Name'] does not work

sdf.select(['Name', 'Age']).show()
# +---------+---+
# |     Name|Age|
# +---------+---+
# |    Krish| 31|
# |Sudhanshu| 30|
# ...

sdf.select('Salary').show()
# +------+
# |Salary|
# +------+
# | 30000|
# | 25000|
# | 20000|
# | 20000|
# | 15000|
# | 18000|
# +------+


sdf.select('Salary').distinct().show()
# +------+
# |Salary|
# +------+
# | 30000|
# | 25000|
# | 20000|
# | 15000|
# | 18000|
# +------+



sdf.dtypes
# [('Name', 'string'), ('age', 'int'), ('Experience', 'int'), ('Salary', 'int')]

sdf.describe().show()  # c.f with df.describe()
# +-------+------+------------------+-----------------+------------------+
# |summary|  Name|               age|       Experience|            Salary|
# +-------+------+------------------+-----------------+------------------+
# |  count|     6|                 6|                6|                 6|
# |   mean|  null|26.333333333333332|4.666666666666667|21333.333333333332|
# | stddev|  null| 4.179314138308661|3.559026084010437| 5354.126134736337|
# |    min|Harsha|                21|                1|             15000|
# |    max| Sunny|                31|               10|             30000|
# +-------+------+------------------+-----------------+------------------+

# Modify 'Experience' Column
sdf = sdf.withColumn('Experience', sdf['Experience'] + 1)

# Create new column as a function of existing column and reassign dfs
sdf = sdf.withColumn('Experience2', sdf['Experience'] + 2)

# +---------+---+----------+------+-----------+
# |     Name|age|Experience|Salary|Experience2|
# +---------+---+----------+------+-----------+
# |    Krish| 31|        11| 30000|         13|
# |Sudhanshu| 30|         9| 25000|         11|
# ...

# DROP COLUMN
# This will drop columns but not reassign dfs, only for show()
sdf.drop('Experience2', 'salary').show()


# RENAME COLUMN  'Name' -> 'First Name'
sdf.withColumnRenamed('Name', 'First Name').show()

# RENAME multiple columns
# sdf.withColumnRenamed(k1, v1).withColumnRenamed(k2, v2)




# ======================================================================================================================
# HANDLING NULLS
# ======================================================================================================================
sdf = ss.read.csv(file2, header=True, inferSchema=True)
# +---------+----+----------+------+
# |     Name| age|Experience|Salary|
# +---------+----+----------+------+
# |    Krish|  31|        10| 30000|
# |Sudhanshu|  30|         8| 25000|
# |    Sunny|  29|         4| 20000|
# |     Paul|  24|         3| 20000|
# |   Harsha|  21|         1| 15000|
# |  Shubham|  23|         2| 18000|
# |   Mahesh|null|      null| 40000|
# |     null|  34|        10| 38000|
# |     null|  36|      null|  null|
# +---------+----+----------+------+

sdf.filter('Salary is NOT NULL').show()
sdf.filter(sdf.Salary.isNotNull()).show()         # same as above
sdf.filter(sdf['Salary'].isNotNull()).show()   # same as above
# +-------+---+----------+------+
# |   Name|age|Experience|Salary|
# +-------+---+----------+------+
# |  Sunny| 29|         4| 20000|
# |   Paul| 24|         3| 20000|
# | Harsha| 21|         1| 15000|
# |Shubham| 23|         2| 18000|
# +-------+---+----------+------+


sdf.createOrReplaceTempView("tmp_view")                          # METHOD 1
ss.sql("SELECT * FROM tmp_view WHERE SALARY IS null").show()

sdf.filter('Salary is NULL').show()                             # METHOD 2
sdf.filter(sdf['Salary'].isNull()).show()                       # METHOD 3
# +----+---+----------+------+
# |Name|age|Experience|Salary|
# +----+---+----------+------+
# |null| 36|      null|  null|
# +----+---+----------+------+


sdf.filter(sdf['Salary'].isNull() & sdf['Experience'].isNull()).show()  


sdf.na.drop().show() # drop all rows with a null entry
# +---------+---+----------+------+
# |     Name|age|Experience|Salary|
# +---------+---+----------+------+
# |    Krish| 31|        10| 30000|
# |Sudhanshu| 30|         8| 25000|
# |    Sunny| 29|         4| 20000|
# |     Paul| 24|         3| 20000|
# |   Harsha| 21|         1| 15000|
# |  Shubham| 23|         2| 18000|
# +---------+---+----------+------+

sdf.na.drop(how='any', thresh=2, subset=['age', 'Experience']).show()
# drop parameters
# how -'any' or 'all' (default is 'any', i.e. drops if any field in row is null)
# thresh (maximum integer number of rows to drop, default is None)
# subset (list of columns to consider for nulls, default is all of the columns)


# Fills null values with 'Unknown' for the 'Name' Column
sdf.na.fill('Unknown', 'Name').show() # Replacement value must be String as column is type string

# Fills null values with 0 for specified Columns
sdf.na.fill(0, ['Age', 'Experience', 'Salary']).show()  # Replacement value must be of type integer


# impute mean value for the null values for given columns
imp = Imputer(inputCols=['Experience', 'Salary'], outputCols=['Exp_imputed', 'Sal_imputed']).setStrategy('mean')
imp.fit(sdf).transform(sdf).show()

# +---------+----+----------+------+-----------+-----------+
# |     Name| age|Experience|Salary|Exp_imputed|Sal_imputed|
# +---------+----+----------+------+-----------+-----------+
# |    Krish|  31|        10| 30000|         10|      30000|
# |Sudhanshu|  30|         8| 25000|          8|      25000|
# |    Sunny|  29|         4| 20000|          4|      20000|
# |     Paul|  24|         3| 20000|          3|      20000|
# |   Harsha|  21|         1| 15000|          1|      15000|
# |  Shubham|  23|         2| 18000|          2|      18000|
# |   Mahesh|null|      null| 40000|          5|      40000|
# |     null|  34|        10| 38000|         10|      38000|
# |     null|  36|      null|  null|          5|      25750|
# +---------+----+----------+------+-----------+-----------+
#

# ======================================================================================================================
# FILTER
# ======================================================================================================================
sdf.filter('Salary<=20000').show()
sdf.filter(sdf['Salary'] <= 20000).show() # same as above
# +-------+---+----------+------+
# |   Name|age|Experience|Salary|
# +-------+---+----------+------+
# |  Sunny| 29|         4| 20000|
# |   Paul| 24|         3| 20000|
# | Harsha| 21|         1| 15000|
# |Shubham| 23|         2| 18000|
# +-------+---+----------+------+


sdf.filter('Salary<=20000').select(['Name', 'Age']).show()
# +-------+---+
# |   Name|Age|
# +-------+---+
# |  Sunny| 29|
# |   Paul| 24|
# | Harsha| 21|
# |Shubham| 23|
# +-------+---+

# ==========================================================================================
# pyspark logic operators
# ==========================================================================================
# &  = AND
# |  = OR
# ~  = NOT
# ^  = XOR


sdf.filter((sdf['Salary'] <= 18000) | (sdf['Salary'] > 35000)).show()
# +-------+----+----------+------+
# |   Name| age|Experience|Salary|
# +-------+----+----------+------+
# | Harsha|  21|         1| 15000|
# |Shubham|  23|         2| 18000|
# | Mahesh|null|      null| 40000|
# |   null|  34|        10| 38000|
# +-------+----+----------+------+

# ===========================================================================
# GROUPBY
# ==========================================================================================
sdf = ss.read.csv(file3, header=True, inferSchema=True)

sdf.groupBy('Name').sum('salary').show()
sdf.groupBy('Name').sum().show()  # same as above,  salary is asssumed
# +---------+-----------+
# |     Name|sum(salary)|
# +---------+-----------+
# |Sudhanshu|      35000|
# |    Sunny|      12000|
# |    Krish|      19000|
# |   Mahesh|       7000|
# +---------+-----------+

sdf.groupBy('Departments').avg('salary').show()
sdf.groupBy('Departments').mean('salary').show()  # same as above
# +------------+-----------+
# | Departments|avg(salary)|
# +------------+-----------+
# |         IOT|     7500.0|
# |    Big Data|     3750.0|
# |Data Science|    10750.0|
# +------------+-----------+

sdf.groupBy('Departments').max('salary').show()
sdf.groupBy('Departments').min('salary').show()
sdf.groupBy('Departments').count().show()
# +------------+-----+
# | Departments|count|
# +------------+-----+
# |         IOT|    2|
# |    Big Data|    4|
# |Data Science|    4|
# +------------+-----+

# aggregation without grouping
sdf.agg({'Salary': 'sum'}).show()
# +-----------+
# |sum(Salary)|
# +-----------+
# |      73000|
# +-----------+

# ======================================================================================================================
# LINEAR REGRESSION Input: age, Experience; Output: Salary
# ======================================================================================================================
sdf = ss.read.csv(file1, header=True, inferSchema=True)
# +---------+---+----------+------+
# |     Name|age|Experience|Salary|
# +---------+---+----------+------+
# |    Krish| 31|        10| 30000|
# |Sudhanshu| 30|         8| 25000|
# |    Sunny| 29|         4| 20000|
# |     Paul| 24|         3| 20000|
# |   Harsha| 21|         1| 15000|
# |  Shubham| 23|         2| 18000|
# +---------+---+----------+------+


# combine two input values into a single vector called 'Independent Features'
va = VectorAssembler(inputCols=['age', 'Experience'], outputCol='Independent Features')
output = va.transform(sdf)
output.show()

# +---------+---+----------+------+--------------------+
# |     Name|age|Experience|Salary|Independent Features|
# +---------+---+----------+------+--------------------+
# |    Krish| 31|        10| 30000|         [31.0,10.0]|
# |Sudhanshu| 30|         8| 25000|          [30.0,8.0]|
# |    Sunny| 29|         4| 20000|          [29.0,4.0]|
# |     Paul| 24|         3| 20000|          [24.0,3.0]|
# |   Harsha| 21|         1| 15000|          [21.0,1.0]|
# |  Shubham| 23|         2| 18000|          [23.0,2.0]|
# +---------+---+----------+------+--------------------+


# We are treating 'Salary' as the dependent variable
finalized_data = output.select('Independent Features', 'Salary')
train_data, test_data =finalized_data.randomSplit([0.75,0.25])  # split train & test data 75% to 25%
regressor = LinearRegression(featuresCol='Independent Features', labelCol='Salary').fit(train_data)


regressor.coefficients # DenseVector([28.4757, 1271.3568])  # one coeficient for each input variable
regressor.intercept    # 14299.832495812996

pred_results = regressor.evaluate(test_data)
pred_results.meanAbsoluteError   # 785.909203671541
pred_results.meanSquaredError    # 617653.2764156357
pred_results.predictions.show()
# +--------------------+------+-----------------+
# |Independent Features|Salary|       prediction|
# +--------------------+------+-----------------+
# |          [23.0,2.0]| 18000|17214.09079632846|
# +--------------------+------+-----------------+


# ======================================================================================================================
# Convert Categorical Data to Numerical Data
# ======================================================================================================================
sdf = ss.read.csv(file4, header=True, inferSchema=True)
sdf.show(3)
# +----------+----+------+------+---+------+----+
# |total_bill| tip|   sex|smoker|day|  time|size|
# +----------+----+------+------+---+------+----+
# |     16.99|1.01|Female|    No|Sun|Dinner|   2|
# |     10.34|1.66|  Male|    No|Sun|Dinner|   3|
# |     21.01| 3.5|  Male|    No|Sun|Dinner|   3|
# +----------+----+------+------+---+------+----+
# only showing top 3 rows


# For single column
indexer = StringIndexer(inputCol='sex', outputCol='sex_indexed')

indexer.fit(sdf).transform(sdf).show(3)
# +----------+----+------+------+---+------+----+-----------+
# |total_bill| tip|   sex|smoker|day|  time|size|sex_indexed|
# +----------+----+------+------+---+------+----+-----------+
# |     16.99|1.01|Female|    No|Sun|Dinner|   2|        1.0|
# |     10.34|1.66|  Male|    No|Sun|Dinner|   3|        0.0|
# |     21.01| 3.5|  Male|    No|Sun|Dinner|   3|        0.0|
# +----------+----+------+------+---+------+----+-----------+
# only showing top 3 rows


# For multiple columns
indexer = StringIndexer(inputCols=['smoker', 'day', 'time'], outputCols=['smoker_idx', 'day_idx', 'time_idx'])
indexer.fit(sdf).transform(sdf).show(3)
# +----------+----+------+------+---+------+----+----------+-------+--------+
# |total_bill| tip|   sex|smoker|day|  time|size|smoker_idx|day_idx|time_idx|
# +----------+----+------+------+---+------+----+----------+-------+--------+
# |     16.99|1.01|Female|    No|Sun|Dinner|   2|       0.0|    1.0|     0.0|
# |     10.34|1.66|  Male|    No|Sun|Dinner|   3|       0.0|    1.0|     0.0|
# |     21.01| 3.5|  Male|    No|Sun|Dinner|   3|       0.0|    1.0|     0.0|
# +----------+----+------+------+---+------+----+----------+-------+--------+
# only showing top 3 rows

# ======================================================================================================================
# Partition Key will divide the rows of data of a dataframe into distinct sets
# Allows you to horizontally scale processing by distributing the data across nodes
# Consider a dataframe with Car information.  possible partition keys are
# 1. Color, 2. Make, 3. Vin Number

# Logical Partitions are the groups formed by a selected partition key.
# e.g. you could set a distinct group for each car color
# You can further re-group the logical partitions into physical partitions
# e.g. if you hash the colors you could group a subset of colors into one physical partition
# This way the number of logical partitions will be scaled down into smaller groups of physical partitions

# Considerations for choosing a partition key:
# a) Storage distribution uniformity across the partitions (a hot partition = too many rows of data)
#    e.g hashing the vin-numbers of the cars will allow you to partition evenly into Logical Groups
# b) High Cardinality = High number of Unique Values  
#    e.g. Vin number is perfect as ALL the numbers are unique which will create perfectly uniform Logical partitions
#    hashing the color or fuel_type would not be as successful
# c) Good distinctness at any given time (sec)
#    better to choose a key that will not cause the number of rows in each partition to vary with time.   


# https://sparkbyexamples.com/apache-hive/hive-show-all-table-partitions/
# https://sparkbyexamples.com/apache-hive/hive-update-or-drop-hive-partition

# Hash Partitioner: 
# Range Partitioner: 
# ======================================================================================================================
