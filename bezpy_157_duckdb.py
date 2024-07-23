# https://pypi.org/project/duckdb/
# pip install duckdb==0.10.1, API for DuckDB, a fast in-process analytical database
# in-process means the DBMS features are running from within the application you’re trying to access from instead of an external process your application connects to
# Source: Basic API usage - https://duckdb.org/docs/api/python/overview.html
# DuckDB is an OLAP database, leverages a SQL query execution engine capable of running complex queries on large datasets

# OnLine Analytical Processing (OLAP) database  => large datasets
# OnLine Transaction Processing (OLTP) database => smaller datasets.  many updates, inserts e.t.c.


import duckdb
connection = duckdb.connect()  # new database will be created.

duckdb.sql('SELECT 42').show()
duckdb.sql('SELECT 42').fetchall()    # [(42,)]
duckdb.sql('SELECT 42').df()          # convert to dataframe

duckdb.read_csv('example.csv') # read a CSV file into a Relation
duckdb.read_parquet('example.parquet')# read a Parquet file into a Relation
duckdb.read_json('example.json') # read a JSON file into a Relation

duckdb.sql('SELECT * FROM "example.csv"')     # directly query a CSV file