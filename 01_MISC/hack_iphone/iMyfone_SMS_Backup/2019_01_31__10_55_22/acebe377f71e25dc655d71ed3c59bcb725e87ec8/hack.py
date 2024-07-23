# Hack for Debbie G to extract her messages from iphone.
# sqlite database was located here and renamed 3d.db
# iMyfone_SMS_Backup\2019_01_31__10_55_22\acebe377f71e25dc655d71ed3c59bcb725e87ec8\3d\3d0d7e5fb2ce288813306e4d4636395e047a3d28


import pandas as pd 
import sqlite3
import sys, os
from datetime import timedelta as td
from dateutil.relativedelta import relativedelta as rd
from datetime import datetime as dt
from datetime import timezone
from pandas import ExcelWriter # needs pip install openpyxl
from tabulate import tabulate

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

# converts ios iphone timestamp to datetime
def ios_dt(ticks):
    secs = ticks/1000000000
    utc = dt(2001, 1, 1) + rd(seconds=secs)
    return utc_to_local(utc)


def dispt(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))


conn = sqlite3.connect('3d.db')
cr = conn.cursor()

cr.execute("select name from sqlite_master where type = 'table'")
print(cr.fetchall()) # lists all tables

# select * from handle where id = '+15169675383';
# select * from message where handle_id in (366,365)  order by ROWID ASC
df = pd.read_sql("select ROWID,text,handle_id,service,account,date, is_from_me from message where handle_id in (366,365)  order by ROWID ASC;", conn)
df['date'] = [ ios_dt(df['date'].iloc[i]) for i in range(len(df))]


cr.close()
conn.close()


writer = ExcelWriter('DebbieG.xlsx')
df.to_excel(writer,'iphone_messages', index=False) # name sheet and supress the index column being printed
writer.save()  # same as writer.close()
