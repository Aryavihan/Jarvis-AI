import time
import random

# Simulated balance for paper trading
balance = {'USDT': 10000, 'BTC': 0.0}
trading_pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT', 'XRP/USDT', 'MATIC/USDT']

def get_mock_price():
    """Simulates fetching real-time prices."""
    return {pair: round(random.uniform(50, 50000), 2) for pair in trading_pairs}

def trade_logic():
    global balance
    prices = get_mock_price()
    for pair in trading_pairs:
        if 'USDT' in pair:
            buy_price = prices[pair]
            sell_price = buy_price + random.uniform(5, 50)  # Simulating price fluctuation
            profit = sell_price - buy_price

            if profit > 10:  # Minimum profit threshold
                balance['USDT'] += profit
                print(f'✅ {pair}: Simulated Buy @ {buy_price}, Sell @ {sell_price} (Profit: {profit:.2f} USDT)')
                print(f'💰 Updated Balance: USDT: {balance["USDT"]:.2f}, BTC: {balance["BTC"]:.6f}')
            else:
                print(f'⚠️ No Significant Arbitrage Opportunity for {pair}.')

# Run paper trading for 1 week
for _ in range(7 * 24 * 60):  # Simulate 1-minute updates for 7 days
    trade_logic()
    time.sleep(1)
