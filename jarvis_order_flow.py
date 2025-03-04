import requests
import time

# Delta Exchange API URL
BASE_URL = "https://api.delta.exchange/v2"

# Fetch Order Book Data (Bid/Ask Liquidity)
def get_order_book(symbol="BTCUSDT"):
    response = requests.get(f"{BASE_URL}/l2orderbook/{symbol}")
    if response.status_code == 200:
        data = response.json()['result']
        bids = data["buy"][:5]  # Top 5 Buy Orders
        asks = data["sell"][:5]  # Top 5 Sell Orders
        return bids, asks
    return None, None

# Calculate Order Flow Delta (Buy vs. Sell Strength)
def calculate_order_flow(bids, asks):
    total_bid_vol = sum(order["size"] for order in bids)
    total_ask_vol = sum(order["size"] for order in asks)
    delta = total_bid_vol - total_ask_vol  # Positive = Bullish, Negative = Bearish
    return total_bid_vol, total_ask_vol, delta

# Main Function (Continuous Monitoring)
def main():
    while True:
        bids, asks = get_order_book()
        if bids and asks:
            bid_vol, ask_vol, delta = calculate_order_flow(bids, asks)

            print("\n🔹 Order Flow Analysis (BTCUSDT)")
            print(f"💰 Total Buy Volume: {bid_vol} BTC")
            print(f"📉 Total Sell Volume: {ask_vol} BTC")
            print(f"📊 Order Flow Delta: {delta} BTC")

            if delta > 0:
                print("✅ **Bullish Momentum - Buyers are Strong!**")
            elif delta < 0:
                print("❌ **Bearish Momentum - Sellers are Dominating!**")
            else:
                print("⚠️ **Market is Balanced - No Clear Trend!**")

        else:
            print("⚠️ Failed to fetch order book data. Retrying...")

        time.sleep(5)  # हर 5 सेकंड में अपडेट होगा

if __name__ == "__main__":
    main()
