# Try this https://towardsdatascience.com/python-stock-analysis-balance-sheet-trend-analysis-18e6eb63cdc
# Try this https://towardsdatascience.com/how-to-get-market-data-from-the-nyse-in-less-than-3-lines-python-41791212709c
# Try this https://towardsdatascience.com/how-we-have-beaten-the-crypto-market-using-machine-learning-a45e8a7dbdcd?source=search_post---------1
# Try https://towardsdatascience.com/backtesting-your-first-trading-strategy-ad3977f3f2a?source=bookmarks---------0----------------------------
# Try https://towardsdatascience.com/choose-stocks-to-invest-with-python-584892e3ad22?source=bookmarks---------0----------------------------
# Also see bezpy_85_investpy.py, also see yahoo_fin
# Also see backtrader library https://algotrading101.com/learn/backtrader-for-backtesting/
# This is a library for backtesting and trading. It allows you to focus on writing reusable trading strategies, indicators, and analyzers instead of having to spend time building infrastructure. It includes lots of features like data feeds from CSV/files, online sources, or from pandas and blaze, Filters for data, like breaking a daily bar into chunks to simulate intraday or working with Renko bricks, and many more.


import pandas as pd
from pandas_datareader import data as pdr  # requires pip install pandas-datareader
import yfinance as yf  # requires 'pip install yfinance'  previously was fix_yahoo_finance
# from yahoofinancials import YahooFinancials  # provides other information - requires pip install yahoofinancials
from datetime import datetime as dt, timedelta as td
import matplotlib.pyplot as plt
from tabulate import tabulate



def tab(df):
    print(tabulate(df, headers='keys', tablefmt='rst'))


def compare():
    # Compare VFINX vs. ^GSPC

    st = dt(2018, 1, 1)
    ed = dt(2020, 9, 22)

    yf.pdr_override()
    d1 = pdr.get_data_yahoo('VFINX', start=st, end=ed)
    d1['PctDiff'] = (d1['Adj Close'] * 100 / d1['Adj Close'].iloc[0]) - 100

    d2 = pdr.get_data_yahoo('^GSPC', start=st, end=ed)
    d2['PctDiff'] = (d2['Adj Close'] * 100 / d2['Adj Close'].iloc[0]) - 100

    df = pd.DataFrame(data={'VFINX_Close': d1['PctDiff'], 'SP500_Close': d2['PctDiff']})

    return df



if __name__ == '__main__':


    df = compare()
    df.plot()
    plt.show()


    # plot display
    plt.style.use('fivethirtyeight')

    # pandas display
    pd.set_option('display.max_rows', 10)  # 5 from head, 5 from tail. Default is 30,30
    pd.set_option('display.max_columns', 20)  # Max number of columns displayed, note number of columns = df.shape[1]
    pd.set_option('display.width', 1000)  # Max chars display on one line
    pd.set_option('max_colwidth', 500)  # Max chars within one column

    symbol = "MSFT"
    # create datetime objects
    st = dt(2020, 1, 1)
    ed = dt(2020, 3, 9)

    msft = yf.Ticker(symbol) # yfinance ticker object
    hist = msft.history(period="max") # get historical market data
    #history(period='1mo', interval='1d', start=None, end=None, prepost=False, actions=True, auto_adjust=True, proxy=None, threads=True, group_by='column', progress=True, **kwargs)

    a = msft.actions # show actions (dividends, splits)
    d = msft.dividends # show dividends
    s = msft.splits  # show splits

    # show financials
    f = msft.financials
    qf = msft.quarterly_financials

    # show major holders
    mh = msft.major_holders

    # show institutional holders
    ih = msft.institutional_holders

    # show balance heet
    bs = msft.balance_sheet
    qbs = msft.quarterly_balance_sheet

    # show cashflow
    cf = msft.cashflow
    qcf = msft.quarterly_cashflow

    # show earnings
    e = msft.earnings
    qe = msft.quarterly_earnings

    # show sustainability
    s = msft.sustainability

    # show analysts recommendations
    r = msft.recommendations

    # show next event (earnings, etc)
    c = msft.calendar

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    isin = msft.isin

    # show options expirations
    opts = msft.options

    # get option chain for specific expiration e.g. 2022-06-16
    # data available via: opt.calls, opt.puts
    expirtation = opts[-1]
    opt = msft.option_chain(expirtation)


    # ==================================================================================================================
    # download() function
    # ==================================================================================================================
    data = yf.download(tickers="SPY AAPL MSFT", period="wtd", interval="1m", group_by='ticker',
                       auto_adjust=True, prepost=True, threads=True, proxy=None)
    # data = yf.download(  # or pdr.get_data_yahoo(...
    #     # tickers list or string as well
    #     tickers="SPY AAPL MSFT",
    #
    #     # use "period" instead of start/end
    #     # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    #     # (optional, default is '1mo')
    #     period="ytd",
    #
    #     # fetch data by interval (including intraday if period < 60 days)
    #     # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    #     # (optional, default is '1d' = day,  also have '1m' = minute, '1h' = hour)
    #     interval="1m",
    #
    #     # group by ticker (to access via data['SPY'])
    #     # (optional, default is 'column')
    #     group_by='ticker',
    #
    #     # adjust all OHLC automatically
    #     # (optional, default is False)
    #     auto_adjust=True,
    #
    #     # download pre/post regular market hours data
    #     # (optional, default is False)
    #     prepost=True,
    #
    #     # use threads for mass downloading? (True/False/Integer)
    #     # (optional, default is True)
    #     threads=True,
    #
    #     # proxy URL scheme use use when downloading?
    #     # (optional, default is None)
    #     proxy=None
    # )


    # ===================================
    # Fetching data for multiple tickers
    # ===================================
    ts = yf.Tickers('MSFT AAPL GOOG')  # returns a named tuple of Ticker objects, tickers are not case sensitive
    ts.symbols # returns ['MSFT', 'AAPL', 'GOOG']
    all_hist = ts.history(interval='1d', start='2020-02-10', end='2020-02-14') # data from all three
    # Note ts.tickers used to be a list, now is a dictionary

    msft_info = ts.tickers['MSFT'].info
    aapl_hist = ts.tickers['AAPL'].history(interval='1d', start='2020-02-10', end='2020-02-14')
    goog_actions = ts.tickers['GOOG'].actions


    # comparison of methods  ALSO see bezpy_83_investpy.com for another method
    stocks = ["MSFT"] # If you want to grab multiple stocks add more labels to this list
    d1 = pdr.get_data_yahoo(stocks, start=st, end=ed)
    d2 = pdr.DataReader(name='MSFT', data_source='yahoo', start=st , end=ed)
    d3 = yf.download(symbol, start=st, end=ed)  # has adj_close value # same as above but excludes end date
    d4 = yf.Ticker(symbol).history(start=st, end=ed, auto_adjust=True)  # no adj close value, data doesn't match other two methods

    plt.clf() # Clean the graph

    d2['Adj Close'].plot()
    plt.legend()        # this will generate the legend in the graph
    plt.show()          # displays the image

    ####################################################################################################################
    #  download data faster, you can “hijack” pandas_datareader.data.get_data_yahoo() method to use yfinance
    yf.pdr_override()  # <== that's all it takes :-)
    # download dataframe
    data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

    # ==================================================================================================================

