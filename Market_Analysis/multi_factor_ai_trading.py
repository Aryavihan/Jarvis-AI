import requests
import yfinance as yf
import pandas as pd
from textblob import TextBlob
import tweepy

# Google News & Twitter API Keys
GOOGLE_NEWS_API_KEY = "YOUR_GOOGLE_NEWS_API_KEY"
TWITTER_BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"

# Stock Symbols
stock_symbols = ["AAPL", "TSLA"]

# Twitter API Authentication
def get_twitter_sentiment(keyword):
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    query = f"{keyword} -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=10)
    sentiment_scores = [TextBlob(tweet.text).sentiment.polarity for tweet in tweets.data or []]
    return sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

# Function to Fetch Sentiment Score
def get_sentiment_score(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={GOOGLE_NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    sentiment_scores = [TextBlob(article["title"]).sentiment.polarity for article in articles[:5]]
    news_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
    
    twitter_sentiment = get_twitter_sentiment(keyword)
    return (news_sentiment + twitter_sentiment) / 2

# Function to Fetch Insider Trading Data
def get_insider_trading(symbol):
    # Dummy Data (Replace with API Call for Real Data)
    insider_trades = {"AAPL": -50000, "TSLA": 20000}  # Negative means selling, Positive means buying
    return insider_trades.get(symbol, 0)

# Function to Fetch Technical Indicators
def get_technical_indicators(symbol):
    data = yf.Ticker(symbol).history(period="3mo")
    data["50MA"] = data["Close"].rolling(window=50).mean()
    data["200MA"] = data["Close"].rolling(window=200).mean()
    last_row = data.iloc[-1]
    return last_row["50MA"], last_row["200MA"], last_row["Close"]

# Function to Execute Stock Trade (Simulation Mode)
def execute_stock_trade(symbol, action):
    print(f"📈 Simulated {action} Order for {symbol}")

# Main Execution
for stock in stock_symbols:
    sentiment_score = get_sentiment_score(stock)
    insider_trade = get_insider_trading(stock)
    ma50, ma200, close_price = get_technical_indicators(stock)
    
    decision = "HOLD"
    
    # Multi-Factor Decision Making
    if sentiment_score > 0.15 and insider_trade > 10000 and close_price > ma50 > ma200:
        decision = "BUY"
    elif sentiment_score < -0.15 and insider_trade < -10000 and close_price < ma50:
        decision = "SELL"
    
    print(f"📊 {stock} - Sentiment Score: {sentiment_score:.2f} | Insider Trade: {insider_trade} | AI Decision: {decision}")
    execute_stock_trade(stock, decision)
