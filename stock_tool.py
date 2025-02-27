import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, period="1mo", interval="1d"):
    """
    Fetch stock price data using yfinance.
    
    :param ticker: Stock symbol (e.g., "AAPL" for Apple).
    :param period: How much history to fetch (default: 1 month).
    :param interval: Data interval (default: daily prices).
    :return: Pandas DataFrame containing stock data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

def visualize_stock_data(data, ticker):
    """
    Plot the stock price trends.
    
    :param data: DataFrame containing stock prices.
    :param ticker: Stock symbol.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label=f"{ticker} Closing Price", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker} Stock Price Trends")
    plt.legend()
    plt.grid()
    plt.show()
