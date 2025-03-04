import requests
import ccxt
import yfinance as yf
import pandas as pd
import numpy as np
import time

# ✅ Binance API Setup (Crypto Trading)
BINANCE_API_KEY = "YOUR_BINANCE_API_KEY"
BINANCE_SECRET_KEY = "YOUR_BINANCE_SECRET_KEY"
exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_SECRET_KEY,
    'enableRateLimit': True
})

# ✅ Stock Market API (Yahoo Finance)
def get_stock_data(symbol, period="1d", interval="1h"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period, interval=interval)
    return df

# ✅ Crypto Market Data (Binance)
def get_crypto_data(symbol, timeframe='1h'):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    return df

# ✅ Simple AI Trading Strategy (Moving Averages)
def generate_trading_signal(df):
    df['MA50'] = df['close'].rolling(window=50).mean()
    df['MA200'] = df['close'].rolling(window=200).mean()
    df['Signal'] = "HOLD"
    df.loc[df['MA50'] > df['MA200'], 'Signal'] = "BUY"
    df.loc[df['MA50'] < df['MA200'], 'Signal'] = "SELL"
    return df

# ✅ Auto Trading Execution (Crypto)
def execute_crypto_trade(symbol, signal, amount):
    if signal == "BUY":
        order = exchange.create_market_buy_order(symbol, amount)
        print(f"✅ BUY ORDER PLACED: {symbol} | Amount: {amount}")
    elif signal == "SELL":
        order = exchange.create_market_sell_order(symbol, amount)
        print(f"✅ SELL ORDER PLACED: {symbol} | Amount: {amount}")

# ✅ Main AI Trading Execution
crypto_symbol = "BTC/USDT"
stock_symbol = "AAPL"

while True:
    print("\n🚀 Fetching Market Data...")
    
    # Fetch Data
    crypto_data = get_crypto_data(crypto_symbol)
    stock_data = get_stock_data(stock_symbol)
    
    # Generate Signals
    crypto_data = generate_trading_signal(crypto_data)
    stock_data = generate_trading_signal(stock_data)
    
    latest_crypto_signal = crypto_data['Signal'].iloc[-1]
    latest_stock_signal = stock_data['Signal'].iloc[-1]
    
    print(f"📈 Crypto Signal for {crypto_symbol}: {latest_crypto_signal}")
    print(f"📊 Stock Signal for {stock_symbol}: {latest_stock_signal}")
    
    # Execute Crypto Trade (Auto Trading Enabled)
    execute_crypto_trade(crypto_symbol, latest_crypto_signal, 0.001)
    
    print("⏳ Waiting for next cycle...")
    time.sleep(3600)  # Run every 1 hour
