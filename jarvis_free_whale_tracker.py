import requests
import time

# Free APIs for Whale Tracking (No Paid Plan Required)
BTC_API_URL = "https://blockchain.info/unconfirmed-transactions?format=json"
ETH_API_URL = "https://api.etherscan.io/api"

# Minimum Whale Transaction Amounts
MIN_BTC_AMOUNT = 500  # 500 BTC से ऊपर की Transactions Track करें
MIN_ETH_AMOUNT = 10000  # 10,000 ETH से ऊपर की Transactions Track करें

# Free Etherscan API Key (अपना Free API Key यहाँ डालो)
ETHERSCAN_API_KEY = "X9G6YVVTN2IENRUMV2Y42HK8C1X62H4NVC"

# Function to Fetch Bitcoin Whale Transactions
def get_btc_whale_transactions():
    response = requests.get(BTC_API_URL)
    if response.status_code == 200:
        data = response.json()
        transactions = data["txs"]
        
        for tx in transactions:
            btc_value = sum([out["value"] for out in tx["out"]]) / 100000000  # Convert Satoshi to BTC
            if btc_value >= MIN_BTC_AMOUNT:
                print("\n🐳 **BTC Whale Alert!**")
                print(f"🔹 {btc_value} BTC moved!")
                print(f"🔗 Transaction ID: {tx['hash']}")
                print(f"⏳ Confirmations: {tx['block_height'] if 'block_height' in tx else 'Unconfirmed'}")
                print("⚠️ Possible Market Impact!")

# Function to Fetch Ethereum Whale Transactions
def get_eth_whale_transactions():
    params = {
        "module": "account",
        "action": "txlist",
        "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",  # Example: Binance ETH Wallet
        "apikey": ETHERSCAN_API_KEY
    }
    response = requests.get(ETH_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            for tx in data["result"]:
                eth_value = int(tx["value"]) / 10**18  # Convert Wei to ETH
                if eth_value >= MIN_ETH_AMOUNT:
                    print("\n🐳 **ETH Whale Alert!**")
                    print(f"🔹 {eth_value} ETH moved!")
                    print(f"🔗 Transaction Hash: {tx['hash']}")
                    print(f"📤 From: {tx['from']}")
                    print(f"📥 To: {tx['to']}")
                    print("⚠️ Possible Market Impact!")

# Main Function (Continuous Monitoring)
def main():
    while True:
        print("\n🔍 Checking for Whale Transactions...")
        get_btc_whale_transactions()
        get_eth_whale_transactions()
        time.sleep(10)  # हर 10 सेकंड में Data Check होगा

if __name__ == "__main__":
    main()
