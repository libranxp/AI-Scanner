import time
from datetime import datetime, time as dtime
from secure_alert_bot.config import Config
from secure_alert_bot.fetch_data import fetch_penny_stocks, fetch_stocks, fetch_crypto
from secure_alert_bot.main import send_telegram_alert

def is_peak_hours(current_time):
    """Check if current UTC time is within peak trading hours."""
    start = Config.PEAK_START_TIME
    end = Config.PEAK_END_TIME
    return start <= current_time.time() <= end

def run_scheduler():
    last_alert_penny = datetime.utcnow() - timedelta(seconds=Config.ALERT_INTERVAL_PENNY_OFF)
    last_alert_stock = datetime.utcnow() - timedelta(seconds=Config.ALERT_INTERVAL_PENNY_OFF)
    last_alert_crypto = datetime.utcnow() - timedelta(seconds=Config.ALERT_INTERVAL_CRYPTO)

    while True:
        now = datetime.utcnow()

        # Penny Stocks Alerts - alert intervals change based on peak hours
        penny_alert_interval = (Config.ALERT_INTERVAL_PENNY_PEAK if is_peak_hours(now) 
                               else Config.ALERT_INTERVAL_PENNY_OFF)
        if (now - last_alert_penny).total_seconds() >= penny_alert_interval:
            penny_stocks = fetch_penny_stocks()
            for stock in penny_stocks:
                msg = (f"<b>Penny Stock Alert</b>\nTicker: {stock['ticker']}\n"
                       f"Price: ${stock['price']}\nChange: {stock['change']}%\nVolume: {stock['volume']:,}")
                send_telegram_alert(Config.PENNY_STOCK_CHANNEL_ID, msg)
            last_alert_penny = now

        # Stocks Alerts (every ALERT_INTERVAL_PENNY_OFF seconds)
        if (now - last_alert_stock).total_seconds() >= Config.ALERT_INTERVAL_PENNY_OFF:
            stocks = fetch_stocks()
            for stock in stocks:
                msg = (f"<b>Stock Alert</b>\nTicker: {stock['ticker']}\n"
                       f"Price: ${stock['price']}\nChange: {stock['change']}%\nVolume: {stock['volume']:,}")
                send_telegram_alert(Config.STOCK_CHANNEL_ID, msg)
            last_alert_stock = now

        # Crypto Alerts (every ALERT_INTERVAL_CRYPTO seconds)
        if (now - last_alert_crypto).total_seconds() >= Config.ALERT_INTERVAL_CRYPTO:
            cryptos = fetch_crypto()
            for coin in cryptos:
                msg = (f"<b>Crypto Alert</b>\nSymbol: {coin['symbol']}\n"
                       f"Price: ${coin['price']}\nChange: {coin['change']}%\nVolume: {coin['volume']:,}")
                send_telegram_alert(Config.CRYPTO_CHANNEL_ID, msg)
            last_alert_crypto = now

        # Sleep for 60 seconds before checking again
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()
