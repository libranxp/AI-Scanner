# formatter.py

def format_penny_stock_alert(alert):
    return f"""
🚨 Penny Stock Alert — High Conviction Setup

Symbol: ${alert['symbol']}
Strategy: {alert['strategy']}
Entry: {alert['entry']} | TP: {alert['target']} | SL: {alert['stop_loss']}
Confidence Score: 🟩 {alert['confidence']}% (Strong Setup)
Catalyst: {alert['catalyst']}
Sentiment Score: {alert['sentiment']} (Bullish Momentum)

📊 Float: {alert['float']} | Volume Surge: {alert['volume_surge']} | RSI: {alert['rsi']} | ATR: {alert['atr']}
🔗 TradingView Chart: {alert['chart_link']}
🔗 Buy on Trading212: https://www.trading212.com/
🔗 Order Book: https://bookmap.com/{alert['symbol'].lower()}
🔗 Catalyst News: {alert['news_link']}

⚠️ Notes: {alert['notes']}
"""

def format_regular_stock_alert(alert):
    return f"""
🚨 Stock Alert — Swing Setup

Symbol: ${alert['symbol']}
Strategy: {alert['strategy']}
Entry: {alert['entry']} | TP: {alert['target']} | SL: {alert['stop_loss']}
Confidence Score: 🟨 {alert['confidence']}% (Watchlist Candidate)
Catalyst: {alert['catalyst']}
Sentiment Score: {alert['sentiment']} (Moderate Bullish Bias)

📊 Float: {alert['float']} | Rel Vol: {alert['rel_vol']} | RSI: {alert['rsi']} | ATR: {alert['atr']}
🔗 TradingView Chart: {alert['chart_link']}
🔗 Buy on Trading212: https://www.trading212.com/
🔗 Order Book: https://bookmap.com/{alert['symbol'].lower()}
🔗 Catalyst News: {alert['news_link']}

📝 Analyst Note: {alert['notes']}
"""

def format_crypto_alert(alert):
    return f"""
🚨 Crypto Alert — Momentum Breakout

Asset: ${alert['symbol']}
Strategy: {alert['strategy']}
Entry: {alert['entry']} | TP: {alert['target']} | SL: {alert['stop_loss']}
Confidence Score: 🟩 {alert['confidence']}% (High Conviction)
Catalyst: {alert['catalyst']}
Sentiment Score: {alert['sentiment']} (Strong Buy Signal)

📊 Volume Spike: {alert['volume_surge']} | RSI: {alert['rsi']} | Order Flow: {alert['order_flow']}
🔗 TradingView Chart: {alert['chart_link']}
🔗 Trade on Kraken: https://kraken.com/trade/{alert['symbol'].lower()}
🔗 Order Book: https://bookmap.com/{alert['symbol'].lower()}
🔗 Catalyst News: {alert['news_link']}

📢 Alert: {alert['notes']}
"""

def format_watchlist(watchlist):
    header = """
📋 Emerald Watchlist (Live Monitor)

Symbol | Strategy     | Entry   | TP     | SL     | Confidence | Catalyst
-------|--------------|---------|--------|--------|------------|---------------------"""
    rows = "\n".join([f"{item['symbol']}   | {item['strategy']} | {item['entry']}   | {item['target']}  | {item['stop_loss']}  | {item['confidence']}%        | {item['catalyst']}" for item in watchlist])
    links = "\n".join([f"🔗 [{item['symbol']} Chart]({item['chart_link']}) | [Buy {item['symbol']}]({item['buy_link']})" for item in watchlist])
    return f"{header}\n{rows}\n\n{links}"

def format_validation(alert):
    return f"""
🔍 AI Reasoning — Why is ${alert['symbol']} Trending?

✅ Float & Volume Surge: {alert['float']} float with {alert['volume_surge']} volume spike, indicating breakout potential.
✅ Catalyst: {alert['catalyst']}
✅ Sentiment: {alert['sentiment']} — indicates heavy bullish chatter across Reddit & StockTwits.
✅ Technicals: {alert['technicals']}

⚠️ Caution: {alert['caution']}

📊 AI Verdict: {alert['verdict']}
"""

def format_wrapup(wrapup_type, date, movers, watchlist_focus, market_conditions, observations=None):
    if wrapup_type == "pre-market":
        header = f"🌅 Pre-Market Wrap-Up — {date}"
    elif wrapup_type == "post-market":
        header = f"🌇 Post-Market Recap — {date}"
    else:
        header = f"📊 Weekend Swing Watchlist"

    movers_section = "\n".join([f"- ${item['symbol']} | {item['gap']} Gap | {item['catalyst']} | {item['sentiment']}" for item in movers])
    focus_section = "\n".join([f"🟩 {item['symbol']} | Entry: {item['entry']} | TP: {item['target']} | SL: {item['stop_loss']} | Confidence: {item['confidence']}%" for item in watchlist_focus])
    conditions = f"📊 Market Conditions: {market_conditions}"

    wrapup = f"{header}\n\n🔥 Top Movers:\n{movers_section}\n\n⚡️ Watchlist Focus:\n{focus_section}\n\n{conditions}"

    if observations:
        obs_section = "\n".join([f"- {obs}" for obs in observations])
        wrapup += f"\n\n📝 Key Observations:\n{obs_section}"

    return wrapup
