# secure_alert_bot/message_formatter.py

from datetime import datetime

def format_penny_stock_alert(stock):
    return (
        f"<b>📈 Penny Stock Alert</b>\n"
        f"Ticker: <code>{stock['ticker']}</code>\n"
        f"Price: ${stock['price']:.2f}\n"
        f"Change: {stock['change']:.2f}%\n"
        f"Volume: {stock['volume']:,}"
    )

def format_stock_alert(stock):
    return (
        f"<b>📊 Stock Alert</b>\n"
        f"Ticker: <code>{stock['ticker']}</code>\n"
        f"Price: ${stock['price']:.2f}\n"
        f"Change: {stock['change']:.2f}%\n"
        f"Volume: {stock['volume']:,}"
    )

def format_crypto_alert(coin):
    return (
        f"<b>💰 Crypto Alert</b>\n"
        f"Symbol: <code>{coin['symbol']}</code>\n"
        f"Price: ${coin['price']:.4f}\n"
        f"Change: {coin['change']:.2f}%\n"
        f"Volume: {coin['volume']:,}"
    )

def format_watchlist_entry(entry):
    return (
        f"<b>🔍 Watchlist Entry</b>\n"
        f"Ticker: <code>{entry['ticker']}</code>\n"
        f"Sector: {entry['sector']}\n"
        f"RSI: {entry['rsi']:.2f}\n"
        f"VWAP: ${entry['vwap']:.2f}"
    )

def format_validation_entry(entry):
    status = "🔄 Confirmed" if entry['valid'] else "❌ Failed"
    return (
        f"<b>📆 Validation</b>\n"
        f"Ticker: <code>{entry['ticker']}</code>\n"
        f"Status: {status}"
    )

def format_wrapup_summary(stats):
    time_str = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    return (
        f"<b>📅 Daily Wrap-up Summary</b>\n"
        f"Date: {time_str}\n"
        f"Total Penny Alerts: {stats['penny']}\n"
        f"Total Stock Alerts: {stats['stocks']}\n"
        f"Total Crypto Alerts: {stats['crypto']}\n"
        f"Validated Setups: {stats['validated']}\n"
        f"Failed Validations: {stats['failed']}"
    )
