import requests
import time

# Delta Exchange API URL
BASE_URL = "https://api.delta.exchange/v2"

# Fetch BTC & ETH Prices
def get_market_data():
    response = requests.get(f"{BASE_URL}/tickers")
    if response.status_code == 200:
        data = response.json()['result']
        
        # BTC और ETH की Price निकालना
        btc_price = next((item for item in data if item["symbol"] == "BTCUSDT"), None)
        eth_price = next((item for item in data if item["symbol"] == "ETHUSDT"), None)
        
        if btc_price and eth_price:
            return {
                "BTC Price": btc_price["close"],
                "ETH Price": eth_price["close"]
            }
    return None

# Order Book Data Fetch करना (Bid/Ask Prices)
def get_order_book(symbol):
    response = requests.get(f"{BASE_URL}/l2orderbook/{symbol}")
    if response.status_code == 200:
        data = response.json()['result']
        bids = data["buy"]
        asks = data["sell"]
        return {
            "Best Bid": bids[0]["price"] if bids else None,
            "Best Ask": asks[0]["price"] if asks else None
        }
    return None

# Main Function (Live Data Fetch करना हर 5 सेकंड में)
def main():
    while True:
        market_data = get_market_data()
        order_book_btc = get_order_book("BTCUSDT")
        order_book_eth = get_order_book("ETHUSDT")

        if market_data and order_book_btc and order_book_eth:
            print("\n🔹 Live Market Data (BTC/ETH) 🔹")
            print(f"BTC Price: {market_data['BTC Price']} USDT")
            print(f"ETH Price: {market_data['ETH Price']} USDT")
            print(f"BTC Order Book - Bid: {order_book_btc['Best Bid']} USDT, Ask: {order_book_btc['Best Ask']} USDT")
            print(f"ETH Order Book - Bid: {order_book_eth['Best Bid']} USDT, Ask: {order_book_eth['Best Ask']} USDT")

        else:
            print("⚠️ Data Fetching Failed. Retrying...")

        time.sleep(5)  # 5 सेकंड बाद दुबारा Data Fetch करेगा

if __name__ == "__main__":
    main()
