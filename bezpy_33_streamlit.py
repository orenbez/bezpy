# PART1: https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020
# PART2: https://towardsdatascience.com/how-to-build-a-simple-machine-learning-web-app-in-python-68a45a0e0291
# To run enter on command prompt

# > streamlit run bezPY_streamlit.py
# You can now view your Streamlit app in your browser.
# Local   URL: http://localhost:8501
# Network URL: http://10.0.0.11:8501

import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")


#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
