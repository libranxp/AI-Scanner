# config.py
import os

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # Telegram Channel IDs
    STOCK_CHANNEL_ID = os.getenv("STOCK_CHANNEL_ID")
    PENNY_STOCK_CHANNEL_ID = os.getenv("PENNY_STOCK_CHANNEL_ID")
    CRYPTO_CHANNEL_ID = os.getenv("CRYPTO_CHANNEL_ID")
    WATCHLIST_CHANNEL_ID = os.getenv("WATCHLIST_CHANNEL_ID")
    VALIDATION_CHANNEL_ID = os.getenv("VALIDATION_CHANNEL_ID")
    WRAPUP_CHANNEL_ID = os.getenv("WRAPUP_CHANNEL_ID")

    # API Keys
    FMP_API_KEY = os.getenv("FMP_API_KEY")
    FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
    COINMARKETCAL_API_KEY = os.getenv("COINMARKETCAL_API_KEY")
    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

    # Scan Intervals (in seconds)
    SCAN_INTERVALS = {
        "stock": int(os.getenv("SCAN_INTERVAL_STOCK", 600)),
        "penny": int(os.getenv("SCAN_INTERVAL_PENNY", 600)),
        "crypto": int(os.getenv("SCAN_INTERVAL_CRYPTO", 600))
    }

    # Alert Intervals (in seconds)
    ALERT_INTERVALS = {
        "penny_peak": int(os.getenv("ALERT_INTERVAL_PENNY_PEAK", 300)),
        "penny_off": int(os.getenv("ALERT_INTERVAL_PENNY_OFF", 600)),
        "crypto": int(os.getenv("ALERT_INTERVAL_CRYPTO", 600))
    }

    # Peak Trading Hours (24-hour format, UTC)
    PEAK_START_TIME = os.getenv("PEAK_START_TIME", "12:30")  # Default: 12:30 UTC
    PEAK_END_TIME = os.getenv("PEAK_END_TIME", "15:30")      # Default: 15:30 UTC

    # External API URLs
    COINGECKO_API_URL = os.getenv("COINGECKO_API_URL", "https://api.coingecko.com/api/v3")

    @classmethod
    def validate(cls):
        required_vars = [
            cls.TELEGRAM_BOT_TOKEN,
            cls.FMP_API_KEY
        ]

        missing = [var for var in required_vars if not var]
        if missing:
            raise EnvironmentError(f"Missing required configuration variables: {missing}")

# Usage:
# Config.validate()  # Ensure critical env vars are set before running the bot.
