import os
import time
import json
import requests

# 🔹 Jarvis AI Evolution V6.2 (Crypto-Only Trading Mode)
CODE_FOLDER = "C:\\Users\\home\\Jarvis-AI\\"
LOG_FILE = CODE_FOLDER + "jarvis_agent_log.txt"
DATA_FILE = CODE_FOLDER + "ai_agent_data.json"

# ✅ Only Crypto Market Data APIs (GOLD & S&P500 Removed)
MARKET_APIS = {
    "BTCUSDT": "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
    "ETHUSDT": "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
}

# ✅ Logging Function
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

# ✅ Fetch Real-Time Crypto Market Data
def fetch_market_data():
    """Fetch BTC & ETH Live Prices"""
    market_data = {}
    for asset, url in MARKET_APIS.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                market_data[asset] = float(data["price"])
            else:
                print(f"⚠️ Failed to Fetch {asset} Market Data!")
        except Exception as e:
            print(f"❌ Error Fetching {asset} Market Data: {e}")
    return market_data

# ✅ Smart Decision-Making: Crypto-Based Strategy Selection
def select_best_strategy():
    """AI Selects Best Crypto Trading Strategy"""
    market_data = fetch_market_data()
    print(f"📊 Market Data: {market_data}")

    if market_data.get("BTCUSDT", 0) > 60000 and market_data.get("ETHUSDT", 0) > 2000:
        print("🔹 AI Selected Crypto Scalping Strategy")
        return "Crypto Scalping"
    else:
        print("🔹 AI Selected BTC Swing Trading Strategy")
        return "BTC Swing Trading"

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

# ✅ AI Execution (Crypto-Based Trading Mode)
if __name__ == "__main__":
    print("🚀 Jarvis AI: Crypto-Only Trading Mode Enabled")

    # ✅ AI Selects Best Strategy
    best_strategy = select_best_strategy()

    # ✅ AI Agents की Performance Load करो
    ai_data = load_agent_data()

    # ✅ AI Data Save करो
    save_agent_data(ai_data)

    # ✅ AI Agents Data Share करें
    share_data_with_agents(ai_data)

    # ✅ AI Reinforcement Learning System
    reinforce_learning("market_scanner", reward=5)
