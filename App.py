import streamlit as st
import pandas as pd
import requests

# Scalp Prop - Optimized Version
st.set_page_config(page_title="Scalp Prop - Terminal", layout="wide")

st.title("🎯 SCALP PROP • PREMIUM")
st.caption("Institutional Matrix | Live Swarm Sync | Max Leverage: 5X Cross")

st.markdown("---")

# Session State for Sync
if "selected_token" not in st.session_state: st.session_state.selected_token = "BTC"

# --- ENGINE: PREÇOS (Binance) ---
@st.cache_data(ttl=30)
def get_live_price(ticker):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={ticker.upper()}USDT"
        res = requests.get(url, timeout=2).json()
        return float(res['price'])
    except:
        return None

# --- RESTAURAR MÉTRICAS EM LINHA ---
# Valores de exemplo baseados na tua conta Bitfunded (10.000$)
acc_bal = 10000
cash_risk = acc_bal * 0.005 # 0.5% risco
daily_loss = acc_bal * 0.05
profit_target = acc_bal * 0.08

m1, m2, m3 = st.columns(3)
m1.metric("Risk / Trade", f"{cash_risk:.0f} USDT")
m2.metric("Daily Loss", f"{daily_loss:.0f} USDT")
m3.metric("Profit Target", f"{profit_target:.0f} USDT")
st.markdown("---")

# --- CUSTOM TOKEN CALC (Botão de disparo) ---
st.subheader("🔍 Custom Operational Setup")
col_input, col_btn = st.columns([3, 1])
custom_tok = col_input.text_input("Enter Token:", value="LTC")
if col_btn.button("CALCULATE"):
    price = get_live_price(custom_tok)
    if price:
        st.success(f"Entry: ${price:.4f}")
        col_res1, col_res2 = st.columns(2)
        col_res1.write(f"**Stop Loss:** ${price*0.98:.4f}")
        col_res2.write(f"**TP 1:** ${price*1.02:.4f} / **TP 2:** ${price*1.04:.4f}")
        st.warning("Scaling: Add 20% margin at TP1 if volume persists.")
    else:
        st.error("Check Ticker Name (e.g., LTC)")

st.markdown("---")

# --- TOP 10 SWARM SETUPS (Com setup detalhado) ---
st.subheader("🔥 Top 10 Pre-Approved Swarm Setups")
top_tokens = ["BTC", "SOL", "SUI", "LINK", "NEAR", "FET", "ETH", "AVAX", "WIF", "LTC"]

for ticker in top_tokens:
    with st.expander(f"🟢 {ticker} (Auto-Setup)"):
        price = get_live_price(ticker)
        if price:
            st.write(f"**Entry:** ${price:.4f}")
            st.write(f"**Stop Loss:** ${price*0.98:.4f}")
            st.write(f"**Take Profit 1:** ${price*1.02:.4f}")
            st.write(f"**Take Profit 2:** ${price*1.04:.4f}")
        else:
            st.write("Fetching real-time data...")
