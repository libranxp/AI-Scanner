import os

class Config:
    TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
    TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    PENNY_STOCK_CHANNEL_ID = os.environ['PENNY_STOCK_CHANNEL_ID']
    STOCK_CHANNEL_ID = os.environ['STOCK_CHANNEL_ID']
    CRYPTO_CHANNEL_ID = os.environ['CRYPTO_CHANNEL_ID']
    WATCHLIST_CHANNEL_ID = os.environ['WATCHLIST_CHANNEL_ID']
    VALIDATION_CHANNEL_ID = os.environ['VALIDATION_CHANNEL_ID']
    WRAPUP_CHANNEL_ID = os.environ['WRAPUP_CHANNEL_ID']

    # Removed LunarCrush API Key
    # Added CoinGecko API URL (optional)
    COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

