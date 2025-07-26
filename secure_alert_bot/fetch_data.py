import os
import requests

# Load API Keys from Environment Variables
LUNARCRUSH_API_KEY = os.environ['LUNARCRUSH_API_KEY']
FMP_API_KEY = os.environ['FMP_API_KEY']
FINNHUB_API_KEY = os.environ['FINNHUB_API_KEY']
COINMARKETCAL_API_KEY = os.environ['COINMARKETCAL_API_KEY']
ALPHAVANTAGE_API_KEY = os.environ['ALPHAVANTAGE_API_KEY']

# --- API Endpoints ---
LUNARCRUSH_URL = "https://api.lunarcrush.com/v2"
FMP_URL = "https://financialmodelingprep.com/api/v3"
FINNHUB_URL = "https://finnhub.io/api/v1"
COINMARKETCAL_URL = "https://developers.coinmarketcal.com/v1"
ALPHAVANTAGE_URL = "https://www.alphavantage.co/query"

# --- Fetch Penny Stocks Data ---
def fetch_penny_stocks():
    url = f"{FMP_URL}/stock_market/actives?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        penny_stocks = [stock for stock in data if 0.5 <= stock['price'] <= 5.0 and stock['changesPercentage'] >= 5.0]
        return penny_stocks
    return []

# --- Fetch Regular Stocks Data ---
def fetch_stocks():
    url = f"{FMP_URL}/stock_market/actives?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stocks = [stock for stock in data if 5.0 < stock['price'] <= 15.0 and stock['changesPercentage'] >= 2.0]
        return stocks
    return []

# --- Fetch Crypto Data ---
def fetch_crypto():
    url = f"{LUNARCRUSH_URL}/assets?data=market&apikey={LUNARCRUSH_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data', [])
        crypto = [coin for coin in data if 0.01 <= coin['price'] <= 15.0 and coin['percent_change_24h'] >= 2.0]
        return crypto
    return []

# --- Fetch Crypto Events ---
def fetch_crypto_events():
    url = f"{COINMARKETCAL_URL}/events"
    headers = {'x-api-key': COINMARKETCAL_API_KEY}
    params = {'page': 1, 'max': 5}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('body', [])
    return []

# --- Fetch Market News ---
def fetch_market_news():
    url = f"{FINNHUB_URL}/news?category=general&token={FINNHUB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

# --- Fetch Technical Indicators (Example: RSI) ---
def fetch_rsi(symbol):
    url = f"{ALPHAVANTAGE_URL}?function=RSI&symbol={symbol}&interval=15min&time_period=14&series_type=close&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rsi_data = data.get('Technical Analysis: RSI', {})
        if rsi_data:
            latest_time = list(rsi_data.keys())[0]
            return float(rsi_data[latest_time]['RSI'])
    return None

# --- Testing Execution ---
if __name__ == "__main__":
    print("Penny Stocks:", fetch_penny_stocks())
    print("Stocks:", fetch_stocks())
    print("Crypto:", fetch_crypto())
    print("Crypto Events:", fetch_crypto_events())
    print("Market News:", fetch_market_news())
    print("RSI Example (AAPL):", fetch_rsi("AAPL"))
