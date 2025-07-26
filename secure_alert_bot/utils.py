from datetime import datetime, time as dtime
import os

def is_peak_hours():
    peak_start = os.getenv('PEAK_START_TIME', '09:15')
    peak_end = os.getenv('PEAK_END_TIME', '11:00')

    peak_start_time = dtime(int(peak_start.split(":")[0]), int(peak_start.split(":")[1]))
    peak_end_time = dtime(int(peak_end.split(":")[0]), int(peak_end.split(":")[1]))

    current_time_utc = datetime.utcnow().time()

    return peak_start_time <= current_time_utc <= peak_end_time

def format_number(num):
    if num >= 1_000_000:
        return f"{num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.2f}K"
    else:
        return str(num)

def build_alert_message(alert_type, data):
    if alert_type == "penny_stock":
        return (f"<b>Penny Stock Alert</b>\n"
                f"Ticker: {data['ticker']}\n"
                f"Price: ${data['price']}\n"
                f"Change: {data['change']}%\n"
                f"Volume: {format_number(data['volume'])}")

    elif alert_type == "stock":
        return (f"<b>Stock Alert</b>\n"
                f"Ticker: {data['ticker']}\n"
                f"Price: ${data['price']}\n"
                f"Change: {data['change']}%\n"
                f"Volume: {format_number(data['volume'])}")

    elif alert_type == "crypto":
        return (f"<b>Crypto Alert</b>\n"
                f"Symbol: {data['symbol']}\n"
                f"Price: ${data['price']}\n"
                f"Change: {data['change']}%\n"
                f"Volume: {format_number(data['volume'])}")

    else:
        return "Invalid Alert Type"

