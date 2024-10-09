import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""# Данные котировок компании Apple""")

tickerSymb = 'AAPL'
tickerData = yf.Ticker(tickerSymb)
tickerDf = tickerData.history(period= "1d", start = '2010-9-30', end = '2024-9-30')


st.write("""### Цена закрытия акций за каждый год""")

st.line_chart(tickerDf.Close)

st.write("""### Объем продаж за каждый год""")

st.line_chart(tickerDf.Volume)
