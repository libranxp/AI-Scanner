import os
from datetime import time

def parse_time(t_str):
    """Parse HH:MM string to datetime.time"""
    try:
        h, m = map(int, t_str.split(":"))
        return time(hour=h, minute=m)
    except Exception:
        return None

class Config:
    # Telegram & Channel IDs
    TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
    TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    PENNY_STOCK_CHANNEL_ID = os.environ['PENNY_STOCK_CHANNEL_ID']
    STOCK_CHANNEL_ID = os.environ['STOCK_CHANNEL_ID']
    CRYPTO_CHANNEL_ID = os.environ['CRYPTO_CHANNEL_ID']
    WATCHLIST_CHANNEL_ID = os.environ['WATCHLIST_CHANNEL_ID']
    VALIDATION_CHANNEL_ID = os.environ['VALIDATION_CHANNEL_ID']
    WRAPUP_CHANNEL_ID = os.environ['WRAPUP_CHANNEL_ID']

    # API Keys
    LUNARCRUSH_API_KEY = os.environ['LUNARCRUSH_API_KEY']
    FMP_API_KEY = os.environ['FMP_API_KEY']
    FINNHUB_API_KEY = os.environ['FINNHUB_API_KEY']
    COINMARKETCAL_API_KEY = os.environ['COINMARKETCAL_API_KEY']
    ALPHAVANTAGE_API_KEY = os.environ['ALPHAVANTAGE_API_KEY']

    # Trading Time Windows (UTC)
    PEAK_START_TIME = parse_time(os.getenv('PEAK_START_TIME', '12:30'))
    PEAK_END_TIME = parse_time(os.getenv('PEAK_END_TIME', '15:30'))

    # Scan intervals (seconds)
    SCAN_INTERVAL_PENNY = int(os.getenv('SCAN_INTERVAL_PENNY', 600))
    SCAN_INTERVAL_STOCK = int(os.getenv('SCAN_INTERVAL_STOCK', 600))
    SCAN_INTERVAL_CRYPTO = int(os.getenv('SCAN_INTERVAL_CRYPTO', 600))

    # Alert intervals (seconds)
    ALERT_INTERVAL_PENNY_PEAK = int(os.getenv('ALERT_INTERVAL_PENNY_PEAK', 300))
    ALERT_INTERVAL_PENNY_OFF = int(os.getenv('ALERT_INTERVAL_PENNY_OFF', 600))
    ALERT_INTERVAL_CRYPTO = int(os.getenv('ALERT_INTERVAL_CRYPTO', 600))
