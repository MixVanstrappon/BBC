import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

# 글로벌 시가총액 상위 10개 기업의 티커 목록
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'BRK-B', 'NVDA', 'META', 'TSM', 'V']

# 최근 1년간 주가 데이터 다운로드
data = yf.download(tickers, period="1y")['Adj Close']

# Plotly를 사용하여 시각화
fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(x=data.index, y=data[ticker], mode='lines', name=ticker))

# 레이아웃 설정
fig.update_layout(
    title='Global Top 10 Market Cap Stocks - 1 Year Price Change',
    xaxis_title='Date',
    yaxis_title='Adjusted Close Price (USD)',
    template='plotly_dark'
)

# Streamlit 애플리케이션 구성
st.title('Global Top 10 Market Cap Stocks - 1 Year Price Change')
st.plotly_chart(fig)
