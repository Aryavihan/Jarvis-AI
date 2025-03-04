from Jarvis_Market_Analysis import dynamic_reinvest_strategy

def auto_trade(reinvest_amount):
    """
    ✅ Reinvest हुए पैसों को Auto-Trade में लगाता है
    """
    if reinvest_amount > 0:
        print(f"🚀 Starting Auto-Trade with ${reinvest_amount}!")
        # 🔥 यहाँ Trading Strategy जोड़ो (Example: Buy Crypto, Stocks, etc.)
    else:
        print("⚠️ No funds available for reinvestment!")

# Example: Market Condition देखकर Reinvest और Auto-Trade
profit = 500  # 🔹 Example Profit Value
market_condition = "bullish"  # 🔹 Market Condition 

reinvest, compound = dynamic_reinvest_strategy(profit, market_condition)
auto_trade(reinvest)
