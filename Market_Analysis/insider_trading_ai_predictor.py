import requests
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

# ✅ Finnhub API Key (अपनी API Key यहाँ डालें)
FINNHUB_API_KEY = "cv1bnjpr01qhkk81osfgcv1bnjpr01qhkk81osg0"

# ✅ Finnhub API Endpoint (Insider Trading Data for a Stock)
FINNHUB_API_URL = "https://finnhub.io/api/v1/stock/insider-transactions?symbol={symbol}&token=" + FINNHUB_API_KEY

# ✅ Fetch Insider Trading Data from Finnhub
def get_insider_trading_data(symbol):
    url = FINNHUB_API_URL.format(symbol=symbol)
    response = requests.get(url).json()
    if "data" not in response:
        print(f"⚠️ No insider trading data found for {symbol}!")
        return []
    return response["data"]

# ✅ Fetch Stock Price Data (Last 6 Months)
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="6mo")
    df = df[["Close"]]
    return df

# ✅ Prepare Data for LSTM Model
def prepare_data(df, look_back=30):
    data = df.values
    scaler = MinMaxScaler(feature_range=(0,1))
    data_scaled = scaler.fit_transform(data)

    X, Y = [], []
    for i in range(len(data_scaled) - look_back):
        X.append(data_scaled[i:i+look_back])
        Y.append(data_scaled[i+look_back])

    return np.array(X), np.array(Y), scaler

# ✅ Build & Train LSTM Model
def build_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# ✅ Predict Future Stock Prices
def predict_stock_price(symbol):
    print(f"\n🚀 Fetching Insider Trading Data for {symbol}...")
    insider_trades = get_insider_trading_data(symbol)
    stock_data = get_stock_data(symbol)

    if stock_data.empty:
        print("⚠️ No stock price data available.")
        return
    
    X_train, Y_train, scaler = prepare_data(stock_data)

    # ✅ Train LSTM Model
    model = build_lstm_model((X_train.shape[1], 1))
    model.fit(X_train, Y_train, epochs=20, batch_size=16, verbose=1)

    # ✅ Predict Next 7 Days Prices
    future_prices = []
    input_seq = X_train[-1].reshape(1, X_train.shape[1], 1)
    
    for _ in range(7):
        predicted_price = model.predict(input_seq)
        predicted_price = predicted_price.reshape(1, 1, 1)  # Shape Fix
        future_prices.append(scaler.inverse_transform(predicted_price.reshape(1, -1))[0][0])
        input_seq = np.append(input_seq[:, 1:, :], predicted_price, axis=1)

    print("\n📊 AI-Predicted Stock Prices for Next 7 Days:")
    for i, price in enumerate(future_prices, 1):
        print(f"Day {i}: ${price:.2f}")

    # ✅ Plot Predictions
    plt.figure(figsize=(10,5))
    plt.plot(range(1, 8), future_prices, marker='o', linestyle='dashed', color='blue')
    plt.xlabel("Days Ahead")
    plt.ylabel("Predicted Price")
    plt.title(f"Predicted Stock Prices for {symbol}")
    plt.show()

# ✅ Run AI Prediction for Apple Stock
symbol = "AAPL"
predict_stock_price(symbol)
