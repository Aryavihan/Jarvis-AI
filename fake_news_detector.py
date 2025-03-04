import requests
import json
from textblob import TextBlob
from newspaper import Article
from transformers import pipeline

# ✅ AI Model for Fake News Detection (Updated with Proper Fake/Real Labels)
fake_news_detector = pipeline("text-classification", model="facebook/bart-large-mnli")

# ✅ Google News API Key (Replace with your API key)
GOOGLE_NEWS_API_KEY = "c2069a68e5d54a3d9ddc52a682f60800"

# ✅ Fetch Latest News from Google
def get_google_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={GOOGLE_NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    return [(article["url"], article["title"]) for article in articles[:5]] if articles else []

# ✅ Extract News Content
def get_news_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error extracting article: {e}")
        return None

# ✅ Fake News Detection
def detect_fake_news(text):
    label_scores = fake_news_detector(text[:512], return_all_scores=True)[0]
    real_score = next((x['score'] for x in label_scores if x['label'] == 'ENTAILMENT'), 0)
    fake_score = next((x['score'] for x in label_scores if x['label'] == 'CONTRADICTION'), 0)
    
    return "FAKE" if fake_score > real_score else "REAL"

# ✅ Sentiment Analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # -1 (Negative) to +1 (Positive)

# ✅ Market Sentiment & Fake News Analysis
def analyze_market_news(keyword):
    news_data = get_google_news(keyword)
    if not news_data:
        print("No news articles found.")
        return

    for url, title in news_data:
        print(f"\n📰 News Title: {title}")
        news_text = get_news_content(url)
        if not news_text:
            continue

        sentiment = analyze_sentiment(news_text)
        fake_news_label = detect_fake_news(news_text)

        print(f"📢 Sentiment Score: {sentiment}")
        print(f"🔍 Fake News Detection: {fake_news_label}")

# ✅ Test Execution
keyword = "Bitcoin"
analyze_market_news(keyword)
