import requests
import json
from textblob import TextBlob
from newspaper import Article

# ✅ Fix: Correct API Key Syntax
GOOGLE_NEWS_API_KEY = "c2069a68e5d54a3d9ddc52a682f60800"  # Replace with your actual API key

# ✅ Fix: Fetch Latest News from Google
def get_google_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={GOOGLE_NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    return [article["url"] for article in articles[:5]] if articles else []

# ✅ Fix: Extract News Content
def get_news_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error extracting article: {e}")
        return None

# ✅ Fix: Sentiment Analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # -1 (Negative) to +1 (Positive)

# ✅ Fix: Get Market Sentiment
def get_market_sentiment(keyword):
    news_urls = get_google_news(keyword)
    if not news_urls:
        print("No news articles found.")
        return 0
    
    news_texts = [get_news_content(url) for url in news_urls if url]
    sentiments = [analyze_sentiment(text) for text in news_texts if text]
    
    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
    return avg_sentiment

# ✅ Test Execution
keyword = "Bitcoin"
market_sentiment = get_market_sentiment(keyword)
print(f"🚀 Market Sentiment for {keyword}: {market_sentiment}")
