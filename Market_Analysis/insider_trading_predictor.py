import requests
import pandas as pd
import yfinance as yf
from textblob import TextBlob

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

# ✅ Fetch Stock Price Data (Last 3 Months)
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="3mo")
    df = df[["Close"]]
    return df

# ✅ Sentiment Analysis from Insider Trades
def analyze_sentiment(trade_data):
    sentiment_scores = []
    
    for trade in trade_data:
        text = f"{trade['name']} {trade['change']} shares at {trade['transactionPrice']}"
        sentiment = TextBlob(text).sentiment.polarity
        sentiment_scores.append(sentiment)

    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
    return avg_sentiment

# ✅ Predict Market Impact based on Insider Trades
def predict_market_movement(symbol):
    print(f"\n🚀 Fetching Insider Trading Data for {symbol}...")
    insider_trades = get_insider_trading_data(symbol)

    if not insider_trades:
        print(f"⚠️ No insider activity detected for {symbol}.")
        return

    # ✅ Filter Large Trades (More than 10,000 shares)
    df = pd.DataFrame(insider_trades)
    df = df[df["change"].abs() > 10000]
    
    if df.empty:
        print("⚠️ No significant insider trades detected.")
        return

    print("\n📊 🔥 Large Insider Trades:")
    print(df[["name", "change", "transactionPrice", "filingDate"]].to_string(index=False))

    # ✅ Analyze Sentiment
    sentiment_score = analyze_sentiment(insider_trades)
    print(f"\n📢 Insider Trading Sentiment Score: {sentiment_score:.2f}")

    # ✅ Fetch Stock Data
    stock_data = get_stock_data(symbol)
    latest_price = stock_data["Close"].iloc[-1]
    print(f"\n💰 Latest Stock Price: ${latest_price:.2f}")

    # ✅ Predict Future Movement (Basic Logic)
    if sentiment_score > 0 and df["change"].sum() > 0:
        print("\n✅ AI Prediction: Stock Price Likely to GO UP 📈")
    elif sentiment_score < 0 and df["change"].sum() < 0:
        print("\n❌ AI Prediction: Stock Price Likely to DROP 📉")
    else:
        print("\n⚖️ AI Prediction: Neutral / Uncertain Market Movement")

# ✅ Test with a Stock Symbol
symbol = "AAPL"  # Apple Stock
predict_market_movement(symbol)
