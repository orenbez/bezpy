# Based on https://towardsdatascience.com/4-ways-to-write-data-to-parquet-with-python-a-comparison-3c4f54ee5fec
# Parquet is a columnar storage format in  byte strings (byte streams) that is designed to optimise data processing
# and querying performance while minimising storage space i.e. faster & smaller  than txt files (csv).


# PyArrow is a high-performance Python library for working with Apache Arrow data.
# It provides a fast and memory-efficient implementation of the Parquet file format,
# which can improve the write performance of parquet files.
# PyArrow supports a range of compression algorithms, including gzip, snappy and LZ4
# gzip = high compression ratios (smaller Parquet files), at the cost of slower compression and decompression speeds

# ======================================================================================================================
# 1. Pandas
# ======================================================================================================================
# converts df to parquet, with default of compression='snappy'
# 'fastparquet' engine requires pip install fastparquet
# 'pyarrow' engine requires pip install pyarrow
# options for engine='pyarrow' or engine='fastparquet'
# options for compression={'snappy', 'gzip', 'brotli', None}, default='snappy'.
# ======================================================================================================================
import pandas as pd


df = pd.read_csv('mydata/heights.csv')

df.to_parquet('mydata/heights.parquet', engine='pyarrow', compression='gzip')
df2 = pd.read_parquet('mydata/heights.parquet', engine='pyarrow')

# ======================================================================================================================
# 2. Pandas with fastparquet
# ======================================================================================================================
# can append to parquet file in batches with option append=True which you can't do with to_parquet()
# ======================================================================================================================
import fastparquet as fp
fp.write('mydata/heights2.parquet', df, compression='gzip', append=True)

# ======================================================================================================================
# 3. Pandas with pyarrow, can use a schema
# ======================================================================================================================
import pyarrow as pa
import pyarrow.parquet as pq

# SETTING BATCH SIZE
batch_size = 250

parquet_schema = pa.schema([('as_of_date', pa.timestamp('ns')),
                            ('company_code', pa.string()),
                            ('fc_balance', pa.float32()),
                            ('fc_currency_code', pa.string()),
                            ('gl_account_number', pa.string()),
                            ('gl_account_name', pa.string())])

parquet_file = 'example_pa.parquet'

df = pd.DataFrame(data, columns=list(parquet_schema.names))
df = df.astype(pandas_schema)
table = pa.Table.from_pandas(df)

with pq.ParquetWriter(parquet_file, parquet_schema, compression='gzip') as writer:
    writer.write_table(table)

# ======================================================================================================================
# 4. Pyspark
# mode = overwrite or append
# ======================================================================================================================

from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark import SparkConf

# WRITING TO PARQUET
df.write.mode('overwrite').option('compression', 'gzip').parquet("example_pyspark_final.parquet")
df.show()