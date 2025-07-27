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
    try:
        num = float(num)
        if num >= 1_000_000:
            return f"{num / 1_000_000:.2f}M"
        elif num >= 1_000:
            return f"{num / 1_000:.2f}K"
        else:
            return str(num)
    except (ValueError, TypeError):
        return str(num)


def build_alert_message(alert_type, data):
    try:
        if alert_type == "penny_stock":
            return (f"<b>Penny Stock Alert</b>\n"
                    f"Ticker: {data.get('ticker', 'N/A')}\n"
                    f"Price: ${data.get('price', 'N/A')}\n"
                    f"Change: {data.get('change', 'N/A')}%\n"
                    f"Volume: {format_number(data.get('volume', 0))}")

        elif alert_type == "stock":
            return (f"<b>Stock Alert</b>\n"
                    f"Ticker: {data.get('ticker', 'N/A')}\n"
                    f"Price: ${data.get('price', 'N/A')}\n"
                    f"Change: {data.get('change', 'N/A')}%\n"
                    f"Volume: {format_number(data.get('volume', 0))}")

        elif alert_type == "crypto":
            return (f"<b>Crypto Alert</b>\n"
                    f"Symbol: {data.get('symbol', 'N/A')}\n"
                    f"Price: ${data.get('price', 'N/A')}\n"
                    f"Change: {data.get('change', 'N/A')}%\n"
                    f"Volume: {format_number(data.get('volume', 0))}")

        else:
            return "Invalid Alert Type"

    except Exception as e:
        return f"Error building alert message: {e}"

