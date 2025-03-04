import requests
import time

# Whale Alert API (Free API का इस्तेमाल कर रहे हैं)
WHALE_ALERT_API_KEY = "YOUR_API_KEY"  # अपना API Key यहां डालो
WHALE_ALERT_URL = "https://api.whale-alert.io/v1/transactions"

# Minimum Whale Transaction Amount (BTC & ETH)
MIN_BTC_AMOUNT = 500  # कम से कम 500 BTC की Transactions Track करें
MIN_ETH_AMOUNT = 10000  # कम से कम 10,000 ETH की Transactions Track करें

# Function to Fetch Whale Transactions
def get_whale_transactions():
    params = {
        "api_key": WHALE_ALERT_API_KEY,
        "min_value": 1000000,  # $1M+ की Transactions
        "currency": "btc,eth"  # BTC और ETH को Track करें
    }
    
    response = requests.get(WHALE_ALERT_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    return None

# Main Function for Tracking Whales
def main():
    while True:
        whale_data = get_whale_transactions()
        
        if whale_data and "transactions" in whale_data:
            for tx in whale_data["transactions"]:
                amount = tx["amount"]
                currency = tx["symbol"].upper()
                from_address = tx["from"]["owner"] if "owner" in tx["from"] else "Unknown"
                to_address = tx["to"]["owner"] if "owner" in tx["to"] else "Unknown"
                value_usd = tx["amount_usd"]
                
                if (currency == "BTC" and amount >= MIN_BTC_AMOUNT) or (currency == "ETH" and amount >= MIN_ETH_AMOUNT):
                    print(f"\n🐳 **Whale Alert Detected!**")
                    print(f"🔹 {amount} {currency} (${value_usd} USD) Moved")
                    print(f"📤 From: {from_address}")
                    print(f"📥 To: {to_address}")
                    
                    if "exchange" in from_address.lower():
                        print("❌ **Whale Selling! (Bearish Sign)**")
                    elif "exchange" in to_address.lower():
                        print("✅ **Whale Buying! (Bullish Sign)**")
                    else:
                        print("⚠️ **Unusual Whale Activity Detected!**")

        else:
            print("⚠️ No Whale Transactions Detected. Retrying...")

        time.sleep(10)  # हर 10 सेकंड में Update होगा

if __name__ == "__main__":
    main()
