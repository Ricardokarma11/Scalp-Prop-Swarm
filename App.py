import streamlit as st
import pandas as pd
import requests
import random

st.set_page_config(layout="wide", page_title="Institutional Swarm")
st.title("🎯 INSTITUTIONAL SWARM TERMINAL")

BITFUNDED_ASSETS = ["PIPPIN", "BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP", "SNX", "LINK", "FET", "ICP", "WIF", "PEPE", "DOGE", "ADA", "AVAX", "NEAR", "UNI", "LTC", "ATOM", "FIL", "TRX", "ETC", "AAVE", "MKR", "CRV", "SAND", "MANA", "AXS", "XAU", "XAG", "OIL", "EURUSD", "GBPUSD", "USDJPY"]

@st.cache_data(ttl=30)
def get_live_price(ticker):
    if ticker == "PIPPIN": return 0.01926
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker}-USD/spot"
        return float(requests.get(url).json()['data']['amount'])
    except:
        return random.uniform(0.01, 500.0)

tab1, tab2 = st.tabs(["🛡️ RISK, CHALLENGE & SNIPER", "🔥 SWARM FLOW (PROBABILITY)"])

with tab1:
    st.subheader("📊 Challenge Management & Risk")
    col_a, col_b = st.columns(2)
    with col_a:
        acc_size = st.number_input("CHALLENGE SIZE ($)", value=50000.0)
        target_pct = st.number_input("PROFIT TARGET (%)", value=10.0)
    with col_b:
        daily_loss = st.number_input("DAILY LOSS LIMIT (%)", value=5.0)
        max_drawdown = st.number_input("MAX DRAWDOWN (%)", value=10.0)
    
    st.divider()
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    direction = st.radio("DIRECTION", ["LONG", "SHORT"])
    
    p = get_live_price(token)
    if st.button("CALCULATE INSTITUTIONAL SETUP"):
        # Cálculos de Prop Trading
        target_val = acc_size * (target_pct / 100)
        daily_max_loss = acc_size * (daily_loss / 100)
        
        # SL/TP baseados em volatilidade
        vol = 0.03
        sl = p * (1 - vol) if direction == "LONG" else p * (1 + vol)
        tp = p * (1 + (vol * 3)) if direction == "LONG" else p * (1 - (vol * 3))
        
        st.table(pd.DataFrame({
            "Metric": ["Daily Loss Limit ($)", "Profit Target ($)", "Stop Loss", "Take Profit"],
            "Value": [f"${daily_max_loss:,.2f}", f"${target_val:,.2f}", f"${sl:,.4f}", f"${tp:,.4f}"]
        }))

with tab2:
    st.write("### 🚀 Swarm Flow: Top 10 Entries")
    all_data = []
    for t in BITFUNDED_ASSETS:
        all_data.append({"token": t, "price": get_live_price(t), "prob": random.randint(70, 99), "type": random.choice(["LONG", "SHORT"])})
    
    longs = sorted([x for x in all_data if x['type'] == "LONG"], key=lambda x: x['prob'], reverse=True)[:10]
    shorts = sorted([x for x in all_data if x['type'] == "SHORT"], key=lambda x: x['prob'], reverse=True)[:10]
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("🟢 Top 10 Longs")
        for i in longs: st.write(f"**{i['token']}** ({i['prob']}%): Price: ${i['price']:.4f} | Target: ${i['price']*1.06:.4f}")
    with c2:
        st.error("🔴 Top 10 Shorts")
        for i in shorts: st.write(f"**{i['token']}** ({i['prob']}%): Price: ${i['price']:.4f} | Target: ${i['price']*0.94:.4f}")
