def smart_reinvest(profit, reinvest_ratio=0.5):
    """
    ✅ Profit को Reinvest और Compound में Split करता है
    🔹 reinvest_ratio = कितने % को Reinvest करना है (Default: 50%)
    """
    reinvest_amount = profit * reinvest_ratio
    compound_amount = profit - reinvest_amount
    
    print(f"✅ Total Profit: ${profit}")
    print(f"🔄 Reinvesting: ${reinvest_amount}")
    print(f"📈 Compounding: ${compound_amount}")
    
    return reinvest_amount, compound_amount
