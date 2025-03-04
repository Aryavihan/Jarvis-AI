import requests
import pandas as pd

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

# ✅ Smart Analysis for Insider Trading
def analyze_insider_trading(symbol):
    print(f"\n🚀 Fetching Insider Trading Data for {symbol}...")
    insider_trades = get_insider_trading_data(symbol)

    if not insider_trades:
        print(f"⚠️ No insider activity detected for {symbol}.")
        return

    df = pd.DataFrame(insider_trades)
    df = df[["name", "share", "change", "transactionPrice", "filingDate"]]

    # ✅ Filter Large Trades (More than 10,000 shares)
    large_trades = df[abs(df["change"]) > 10000]

    if large_trades.empty:
        print("⚠️ No significant insider trades detected.")
    else:
        print("\n📊 🔥 Large Insider Trades (10K+ shares):")
        print(large_trades.to_string(index=False))

    # ✅ Analyze Trend (More Buying or Selling?)
    total_buys = df[df["change"] > 0]["change"].sum()
    total_sells = abs(df[df["change"] < 0]["change"].sum())

    if total_buys > total_sells:
        print("\n✅ Insider Trend: BULLISH (More Buying)")
    elif total_sells > total_buys:
        print("\n❌ Insider Trend: BEARISH (More Selling)")
    else:
        print("\n⚖️ Insider Trend: NEUTRAL (Balanced Buying/Selling)")

# ✅ Test with a Stock Symbol
symbol = "AAPL"  # Apple Stock
analyze_insider_trading(symbol)
