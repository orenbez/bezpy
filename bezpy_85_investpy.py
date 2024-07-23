# Requires pip install investpy
# 11/04/21 investpy-1.0.7
# https://pypi.org/project/investpy/
# investpy is a Python package to retrieve data from Investing.com
# SEE bezpy_24_yahoo_finance.py for better tools

from datetime import datetime as dt
from investpy import get_stock_historical_data, get_bond_historical_data


# Define a start date and End Date  dd/mm/YYYY
start = '01/01/2021'
#setting today date as End Date
end = dt.today().strftime('%d/%m/%Y')

## Returns DataFrame - Read Stock Price Data (Eg Apple Stock Price)  NO Adj_Close field though
AAPL = get_stock_historical_data(stock='AAPL',country='United States',from_date=start,to_date=end)

## Returns DataFrame - Read Bond Price Data (Eg Malaysia 10-Year Bond Yield)
MSIA = get_bond_historical_data(bond='Malaysia 10Y', from_date=start, to_date=end)