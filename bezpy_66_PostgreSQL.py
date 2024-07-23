# PostgreSQL
# see '16_POSTGRESQL\PostgreSQL_Practice_DB.sql'

from sqlalchemy import create_engine, inspect
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
import psycopg2  # requires `pip install psycopg2`
import pandas as pd


# ======================================================================================================================
conn = psycopg2.connect('dbname=Socratica user=postgres password=badge7383')
cr = conn.cursor()
cr.execute('SELECT COUNT(*) FROM test')
response = cr.fetchone()
cr.close()
conn.close()
# ======================================================================================================================

engine = create_engine('postgresql+psycopg2://postgres:badge7383@localhost:5432/Socratica')
Session = sessionmaker(bind=engine)
session = Session()
#session.execute('exec SP_UPDATE_STUFF')
#session.commit()
session.close() # releases resources


#query_result = pd.read_sql(sql_query, engine)

inspector = inspect(engine)
print(inspector.get_table_names())  # Replaces depricated  engine.table_names()
df = pd.read_csv('https://raw.githubusercontent.com/socratica/sql/master/earthquake.csv')
df.to_sql('Earthquakes', engine, schema=None, if_exists='append', index=True, index_label=None, chunksize=None, dtype=None)


