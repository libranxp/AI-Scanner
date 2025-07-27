import os
import time
import requests
from datetime import datetime, timedelta

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
PENNY_STOCK_CHANNEL_ID = os.environ['PENNY_STOCK_CHANNEL_ID']
STOCK_CHANNEL_ID = os.environ['STOCK_CHANNEL_ID']
CRYPTO_CHANNEL_ID = os.environ['CRYPTO_CHANNEL_ID']
FMP_API_KEY = os.environ['FMP_API_KEY']

# --- Helper Function ---
def send_telegram_alert(channel_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": channel_id, "text": message, "parse_mode": "HTML"}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Failed to send alert: {response.text}")

# --- Fetch Functions ---
def fetch_penny_stocks():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()
    penny_stocks = [stock for stock in data if stock.get('price', 0) < 5]
    return penny_stocks[:3]  # Limit to top 3

def fetch_stocks():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()
    stocks = [stock for stock in data if stock.get('price', 0) >= 5]
    return stocks[:3]  # Limit to top 3

def fetch_crypto():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url)
    if response.status_code != 200:
        return {}

    return response.json()

# --- Main Scheduler ---
def run_scheduler():
    last_alert_time = datetime.utcnow() - timedelta(minutes=10)

    while True:
        current_time = datetime.utcnow()

        if (current_time - last_alert_time).total_seconds() >= 600:
            # Penny Stock Alerts
            penny_stocks = fetch_penny_stocks()
            for stock in penny_stocks:
                msg = (
                    f"<b>Penny Stock Alert 🚀</b>\n"
                    f"Ticker: {stock['symbol']}\n"
                    f"Price: ${stock['price']}\n"
                    f"Change: {stock['changesPercentage']}\n"
                    f"Volume: {stock.get('volume', 'N/A')}"
                )
                send_telegram_alert(PENNY_STOCK_CHANNEL_ID, msg)

            # Stock Alerts
            stocks = fetch_stocks()
            for stock in stocks:
                msg = (
                    f"<b>Stock Alert 📈</b>\n"
                    f"Ticker: {stock['symbol']}\n"
                    f"Price: ${stock['price']}\n"
                    f"Change: {stock['changesPercentage']}\n"
                    f"Volume: {stock.get('volume', 'N/A')}"
                )
                send_telegram_alert(STOCK_CHANNEL_ID, msg)

            # Crypto Alerts
            crypto_data = fetch_crypto()
            for coin, data in crypto_data.items():
                msg = (
                    f"<b>Crypto Alert 🪙</b>\n"
                    f"Coin: {coin.title()}\n"
                    f"Price: ${data['usd']}\n"
                    f"24h Change: {round(data['usd_24h_change'], 2)}%"
                )
                send_telegram_alert(CRYPTO_CHANNEL_ID, msg)

            last_alert_time = current_time

        time.sleep(60)  # Sleep 1 min to avoid spamming API
