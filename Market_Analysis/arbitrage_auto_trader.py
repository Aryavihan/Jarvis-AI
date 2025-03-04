import ccxt
import requests
import time

# Delta Exchange API Setup
delta = ccxt.delta({
    'apiKey': 'JUlpC8xzMppNXNmDQdEoQqNN6WQi64',
    'secret': 'JUlpC8xzMppNXNmDQdEoQqNN6WQi64'
})

# CoinDCX API Setup
COINDCX_API_URL = "https://api.coindcx.com/exchange/ticker"

def get_delta_price():
    try:
        ticker = delta.fetch_ticker('BTC/USDT')
        return ticker['last']
    except Exception as e:
        print(f"❌ Delta API Error: {e}")
        return None

def get_coindcx_price():
    try:
        response = requests.get(COINDCX_API_URL)
        data = response.json()
        for ticker in data:
            if ticker['market'] == 'BTCUSDT':
                return float(ticker['last_price'])
    except Exception as e:
        print(f"❌ CoinDCX API Error: {e}")
        return None

def execute_trade(delta_price, coindcx_price):
    profit = coindcx_price - delta_price
    if profit > 10:  # Arbitrage Threshold
        print(f"📉 Buy from Delta @ {delta_price} & Sell on CoinDCX @ {coindcx_price} (Profit: {profit} USDT)")
        # TODO: Add Auto-Execution Logic Here
    else:
        print("⚠️ No Significant Arbitrage Opportunity.")

while True:
    delta_price = get_delta_price()
    coindcx_price = get_coindcx_price()
    if delta_price and coindcx_price:
        print(f"✅ Delta BTC Price: {delta_price}")
        print(f"✅ CoinDCX BTC Price: {coindcx_price}")
        execute_trade(delta_price, coindcx_price)
    time.sleep(5)  # Fetch every 5 seconds
