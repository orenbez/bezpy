import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from scipy import stats
from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer, Date, BIGINT, Float



def dbconnect():
    global engine
    conn_str = r"mssql+pyodbc://ro:Tsc7354%40!@192.168.150.17:1433/WangExport?driver=SQL+Server+Native+Client+11.0"
    try:
        engine = create_engine(conn_str, echo=False)
    except:
        print('Database Connectivity issue')
        exit(1)


dbconnect()        
query = """  SELECT DATEDIFF(day, [QuoteCreatedDate],[PolicyIssueDate]) as LeadToSale
              FROM [WangExport].[dbo].[LEAD_DATA_HIST_3YRS]  
              Where PolicyIssueDate is not NULL AND AITPolicyNumber <> ''
              --AND DATEDIFF(day, [QuoteCreatedDate],[PolicyIssueDate]) < 100
              AND [QuoteCreatedDate] >= '2019-01-10'"""


df = pd.read_sql(query, con=engine)

#Pandas Plot
df['LeadToSale'].plot(kind='kde')
plt.show()

#Pandas Histogram
df['LeadToSale'].hist(color = 'blue', edgecolor = 'black',bins=1400, grid=True)
plt.show()


# matplotlib histogram
plt.hist(df['LeadToSale'], color = 'blue', edgecolor = 'black',bins=1400)


# seaborn histogram
sns.distplot(df['LeadToSale'], hist=True, kde=False, 
             bins=1400, color = 'blue',
             hist_kws={'edgecolor':'black'})

# Add labels
plt.title('Time for Leads To Sale')
plt.xlabel('Time (days)')
plt.ylabel('Frequency')
plt.show()
