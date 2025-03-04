from sklearn.preprocessing import MinMaxScaler
import requests
import yfinance as yf
import pandas as pd
from textblob import TextBlob
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Google News API Key
GOOGLE_NEWS_API_KEY = "c2069a68e5d54a3d9ddc52a682f60800"

# Stock Symbols
stock_symbols = ["AAPL", "TSLA"]

# Function to Fetch Sentiment Score
def get_sentiment_score(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={GOOGLE_NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    sentiment_scores = [TextBlob(article["title"]).sentiment.polarity for article in articles[:5]]
    news_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
    return news_sentiment

# Function to Fetch Insider Trading Data
def get_insider_trading(symbol):
    insider_trades = {"AAPL": -50000, "TSLA": 20000}
    return insider_trades.get(symbol, 0)

# Function to Fetch Technical Indicators
def get_technical_indicators(symbol):
    data = yf.Ticker(symbol).history(period="6mo")
    data["50MA"] = data["Close"].rolling(window=50).mean()
    data["200MA"] = data["Close"].rolling(window=200).mean()
    last_row = data.iloc[-1]
    return last_row["50MA"], last_row["200MA"], last_row["Close"]

# AI Model for Future Price Prediction
def train_price_model(symbol):
    data = yf.Ticker(symbol).history(period="1y")["Close"]
    data = data.values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)
    X, y = [], []
    for i in range(60, len(data_scaled)):
        X.append(data_scaled[i-60:i, 0])
        y.append(data_scaled[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
        LSTM(50, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X, y, epochs=20, batch_size=16, verbose=0)
    return model, scaler

# Function to Predict Future Price
def predict_future_price(symbol):
    model, scaler = train_price_model(symbol)
    data = yf.Ticker(symbol).history(period="3mo")["Close"]
    data = data.values.reshape(-1, 1)
    data_scaled = scaler.transform(data)
    X_input = np.reshape(data_scaled[-60:], (1, 60, 1))
    predicted_price = scaler.inverse_transform(model.predict(X_input))
    return predicted_price[0][0]

# Function to Execute Stock Trade (Simulation Mode)
def execute_stock_trade(symbol, action):
    print(f"\U0001F4C8 Simulated {action} Order for {symbol}")

# Main Execution
for stock in stock_symbols:
    sentiment_score = get_sentiment_score(stock)
    insider_trade = get_insider_trading(stock)
    ma50, ma200, close_price = get_technical_indicators(stock)
    future_price = predict_future_price(stock)
    
    decision = "HOLD"
    if sentiment_score > 0.15 and insider_trade > 10000 and close_price > ma50 > ma200 and future_price > close_price:
        decision = "BUY"
    elif sentiment_score < -0.15 and insider_trade < -10000 and close_price < ma50 and future_price < close_price:
        decision = "SELL"
    
    print(f"\U0001F4CA {stock} - Sentiment Score: {sentiment_score:.2f} | Insider Trade: {insider_trade} | AI Predicted Price: {future_price:.2f} | AI Decision: {decision}")
    execute_stock_trade(stock, decision)
