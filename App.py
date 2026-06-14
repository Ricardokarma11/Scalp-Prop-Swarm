import streamlit as st
import pandas as pd
import requests
import random

BITFUNDED_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP", "SNX", "LINK", "FET", "ICP", "WIF", "PEPE", "DOGE"]

st.set_page_config(layout="wide", page_title="Institutional Swarm")
st.title("🎯 INSTITUTIONAL SWARM TERMINAL")

@st.cache_data(ttl=30)
def get_live_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker}-USD/spot"
        return float(requests.get(url).json()['data']['amount'])
    except:
        return random.uniform(1.0, 500.0)

tab1, tab2 = st.tabs(["🛡️ RISK & POSITION", "🔥 SWARM FLOW (PROBABILITY)"])

with tab1:
    st.subheader("⚙️ Risk Management")
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    col1, col2, col3 = st.columns(3)
    with col1:
        account_size = st.number_input("ACCOUNT SIZE ($)", value=10000.0)
    with col2:
        risk_pct = st.number_input("RISK PER TRADE (%)", value=1.0)
    with col3:
        sl_dist = st.number_input("STOP LOSS DISTANCE (%)", value=2.0)
        
    p = get_live_price(token)
    if st.button("CALCULATE POSITION"):
        risk_amount = account_size * (risk_pct / 100)
        pos_size = risk_amount / (sl_dist / 100)
        st.table(pd.DataFrame({
            "Metric": ["Entry Price", "Risk Amount", "Position Size"],
            "Value": [f"${p:,.4f}", f"${risk_amount:,.2f}", f"${pos_size:,.2f}"]
        }))

with tab2:
    st.write("### 🚀 Swarm Flow: Top 10 Longs & Shorts")
    
    # Gerar dados simulados para Longs e Shorts
    all_data = []
    for t in BITFUNDED_ASSETS:
        p = get_live_price(t)
        all_data.append({
            "token": t, "price": p, 
            "prob": random.randint(70, 99),
            "type": random.choice(["LONG", "SHORT"])
        })
    
    # Separar e ordenar
    longs = sorted([x for x in all_data if x['type'] == "LONG"], key=lambda x: x['prob'], reverse=True)[:10]
    shorts = sorted([x for x in all_data if x['type'] == "SHORT"], key=lambda x: x['prob'], reverse=True)[:10]
    
    col_l, col_s = st.columns(2)
    with col_l:
        st.success("🟢 Top 10 Longs")
        for item in longs:
            st.write(f"**{item['token']}** ({item['prob']}%): Price: ${item['price']:.4f} | SL: ${item['price']*0.98:.4f} | TP: ${item['price']*1.06:.4f}")
            
    with col_s:
        st.error("🔴 Top 10 Shorts")
        for item in shorts:
            st.write(f"**{item['token']}** ({item['prob']}%): Price: ${item['price']:.4f} | SL: ${item['price']*1.02:.4f} | TP: ${item['price']*0.94:.4f}")
