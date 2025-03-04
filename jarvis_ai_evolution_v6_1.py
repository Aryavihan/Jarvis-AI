import os
import time
import random
import subprocess
import requests
import json

# 🔹 Jarvis AI Evolution V6.1 (Bug Fix + Market Data API Keys Added)
CODE_FOLDER = "C:\\Users\\home\\Jarvis-AI\\"
LOG_FILE = CODE_FOLDER + "jarvis_agent_log.txt"
DATA_FILE = CODE_FOLDER + "ai_agent_data.json"

# ✅ Market Data APIs (API Keys Required)
METALS_API_KEY = "your_metals_api_key"  # 🔹 Replace with your Metals API Key
FMP_API_KEY = "your_fmp_api_key"  # 🔹 Replace with your Financial Modeling Prep API Key

MARKET_APIS = {
    "BTCUSDT": "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
    "ETHUSDT": "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT",
    "GOLD": f"https://metals-api.com/api/latest?base=XAU&apikey={METALS_API_KEY}",
    "S&P500": f"https://financialmodelingprep.com/api/v3/quote/%5EGSPC?apikey={FMP_API_KEY}"
}

# ✅ Logging Function (Bug Fix)
def log_update(update_text):
    """Jarvis अपने Updates को Log करेगा"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{time.ctime()} - {update_text}\n")

# ✅ Load & Save AI Agent Performance Data
def load_agent_data():
    """Load AI Agent Performance Data"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_agent_data(data):
    """Save AI Agent Performance Data Locally"""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    log_update("AI Data Saved Locally")
    print("💾 AI Data Saved Locally!")

# ✅ Fetch Real-Time Market Data for Different Assets
def fetch_market_data(asset):
    """Fetch Real-Time Market Data for Given Asset"""
    try:
        url = MARKET_APIS.get(asset)
        if not url:
            print(f"⚠️ No API available for {asset}")
            return None

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if asset == "BTCUSDT" or asset == "ETHUSDT":
                return float(data["price"])
            elif asset == "GOLD" and "rates" in data:
                return float(data["rates"]["USD"])
            elif asset == "S&P500" and isinstance(data, list):
                return float(data[0]["price"])
        else:
            print(f"⚠️ Failed to Fetch {asset} Market Data!")
            return None
    except Exception as e:
        print(f"❌ Error Fetching {asset} Market Data: {e}")
        return None

# ✅ Smart Decision-Making: Strategy Selection & Optimization
def select_best_strategy():
    """AI Selects Best Trading Strategy Based on Market Conditions"""
    market_data = {asset: fetch_market_data(asset) for asset in MARKET_APIS}
    print(f"📊 Market Data: {market_data}")

    if market_data["BTCUSDT"] and market_data["BTCUSDT"] > 60000 and market_data["GOLD"] and market_data["GOLD"] < 1800:
        print("🔹 AI Selected Crypto Scalping Strategy")
        return "Crypto Scalping"
    elif market_data["S&P500"] and market_data["S&P500"] > 4500:
        print("🔹 AI Selected Stock Trend Following Strategy")
        return "Stock Trend Following"
    else:
        print("🔹 AI Selected Gold Safe-Haven Strategy")
        return "Gold Safe-Haven"

# ✅ Reinforcement Learning: AI Improves its Strategy
def reinforce_learning(agent_name, reward):
    """AI को उसकी Performance के हिसाब से Train करेगा"""
    ai_data = load_agent_data()
    if agent_name not in ai_data:
        ai_data[agent_name] = {"performance": 0, "last_update": time.ctime()}
    
    ai_data[agent_name]["performance"] += reward  # 🔹 Learning Process
    save_agent_data(ai_data)
    log_update(f"📈 {agent_name} Reinforced Learning! New Score: {ai_data[agent_name]['performance']}")
    print(f"📈 {agent_name} Reinforced Learning! New Score: {ai_data[agent_name]['performance']}")

# ✅ Multi-Agent Data Sharing System
def share_data_with_agents(data):
    """AI Agents के बीच Data Share करेगा"""
    print(f"🔄 Sharing Data with AI Agents: {data}")
    log_update("AI Agents Data Shared")

# ✅ AI Execution (Smart Decision-Making + Multi-Asset Trading)
if __name__ == "__main__":
    print("🚀 Jarvis AI: Smart Decision-Making & Multi-Asset Trading Enabled")

    # ✅ AI Selects Best Strategy
    best_strategy = select_best_strategy()

    # ✅ AI Agents की Performance Load करो
    ai_data = load_agent_data()

    # ✅ AI Data Save करो
    save_agent_data(ai_data)

    # ✅ AI Agents Data Share करें
    share_data_with_agents(ai_data)

    # ✅ AI Agents Upgrade करें
    agents = ["market_scanner"]
    for agent in agents:
        reinforce_learning(agent, reward=5)  # Reward System Enabled
