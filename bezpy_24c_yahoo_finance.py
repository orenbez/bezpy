from datetime import datetime as dt
import pandas as pd
import requests
# see https://blog.coupler.io/yahoo-finance-to-excel/#How_to_export_a_table_from_Yahoo_Finance_to_Excel

def get_yahoo_cookie():
    cookie = None
    user_agent_key = "User-Agent"
    user_agent_value = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

    headers = {user_agent_key: user_agent_value}
    response = requests.get("https://fc.yahoo.com", headers=headers, allow_redirects=True)

    if not response.cookies:
        raise Exception("Failed to obtain Yahoo auth cookie.")
    cookie = list(response.cookies)[0]
    return cookie


def get_yahoo_crumb(cookie):
    crumb = None
    user_agent_key = "User-Agent"
    user_agent_value = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers = {user_agent_key: user_agent_value}
    crumb_response = requests.get(
        "https://query1.finance.yahoo.com/v1/test/getcrumb",
        headers=headers,
        cookies={cookie.name: cookie.value},
        allow_redirects=True,
    )
    crumb = crumb_response.text

    if crumb is None:
        raise Exception("Failed to retrieve Yahoo crumb.")
    return crumb


def conv_df(resp):
    j = resp.json()
    data = [j['chart']['result'][0]['timestamp']] + list(j['chart']['result'][0]['indicators']['quote'][0].values())
    df = pd.DataFrame(
        {'timestamp': data[0], 'close': data[1], 'open': data[2], 'high': data[3], 'low': data[4], 'volume': data[5]})
    df['time'] = pd.to_datetime(df['timestamp'], unit='s')
    df['date'] = df['time'].apply(lambda x: x.strftime('%Y-%m-%d'))
    return df


if __name__ == '__main__':

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    # ==================================================================================================================
    # No longer working - cookie/crumbs no longer required
    # cookie = get_yahoo_cookie()       # better to cache this if you need to reuse
    # crumb = get_yahoo_crumb(cookie)   # better to cache this if you need to reuse
    # url = f'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1492524105&period2=1495116105&interval=1d&events=history&crumb={crumb}' # 401
    # url = f'https://query2.finance.yahoo.com/v7/finance/quote?symbols={ticker}&crumb={crumb}'  # 401
    # url = f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price&crumb={crumb}'  # 401
    # url = f'https://query2.finance.yahoo.com/v7/finance/quote?symbols={ticker}&fields=regularMarketPreviousClose&region=US&lang=en-US'  # 401
    # >>> data.text
    # '{"finance":{"result":null,"error":{"code":"Unauthorized","description":"User is unable to access this feature - https://bit.ly/yahoo-finance-api-feedback"}}}'
    # ==================================================================================================================
    # No longer working:  'Max retries exceeded with url'
    # url = f'http://ichart.finance.yahoo.com/table.csv?s={ticker}&a=5&b=1&c=2012&d=5&e=1&f=2013&g=d&ignore=.csv'  #  a=5 represents june, g=d means daily, g=w (weekly), g=m (monthly)
    # url = f'http://real-chart.finance.yahoo.com/table.csv?s={ticker}&a=05&b=01&c=2012&d=05&e=01&f=2013&g=d&ignore=.csv'  #  a=05 represents june, g=d means daily
    # url = f'http://finance.yahoo.com/d/quotes.csv?s={ticker}'
    # ==================================================================================================================
    # ==================================================================================================================
    # &period1=: UNIX timestamp representation of the date you wish to start at.
    # &period2=: UNIX timestamp representation of the date you wish to end at.
    # &includePrePost=true => Add pre & post market data
    # &events=div%7Csplit   %7C is hex for |. , will work but internally yahoo uses pipe
    # &interval {'1m', '5m', '15m', '30m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'}
    # ==================================================================================================================
    ticker = 'GOOGL'
    interval = '1d'
    period1 = int(dt(2020, 1, 1).timestamp())
    period2 = int(dt(2020, 1, 5).timestamp())
    base_url = 'https://query2.finance.yahoo.com/v8/finance/chart'
    url = f'{base_url}/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true&ignore=.csv'
    data = requests.get(url, headers=headers)
    conv_df(data)
