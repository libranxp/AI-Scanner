import os
import requests
import re

# Fetch Telegram credentials and channel IDs from environment variables
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

CHANNELS = {
    'penny': os.getenv('TELEGRAM_CHANNEL_PENNY'),        # e.g. "-1001234567890"
    'stock': os.getenv('TELEGRAM_CHANNEL_STOCK'),
    'crypto': os.getenv('TELEGRAM_CHANNEL_CRYPTO'),
    'watchlist': os.getenv('TELEGRAM_CHANNEL_WATCHLIST'),
    'validation': os.getenv('TELEGRAM_CHANNEL_VALIDATION'),
    'wrapup': os.getenv('TELEGRAM_CHANNEL_WRAPUP'),
}

if not BOT_TOKEN or any(v is None for v in CHANNELS.values()):
    raise EnvironmentError("Telegram BOT_TOKEN or some CHANNEL IDs are missing in environment variables")


def escape_markdown(text):
    """
    Escape text for Telegram MarkdownV2 parse_mode
    """
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


# Layout formatters

def format_penny_alert(data):
    text = (
        "🚨 *Penny Stock Alert — High Conviction Setup*\n\n"
        f"*Symbol:* ${escape_markdown(data['symbol'])}\n"
        f"*Strategy:* {escape_markdown(data['strategy'])}\n"
        f"*Entry:* ${escape_markdown(data['entry'])} | *TP:* ${escape_markdown(data['tp'])} | *SL:* ${escape_markdown(data['sl'])}\n"
        f"*Confidence Score:* {escape_markdown(data['confidence_emoji'])} {escape_markdown(data['confidence_percent'])}% ({escape_markdown(data['confidence_text'])})\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment Score:* {escape_markdown(data['sentiment_score'])} ({escape_markdown(data['sentiment_text'])})\n\n"
        f"📊 *Float:* {escape_markdown(data['float'])}M | *Volume Surge:* +{escape_markdown(data['volume_surge'])}% | *RSI:* {escape_markdown(data['rsi'])} | *ATR:* {escape_markdown(data['atr'])}\n"
        f"🔗 [TradingView Chart]({escape_markdown(data['tv_chart'])})\n"
        f"🔗 [Buy on Trading212]({escape_markdown(data['buy_link'])})\n"
        f"🔗 [Order Book]({escape_markdown(data['order_book'])})\n"
        f"🔗 [Catalyst News]({escape_markdown(data['catalyst_news'])})\n\n"
        f"⚠️ *Notes:* {escape_markdown(data['notes'])}"
    )
    return text


def format_stock_alert(data):
    text = (
        "🚨 *Stock Alert — Swing Setup*\n\n"
        f"*Symbol:* ${escape_markdown(data['symbol'])}\n"
        f"*Strategy:* {escape_markdown(data['strategy'])}\n"
        f"*Entry:* ${escape_markdown(data['entry'])} | *TP:* ${escape_markdown(data['tp'])} | *SL:* ${escape_markdown(data['sl'])}\n"
        f"*Confidence Score:* {escape_markdown(data['confidence_emoji'])} {escape_markdown(data['confidence_percent'])}% ({escape_markdown(data['confidence_text'])})\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment Score:* {escape_markdown(data['sentiment_score'])} ({escape_markdown(data['sentiment_text'])})\n\n"
        f"📊 *Float:* {escape_markdown(data['float'])}M | *Rel Vol:* {escape_markdown(data['rel_vol'])} | *RSI:* {escape_markdown(data['rsi'])} | *ATR:* {escape_markdown(data['atr'])}\n"
        f"🔗 [TradingView Chart]({escape_markdown(data['tv_chart'])})\n"
        f"🔗 [Buy on Trading212]({escape_markdown(data['buy_link'])})\n"
        f"🔗 [Order Book]({escape_markdown(data['order_book'])})\n"
        f"🔗 [Catalyst News]({escape_markdown(data['catalyst_news'])})\n\n"
        f"📝 *Analyst Note:* {escape_markdown(data['analyst_note'])}"
    )
    return text


def format_crypto_alert(data):
    text = (
        "🚨 *Crypto Alert — Momentum Breakout*\n\n"
        f"*Asset:* ${escape_markdown(data['asset'])}\n"
        f"*Strategy:* {escape_markdown(data['strategy'])}\n"
        f"*Entry:* ${escape_markdown(data['entry'])} | *TP:* ${escape_markdown(data['tp'])} | *SL:* ${escape_markdown(data['sl'])}\n"
        f"*Confidence Score:* {escape_markdown(data['confidence_emoji'])} {escape_markdown(data['confidence_percent'])}% ({escape_markdown(data['confidence_text'])})\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment Score:* {escape_markdown(data['sentiment_score'])} ({escape_markdown(data['sentiment_text'])})\n\n"
        f"📊 *Volume Spike:* +{escape_markdown(data['volume_spike'])}% | *RSI:* {escape_markdown(data['rsi'])} | *Order Flow:* {escape_markdown(data['order_flow'])}\n"
        f"🔗 [TradingView Chart]({escape_markdown(data['tv_chart'])})\n"
        f"🔗 [Trade on Kraken]({escape_markdown(data['trade_link'])})\n"
        f"🔗 [Order Book]({escape_markdown(data['order_book'])})\n"
        f"🔗 [Catalyst News]({escape_markdown(data['catalyst_news'])})\n\n"
        f"📢 *Alert:* {escape_markdown(data['alerts'])}"
    )
    return text


def format_watchlist(data):
    # data['watchlist'] is a list of dicts
    header = (
        "📋 *Emerald Watchlist (Live Monitor)*\n\n"
        "*Symbol* | *Strategy* | *Entry* | *TP* | *SL* | *Confidence* | *Catalyst*\n"
        "--------|------------|---------|------|------|-------------|-----------------\n"
    )
    rows = ""
    for w in data['watchlist']:
        rows += (
            f"{escape_markdown(w['symbol'])} | "
            f"{escape_markdown(w['strategy'])} | "
            f"${escape_markdown(w['entry'])} | "
            f"${escape_markdown(w['tp'])} | "
            f"${escape_markdown(w['sl'])} | "
            f"{escape_markdown(str(w['confidence']))}% | "
            f"{escape_markdown(w['catalyst'])}\n"
        )
    links = "\n".join(
        f"🔗 [{escape_markdown(w['symbol'])} Chart]({escape_markdown(w['tv_chart'])}) | [Buy {escape_markdown(w['symbol'])}]({escape_markdown(w['buy_link'])})"
        for w in data['watchlist']
    )
    return header + rows + "\n" + links


def format_validation(data):
    text = (
        f"🔍 *AI Reasoning — Why is ${escape_markdown(data['symbol'])} Trending?*\n\n"
        f"✅ Float & Volume Surge: {escape_markdown(data['float'])}M float with +{escape_markdown(data['volume_surge'])}% volume spike, indicating breakout potential.\n"
        f"✅ Catalyst: {escape_markdown(data['catalyst'])} is a strong driver.\n"
        f"✅ Sentiment: {escape_markdown(data['sentiment_score'])} — indicates {escape_markdown(data['sentiment_text'])} chatter across Reddit & StockTwits.\n"
        f"✅ Technicals: {escape_markdown(data['technicals'])}\n\n"
        f"⚠️ Caution: {escape_markdown(data['caution'])}\n\n"
        f"📊 AI Verdict: {escape_markdown(data['verdict'])}"
    )
    return text


def format_wrapup(data):
    pre = data['pre_market']
    post = data['post_market']
    weekend = data['weekend']

    top_movers_lines = "\n".join(
        f"- ${escape_markdown(item['symbol'])} | {escape_markdown(item['gap'])} Gap | {escape_markdown(item['catalyst'])} | Strong Sentiment ({escape_markdown(item['sentiment'])})"
        for item in pre['top_movers']
    )
    watchlist_focus_lines = "\n".join(
        f"{escape_markdown(item['confidence_emoji'])} ${escape_markdown(item['symbol'])} | Entry: ${escape_markdown(item['entry'])} | TP: ${escape_markdown(item['tp'])} | SL: ${escape_markdown(item['sl'])} | Confidence: {escape_markdown(str(item['confidence_percent']))}%"
        for item in pre['watchlist_focus']
    )
    post_recap_lines = "\n".join(
        f"- {escape_markdown(item['symbol'])} closed {escape_markdown(item['change'])} at ${escape_markdown(item['close'])} — {escape_markdown(item['notes'])}"
        for item in post['recap']
    )
    post_observations_lines = "\n".join(
        f"- {escape_markdown(note)}" for note in post['observations']
    )
    weekend_lines = "\n".join(
        f"- {escape_markdown(note)}" for note in weekend['plans']
    )

    text = (
        "*Emerald Recap & Wrapup*\n\n"
        "*Pre-market Highlights:*\n"
        f"{top_movers_lines}\n\n"
        "*Watchlist Focus:*\n"
        f"{watchlist_focus_lines}\n\n"
        "*Post-market Recap:*\n"
        f"{post_recap_lines}\n\n"
        "*Observations & Notes:*\n"
        f"{post_observations_lines}\n\n"
        "*Weekend Plans:*\n"
        f"{weekend_lines}"
    )
    return text


# Main alert function

def send_alert(alert_type, data):
    """
    alert_type: one of 'penny', 'stock', 'crypto', 'watchlist', 'validation', 'wrapup'
    data: dict with keys relevant to each alert type
    """
    formatter_map = {
        'penny': format_penny_alert,
        'stock': format_stock_alert,
        'crypto': format_crypto_alert,
        'watchlist': format_watchlist,
        'validation': format_validation,
        'wrapup': format_wrapup,
    }
    channel_id = CHANNELS.get(alert_type)
    if not channel_id:
        raise ValueError(f"No Telegram channel set for alert type: {alert_type}")

    formatter = formatter_map.get(alert_type)
    if not formatter:
        raise ValueError(f"No formatter for alert type: {alert_type}")

    message = formatter(data)
    return send_telegram_message(channel_id, message)


# Example usage

if __name__ == "__main__":
    # Example: Penny alert data dictionary
    penny_data = {
        'symbol': 'XYZ',
        'strategy': 'Breakout Scalping',
        'entry': '1.23',
        'tp': '1.50',
        'sl': '1.10',
        'confidence_emoji': '🔥',
        'confidence_percent': '85',
        'confidence_text': 'Strong',
        'catalyst': 'FDA Approval',
        'sentiment_score': '+70',
        'sentiment_text': 'Bullish',
        'float': '10',
        'volume_surge': '150',
        'rsi': '72',
        'atr': '0.05',
        'tv_chart': 'https://www.tradingview.com/chart/?symbol=XYZ',
        'buy_link': 'https://trading212.com/stocks/XYZ',
        'order_book': 'https://example.com/orderbook/XYZ',
        'catalyst_news': 'https://news.example.com/fda-approval-xyz',
        'notes': 'Strong volume, breaking out of consolidation.'
    }
    res = send_alert('penny', penny_data)
    print(res)
