import requests
import yfinance as yf
from textblob import TextBlob

# Google News API Key
GOOGLE_NEWS_API_KEY = "c2069a68e5d54a3d9ddc52a682f60800"

# Stock Symbols
stock_symbols = ["AAPL", "TSLA"]

# Function to Fetch Sentiment Score
def get_sentiment_score(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={GOOGLE_NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    sentiment_scores = []
    for article in articles[:5]:  # Top 5 news articles
        text = article["title"] + " " + article.get("description", "")
        sentiment_scores.append(TextBlob(text).sentiment.polarity)
    return sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

# Function to Execute Stock Trade (Simulation Mode)
def execute_stock_trade(symbol, action):
    print(f"📈 Simulated {action} Order for {symbol}")

# Main Execution
for stock in stock_symbols:
    sentiment_score = get_sentiment_score(stock)
    decision = "HOLD"
    if sentiment_score > 0.2:
        decision = "BUY"
    elif sentiment_score < -0.2:
        decision = "SELL"
    print(f"📊 {stock} - Sentiment Score: {sentiment_score:.2f} | AI Decision: {decision}")
    execute_stock_trade(stock, decision)
