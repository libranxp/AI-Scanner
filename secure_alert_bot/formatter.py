# formatter.py

from datetime import datetime

def format_penny_stock_alert(data):
    return f"""🚨 Penny Stock Alert — High Conviction Setup

Symbol: ${data['symbol']}
Strategy: {data['strategy']}
Entry: ${data['entry']} | TP: ${data['target']} | SL: ${data['stoploss']}
Confidence Score: 🟩 {data['confidence']}% (Strong Setup)
Catalyst: {data['catalyst']}
Sentiment Score: {data['sentiment']} ({data['sentiment_text']})

📊 Float: {data['float']}M | Volume Surge: +{data['volume_surge']}% | RSI: {data['rsi']} | ATR: {data['atr']}
🔗 TradingView Chart: {data['tv_link']}
🔗 Buy on Trading212: https://www.trading212.com/
🔗 Order Book: https://bookmap.com/{data['symbol'].lower()}
🔗 Catalyst News: {data['news_link']}

⚠️ Notes: {data['notes']}"""

def format_regular_stock_alert(data):
    return f"""🚨 Stock Alert — Swing Setup

Symbol: ${data['symbol']}
Strategy: {data['strategy']}
Entry: ${data['entry']} | TP: ${data['target']} | SL: ${data['stoploss']}
Confidence Score: 🟨 {data['confidence']}% (Watchlist Candidate)
Catalyst: {data['catalyst']}
Sentiment Score: {data['sentiment']} ({data['sentiment_text']})

📊 Float: {data['float']}M | Rel Vol: {data['rel_vol']} | RSI: {data['rsi']} | ATR: {data['atr']}
🔗 TradingView Chart: {data['tv_link']}
🔗 Buy on Trading212: https://www.trading212.com/
🔗 Order Book: https://bookmap.com/{data['symbol'].lower()}
🔗 Catalyst News: {data['news_link']}

📝 Analyst Note: {data['notes']}"""

def format_crypto_alert(data):
    return f"""🚨 Crypto Alert — Momentum Breakout

Asset: ${data['symbol']}
Strategy: {data['strategy']}
Entry: ${data['entry']} | TP: ${data['target']} | SL: ${data['stoploss']}
Confidence Score: 🟩 {data['confidence']}% (High Conviction)
Catalyst: {data['catalyst']}
Sentiment Score: {data['sentiment']} ({data['sentiment_text']})

📊 Volume Spike: +{data['volume_surge']}% | RSI: {data['rsi']} | Order Flow: Bullish Dominance {data['order_flow']}%
🔗 TradingView Chart: {data['tv_link']}
🔗 Trade on Kraken: https://kraken.com/trade/{data['symbol'].lower()}
🔗 Order Book: https://bookmap.com/{data['symbol'].lower()}
🔗 Catalyst News: {data['news_link']}

📢 Alert: {data['notes']}"""

def format_watchlist_table(watchlist_data):
    table = "📋 Emerald Watchlist (Live Monitor)\n\n"
    table += "Symbol | Strategy     | Entry   | TP     | SL     | Confidence | Catalyst\n"
    table += "-------|--------------|---------|--------|--------|------------|---------------------\n"
    for item in watchlist_data:
        table += f"{item['symbol']}   | {item['strategy']:<12} | ${item['entry']:<6} | ${item['target']:<5} | ${item['stoploss']:<5} | {item['confidence']}%        | {item['catalyst']}\n"
    table += "\n"
    for item in watchlist_data:
        table += f"🔗 [{item['symbol']} Chart]({item['tv_link']}) | [Buy {item['symbol']}]({item['buy_link']})\n"
    return table

def format_validation_summary(data):
    return f"""🔍 AI Reasoning — Why is ${data['symbol']} Trending?

✅ Float & Volume Surge: {data['float']}M float with +{data['volume_surge']}% volume spike, indicating breakout potential.
✅ Catalyst: {data['catalyst']}
✅ Sentiment: {data['sentiment']} — indicates {data['sentiment_text']}.
✅ Technicals: {data['technicals']}

⚠️ Caution: {data['caution']}

📊 AI Verdict: {data['verdict']}"""

def format_wrapup_summary(pre, post, weekend):
    now = datetime.now().strftime('%B %d, %Y')
    return f"""### **Pre-Market Wrap-Up (8:30 AM EST)**

🌅 Pre-Market Wrap-Up — {now}

🔥 Top Movers:
{pre['top_movers']}

⚡️ Watchlist Focus:
{pre['watchlist_focus']}

📊 Market Conditions: {pre['market_conditions']}

---

### **Post-Market Recap (4:15 PM EST)**

🌇 Post-Market Recap — {now}

{post['recap']}

📝 Key Observations:
{post['observations']}

---

### **Weekend Swing Summary (Sunday 6:00 PM EST)**

📊 Weekend Swing Watchlist

Symbol | Setup         | Entry  | Target | Confidence | Catalyst
-------|---------------|--------|--------|------------|------------------
{weekend['table']}

⚡️ Focus will be on {weekend['focus']}"""

def format_channel_mapping():
    return """## 📢 ALERT SUMMARY — CHANNELS MAPPED:

| Category              | Telegram Channel  | Frequency                        |
| --------------------- | ----------------- | -------------------------------- |
| Penny Stock Alerts    | `ai_alert_peny`   | Real-time                        |
| Regular Stock Alerts  | `ai_alert_stock`  | Real-time                        |
| Crypto Coin Alerts    | `ai_alert_crypto` | Real-time                        |
| Watchlist Aggregator  | `ai_watchlist`    | Hourly / Manual / Daily          |
| AI Validation Summary | `ai_validation`   | After each alert or bulk scan    |
| Market Wrap-ups       | `ai_wrapup`       | Pre-Market, Post-Market, Weekend |
"""

def format_command_help():
    return """| Command       | Function                              |
| ------------- | ------------------------------------- |
| `/watchlist`  | Posts latest Watchlist table          |
| `/validation` | Live orderbook/tape check on-demand   |
| `/wrapup`     | Posts pre/post-market or weekend wrap |
| `/scalp`      | Shows high-conviction penny setups    |"""


