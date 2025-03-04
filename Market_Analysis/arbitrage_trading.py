import requests

def get_coindcx_price():
    response = requests.get("https://api.coindcx.com/exchange/ticker")
    data = response.json()

    for item in data:
        if item['market'] == 'BTCUSDT':
            return float(item['last_price'])
    return None  

def get_delta_price():
    response = requests.get("https://api.delta.exchange/v2/tickers")
    data = response.json()

    for item in data['result']:
        if item['symbol'] == 'BTCUSDT':
            return float(item['close'])
    return None  

coindcx_price = get_coindcx_price()
delta_price = get_delta_price()

if coindcx_price and delta_price:
    print(f"✅ CoinDCX BTC Price: {coindcx_price}")
    print(f"✅ Delta BTC Price: {delta_price}")

    # Arbitrage Opportunity Calculation
    if delta_price > coindcx_price:
        print(f"📈 Buy from CoinDCX @ {coindcx_price} & Sell on Delta @ {delta_price} (Profit: {delta_price - coindcx_price})")
    elif coindcx_price > delta_price:
        print(f"📉 Buy from Delta @ {delta_price} & Sell on CoinDCX @ {coindcx_price} (Profit: {coindcx_price - delta_price})")
    else:
        print("🔍 No Arbitrage Opportunity Right Now!")
else:
    print("⚠️ Error fetching prices from one of the exchanges!")
