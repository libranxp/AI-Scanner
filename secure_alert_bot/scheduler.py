import os
import time
import requests
from datetime import datetime, timedelta
from logger import get_logger
from secure_alert_bot.utils import build_alert_message

# Environment Variables
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
PENNY_STOCK_CHANNEL_ID = os.environ['PENNY_STOCK_CHANNEL_ID']
STOCK_CHANNEL_ID = os.environ['STOCK_CHANNEL_ID']
CRYPTO_CHANNEL_ID = os.environ['CRYPTO_CHANNEL_ID']
FMP_API_KEY = os.environ['FMP_API_KEY']

logger = get_logger("scheduler", log_file="logs/scheduler.log")

# --- Helper Function ---
def send_telegram_alert(channel_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": channel_id, "text": message, "parse_mode": "HTML"}
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            logger.error(f"Failed to send alert to {channel_id}: {response.text}")
    except Exception as e:
        logger.exception(f"Exception occurred while sending alert to {channel_id}")

# --- Fetch Functions ---
def fetch_penny_stocks():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        penny_stocks = [stock for stock in data if stock.get('price', 0) < 5]
        return penny_stocks[:3]
    except Exception as e:
        logger.exception("Failed to fetch penny stocks")
        return []

def fetch_stocks():
    url = f"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        stocks = [stock for stock in data if stock.get('price', 0) >= 5]
        return stocks[:3]
    except Exception as e:
        logger.exception("Failed to fetch stocks")
        return []

def fetch_crypto():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.exception("Failed to fetch crypto data")
        return {}

# --- Main Scheduler ---
def run_scheduler():
    logger.info("Scheduler started.")
    last_alert_time = datetime.utcnow() - timedelta(minutes=10)

    while True:
        current_time = datetime.utcnow()

        if (current_time - last_alert_time).total_seconds() >= 600:
            # Penny Stock Alerts
            penny_stocks = fetch_penny_stocks()
            for stock in penny_stocks:
                msg = build_alert_message("penny_stock", {
                    'ticker': stock.get('symbol', 'N/A'),
                    'price': stock.get('price', 'N/A'),
                    'change': stock.get('changesPercentage', 'N/A'),
                    'volume': stock.get('volume', 0)
                })
                send_telegram_alert(PENNY_STOCK_CHANNEL_ID, msg)

            # Stock Alerts
            stocks = fetch_stocks()
            for stock in stocks:
                msg = build_alert_message("stock", {
                    'ticker': stock.get('symbol', 'N/A'),
                    'price': stock.get('price', 'N/A'),
                    'change': stock.get('changesPercentage', 'N/A'),
                    'volume': stock.get('volume', 0)
                })
                send_telegram_alert(STOCK_CHANNEL_ID, msg)

            # Crypto Alerts
            crypto_data = fetch_crypto()
            for coin, data in crypto_data.items():
                msg = build_alert_message("crypto", {
                    'symbol': coin,
                    'price': data.get('usd', 'N/A'),
                    'change': round(data.get('usd_24h_change', 0), 2),
                    'volume': 0  # Crypto volume not available in current API
                })
                send_telegram_alert(CRYPTO_CHANNEL_ID, msg)

            last_alert_time = current_time
            logger.info("Alerts sent successfully.")

        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()
