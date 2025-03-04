import requests
import pandas as pd

# ✅ SEC API (For Insider Trading Data)
SEC_API_URL = "https://www.sec.gov/files/company_tickers.json"
INSIDER_TRADING_URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=4&dateb=&owner=include&count=10"

# ✅ Fetch Insider Trading Data with Error Handling
def get_insider_trading_data():
    headers = {"User-Agent": "Jarvis AI Insider Tracker"}
    
    try:
        response = requests.get(SEC_API_URL, headers=headers)
        if response.status_code != 200:
            print("⚠️ SEC API Error: Unable to fetch data!")
            return []

        json_data = response.json()
        company_data = pd.DataFrame.from_dict(json_data, orient="index")

        if company_data.empty:
            print("⚠️ No Insider Trading Data Found!")
            return []

        # Example: Top 5 Companies Insider Trading Data
        insider_trades = []
        for cik in company_data["cik_str"][:5]:  # Check first 5 companies
            url = INSIDER_TRADING_URL.format(cik=cik)
            trade_data = requests.get(url, headers=headers).text
            insider_trades.append({"CIK": cik, "Trade Data": trade_data[:500]})  # Store first 500 chars of data

        return insider_trades

    except Exception as e:
        print(f"❌ Error fetching SEC Data: {e}")
        return []

# ✅ Run Insider Trading Detection
def run_insider_trading_detector():
    print("\n🚀 Fetching Insider Trading Data...")
    insider_data = get_insider_trading_data()
    
    if not insider_data:
        print("⚠️ No insider trading activity detected.")
        return

    for data in insider_data:
        print(f"📊 Insider Trading for CIK {data['CIK']}: {data['Trade Data']}")

# ✅ Execute the Detector
run_insider_trading_detector()
