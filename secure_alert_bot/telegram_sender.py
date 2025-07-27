import os
import requests
import re

# Fetch Telegram credentials and channel IDs from environment variables
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

CHANNELS = {
    'penny': os.getenv('TELEGRAM_CHANNEL_PENNY'),
    'stock': os.getenv('TELEGRAM_CHANNEL_STOCK'),
    'crypto': os.getenv('TELEGRAM_CHANNEL_CRYPTO'),
    'watchlist': os.getenv('TELEGRAM_CHANNEL_WATCHLIST'),
    'validation': os.getenv('TELEGRAM_CHANNEL_VALIDATION'),
    'wrapup': os.getenv('TELEGRAM_CHANNEL_WRAPUP'),
}

if not BOT_TOKEN or any(v is None for v in CHANNELS.values()):
    raise EnvironmentError("Telegram BOT_TOKEN or some CHANNEL IDs are missing in environment variables")


def escape_markdown(text):
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', str(text))


def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'MarkdownV2',
        'disable_web_page_preview': False,
    }
    r = requests.post(url, data=payload)
    if not r.ok:
        print(f"Telegram API Error: {r.status_code} {r.text}")
    return r.json()


# Layout formatters (format_penny_alert, format_stock_alert, format_crypto_alert, format_watchlist, format_validation, format_wrapup)
# ... (Your existing formatting functions go here)

# Main alert function
def send_alert(alert_type, data):
    formatter_map = {
        'penny': format_penny_alert,
        'stock': format_stock_alert,
        'crypto': format_crypto_alert,
        'watchlist': format_watchlist,
        'validation': format_validation,
        'wrapup': format_wrapup,
    }

    if alert_type not in formatter_map:
        raise ValueError(f"Unsupported alert type: {alert_type}")

    formatter = formatter_map[alert_type]
    chat_id = CHANNELS[alert_type]
    message_text = formatter(data)

    return send_telegram_message(chat_id, message_text)

# Example Usage:
# data = {...}  # your data dict here
# send_alert('penny', data)
