from Jarvis_Reinvest import smart_reinvest

def dynamic_reinvest_strategy(profit, market_condition="neutral"):
    """
    ✅ Market Condition देखकर Reinvest और Compound Ratio Set करता है
    🔹 market_condition: "bullish" (अच्छा) | "neutral" (सामान्य) | "bearish" (खराब)
    """
    ratios = {
        "bullish": 0.7,  # 70% Reinvest, 30% Compound
        "neutral": 0.5,  # 50% Reinvest, 50% Compound
        "bearish": 0.3   # 30% Reinvest, 70% Compound
    }
    
    reinvest_ratio = ratios.get(market_condition, 0.5)
    return smart_reinvest(profit, reinvest_ratio)
