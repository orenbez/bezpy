# https://pypi.org/project/yfinance
# https://medium.com/the-handbook-of-coding-in-finance/building-financial-data-storage-with-postgresql-in-python-b981e38826fe
# also see bezpy_85_investpy
import psycopg2
import yfinance as yf
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

ticker = 'AAPL'
stock_data = yf.download(ticker, start='2021-8-1', end="2021-9-1")
stock_data.index = np.datetime_as_string(stock_data.index, unit='D')
stock_data['Ticker'] = ticker
stock_data = stock_data.rename(columns={"Adj Close": "Adj_Close"})
records = stock_data.to_records(index=True)

conn = psycopg2.connect(database="postgres", user='postgres', password='badge7383', host='127.0.0.1', port= '5432')
cursor = conn.cursor()

sql = r'''SELECT 'CREATE DATABASE stocks' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'stocks')\gexec'''
cursor.execute(sql)
print("Database stocks created successfully!")
cursor.execute('''CREATE TABLE IF NOT EXISTS prices
                   (Date DATE NOT NULL,
                    Open FLOAT NOT NULL,
                    High FLOAT NOT NULL,
                    Low FLOAT NOT NULL,
                    Close FLOAT NOT NULL,
                    Adj_Close FLOAT NOT NULL,
                    Volume BIGINT NOT NULL,
                    Ticker VARCHAR(255) NOT NULL);''')
print("Table created successfully")

query = """INSERT INTO prices (Date, Open, High, Low, Close, Adj_Close, Volume, Ticker)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
cursor.executemany(query, records)
print("Data Insert Successfully")

conn.close()