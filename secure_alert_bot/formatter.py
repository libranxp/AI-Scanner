import re

def escape_markdown(text):
    """
    Escape text for Telegram MarkdownV2 parse_mode.
    """
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', str(text))

def format_penny_alert(data):
    return (
        "\ud83d\udea8 *Penny Stock Alert \u2014 High Conviction Setup*\n\n"
        f"*Symbol:* ${escape_markdown(data['symbol'])}\n"
        f"*Strategy:* {escape_markdown(data['strategy'])}\n"
        f"*Entry:* ${escape_markdown(data['entry'])} | *TP:* ${escape_markdown(data['tp'])} | *SL:* ${escape_markdown(data['sl'])}\n"
        f"*Confidence Score:* {escape_markdown(data['confidence_emoji'])} {escape_markdown(data['confidence_percent'])}% ({escape_markdown(data['confidence_text'])})\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment Score:* {escape_markdown(data['sentiment_score'])} ({escape_markdown(data['sentiment_text'])})\n\n"
        f"\ud83d\udcc8 *Float:* {escape_markdown(data['float'])}M | *Volume Surge:* +{escape_markdown(data['volume_surge'])}% | *RSI:* {escape_markdown(data['rsi'])} | *ATR:* {escape_markdown(data['atr'])}\n"
        f"\ud83d\udd17 [TradingView Chart]({escape_markdown(data['tv_chart'])})\n"
        f"\ud83d\udd17 [Buy on Trading212]({escape_markdown(data['buy_link'])})\n"
        f"\ud83d\udd17 [Order Book]({escape_markdown(data['order_book'])})\n"
        f"\ud83d\udd17 [Catalyst News]({escape_markdown(data['catalyst_news'])})\n\n"
        f"\u26a0\ufe0f *Notes:* {escape_markdown(data['notes'])}"
    )

def format_stock_alert(data):
    return (
        "\ud83d\udea8 *Stock Alert \u2014 Swing Setup*\n\n"
        f"*Symbol:* ${escape_markdown(data['symbol'])}\n"
        f"*Strategy:* {escape_markdown(data['strategy'])}\n"
        f"*Entry:* ${escape_markdown(data['entry'])} | *TP:* ${escape_markdown(data['tp'])} | *SL:* ${escape_markdown(data['sl'])}\n"
        f"*Confidence Score:* {escape_markdown(data['confidence_emoji'])} {escape_markdown(data['confidence_percent'])}% ({escape_markdown(data['confidence_text'])})\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment Score:* {escape_markdown(data['sentiment_score'])} ({escape_markdown(data['sentiment_text'])})\n\n"
        f"\ud83d\udcc8 *Float:* {escape_markdown(data['float'])}M | *Rel Vol:* {escape_markdown(data['rel_vol'])} | *RSI:* {escape_markdown(data['rsi'])} | *ATR:* {escape_markdown(data['atr'])}\n"
        f"\ud83d\udd17 [TradingView Chart]({escape_markdown(data['tv_chart'])})\n"
        f"\ud83d\udd17 [Buy on Trading212]({escape_markdown(data['buy_link'])})\n"
        f"\ud83d\udd17 [Order Book]({escape_markdown(data['order_book'])})\n"
        f"\ud83d\udd17 [Catalyst News]({escape_markdown(data['catalyst_news'])})\n\n"
        f"\ud83d\uddd8\ufe0f *Analyst Note:* {escape_markdown(data['analyst_note'])}"
    )

def format_crypto_alert(data):
    return (
        "\ud83d\udea8 *Crypto Alert \u2014 Momentum Breakout*\n\n"
        f"*Asset:* ${escape_markdown(data['asset'])}\n"
        f"*Strategy:* {escape_markdown(data['strategy'])}\n"
        f"*Entry:* ${escape_markdown(data['entry'])} | *TP:* ${escape_markdown(data['tp'])} | *SL:* ${escape_markdown(data['sl'])}\n"
        f"*Confidence Score:* {escape_markdown(data['confidence_emoji'])} {escape_markdown(data['confidence_percent'])}% ({escape_markdown(data['confidence_text'])})\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment Score:* {escape_markdown(data['sentiment_score'])} ({escape_markdown(data['sentiment_text'])})\n\n"
        f"\ud83d\udcc8 *Volume Spike:* +{escape_markdown(data['volume_spike'])}% | *RSI:* {escape_markdown(data['rsi'])} | *Order Flow:* {escape_markdown(data['order_flow'])}\n"
        f"\ud83d\udd17 [TradingView Chart]({escape_markdown(data['tv_chart'])})\n"
        f"\ud83d\udd17 [Trade on Kraken]({escape_markdown(data['trade_link'])})\n"
        f"\ud83d\udd17 [Order Book]({escape_markdown(data['order_book'])})\n"
        f"\ud83d\udd17 [Catalyst News]({escape_markdown(data['catalyst_news'])})\n\n"
        f"\ud83d\udce2 *Alert:* {escape_markdown(data['alerts'])}"
    )

def format_watchlist_alert(data):
    return (
        "\ud83d\uddd2\ufe0f *Daily Watchlist Update*\n\n"
        f"*Symbol:* ${escape_markdown(data['symbol'])}\n"
        f"*Setup:* {escape_markdown(data['setup'])}\n"
        f"*Price Range:* ${escape_markdown(data['price_range'])}\n"
        f"*Catalyst:* {escape_markdown(data['catalyst'])}\n"
        f"*Sentiment:* {escape_markdown(data['sentiment'])}\n"
        f"*Key Levels:* {escape_markdown(data['key_levels'])}\n\n"
        f"\ud83d\udcc8 *Float:* {escape_markdown(data['float'])}M | *Rel Vol:* {escape_markdown(data['rel_vol'])} | *RSI:* {escape_markdown(data['rsi'])}\n"
        f"\ud83d\udd17 [Chart Link]({escape_markdown(data['chart_link'])}) | \ud83d\udd17 [News]({escape_markdown(data['news_link'])})"
    )

def format_validation_alert(data):
    return (
        "\u2705 *Trade Validation \u2014 Setup Confirmed*\n\n"
        f"*Symbol:* ${escape_markdown(data['symbol'])}\n"
        f"*Trigger Level:* ${escape_markdown(data['trigger'])}\n"
        f"*Breakout Volume:* {escape_markdown(data['volume'])}\n"
        f"*Order Flow Bias:* {escape_markdown(data['order_flow'])}\n"
        f"*Sentiment Update:* {escape_markdown(data['sentiment'])}\n"
        f"*Updated Confidence:* {escape_markdown(data['confidence'])}\n\n"
        f"\ud83d\udd17 [Live Chart]({escape_markdown(data['chart_link'])})"
    )

def format_wrapup_alert(data):
    return (
        "\ud83d\udd9a *Wrap-Up \u2014 Daily Recap*\n\n"
        f"*Date:* {escape_markdown(data['date'])}\n"
        f"*Top Gainer:* ${escape_markdown(data['top_gainer'])}\n"
        f"*Biggest Mover:* ${escape_markdown(data['biggest_mover'])}\n"
        f"*News Highlight:* {escape_markdown(data['news_highlight'])}\n"
        f"*Market Sentiment:* {escape_markdown(data['market_sentiment'])}\n\n"
        f"\ud83d\udcc8 *SPY Close:* {escape_markdown(data['spy_close'])} | *QQQ Close:* {escape_markdown(data['qqq_close'])}\n"
        f"\ud83d\udd17 [Full Report]({escape_markdown(data['report_link'])})"
    )

