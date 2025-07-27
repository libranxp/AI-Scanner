import requests
from .config import FMP_API_KEY, ALPHAVANTAGE_API_KEY
from .logger import logger

FMP_URL = "https://financialmodelingprep.com/api/v3/stock-screener"
ALPHA_URL = "https://www.alphavantage.co/query"

def fetch_from_fmp():
    params = {
        'priceLowerThan': 15,
        'volumeMoreThan': 500000,
        'betaMoreThan': 0,
        'limit': 20,
        'apikey': FMP_API_KEY
    }
    response = requests.get(FMP_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"FMP API Error: {response.status_code}")
        return None

def fetch_from_alpha():
    params = {
        'function': 'TOP_GAINERS_LOSERS',  # Hypothetical function
        'apikey': ALPHAVANTAGE_API_KEY
    }
    response = requests.get(ALPHA_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"AlphaVantage API Error: {response.status_code}")
        return None

def fetch_data():
    data = fetch_from_fmp()
    if not data:
        data = fetch_from_alpha()
    return data

