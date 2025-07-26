# secure_alert_bot/main.py

import os
import time
import requests
from datetime import datetime, timedelta

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
PENNY_STOCK_CHANNEL_ID = os.environ['PENNY_STOCK_CHANNEL_ID']
STOCK_CHANNEL_ID = os.environ['STOCK_CHANNEL_ID']
CRYPTO_CHANNEL_ID = os.environ['CRYPTO_CHANNEL_ID']
WATCHLIST_CHANNEL_ID = os.environ['WATCHLIST_CHANNEL_ID']
VALIDATION_CHANNEL_ID = os.environ['VALIDATION_CHANNEL_ID']
WRAPUP_CHANNEL_ID = os.environ['WRAPUP_CHANNEL_ID']

# --- Helper Functions ---
def send_telegram_alert(channel_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": channel_id, "text": message, "parse_mode": "HTML"}
    requests.post(url, data=payload)

# --- Mock Data Fetch (Replace with Real API Calls) ---
def fetch_penny_stocks():
    return [{"ticker": "XYZ", "price": 2.15, "change": 12.5, "volume": 1_500_000}]

def fetch_stocks():
    return [{"ticker": "ABC", "price": 8.75, "change": 5.1, "volume": 2_100_000}]

def fetch_crypto():
    return [{"symbol": "BTCUSDT", "price": 29250, "change": 2.3, "volume": 8500_000}]

# --- Main Loop ---
def run_alerts():
    last_alert_penny = datetime.utcnow() - timedelta(minutes=10)
    last_alert_stock = datetime.utcnow() - timedelta(minutes=10)
    last_alert_crypto = datetime.utcnow() - timedelta(minutes=10)

    while True:
        current_time = datetime.utcnow()

        # Penny Stocks Alerts
        if (current_time - last_alert_penny).total_seconds() >= 600:
            penny_stocks = fetch_penny_stocks()
            for stock in penny_stocks:
                msg = f"<b>Penny Stock Alert</b>\nTicker: {stock['ticker']}\nPrice: ${stock['price']}\nChange: {stock['change']}%\nVolume: {stock['volume']:,}"
                send_telegram_alert(PENNY_STOCK_CHANNEL_ID, msg)
            last_alert_penny = current_time

        # Stocks Alerts
        if (current_time - last_alert_stock).total_seconds() >= 600:
            stocks = fetch_stocks()
            for stock in stocks:
                msg = f"<b>Stock Alert</b>\nTicker: {stock['ticker']}\nPrice: ${stock['price']}\nChange: {stock['change']}%\nVolume: {stock['volume']:,}"
                send_telegram_alert(STOCK_CHANNEL_ID, msg)
            last_alert_stock = current_time

        # Crypto Alerts
        if (current_time - last_alert_crypto).total_seconds() >= 600:
            crypto_coins = fetch_crypto()
            for coin in crypto_coins:
                msg = f"<b>Crypto Alert</b>\nSymbol: {coin['symbol']}\nPrice: ${coin['price']}\nChange: {coin['change']}%\nVolume: {coin['volume']:,}"
                send_telegram_alert(CRYPTO_CHANNEL_ID, msg)
            last_alert_crypto = current_time

        time.sleep(60)  # Main loop sleep (minimal load)

if __name__ == "__main__":
    run_alerts()
