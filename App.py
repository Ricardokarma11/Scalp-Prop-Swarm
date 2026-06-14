import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Scalp Prop", layout="wide")
st.title("🎯 SCALP PROP")

# --- ENGINE DE PREÇOS (Otimizado) ---
def get_price(token):
    try:
        # Formata o ticker para o padrão Binance
        symbol = f"{token.strip().upper()}USDT"
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return float(response.json()['price'])
        return None
    except:
        return None

# --- UI: CUSTOM SETUP ---
st.subheader("🔍 Custom Setup")
token_input = st.text_input("Enter Token:", value="LTC")
if st.button("CALCULATE"):
    price = get_price(token_input)
    if price:
        st.success(f"Market: {token_input.upper()} | Price: ${price:.4f}")
        # Setup fixo 1:3 RR
        sl = price * 0.98
        tp1 = price * 1.02
        tp2 = price * 1.04
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Stop Loss", f"${sl:.4f}")
        c2.metric("TP 1", f"${tp1:.4f}")
        c3.metric("TP 2", f"${tp2:.4f}")
        st.info("💡 Action: Add 20% margin if price confirms trend at TP1.")
    else:
        st.error("Ticker not found. Try 'BTC', 'ETH', 'LTC'.")

st.markdown("---")

# --- LISTA SWARM ---
st.subheader("🔥 Top 10 Pre-Approved Swarm Setups")
tokens = ["BTC", "SOL", "SUI", "LINK", "NEAR", "FET", "ETH", "AVAX", "WIF", "LTC"]

for t in tokens:
    with st.expander(f"🟢 {t} - View Setup"):
        p = get_price(t)
        if p:
            st.write(f"**Entry:** ${p:.4f}")
            st.write(f"**Stop Loss:** ${p*0.98:.4f}")
            st.write(f"**TP 1:** ${p*1.02:.4f} | **TP 2:** ${p*1.04:.4f}")
        else:
            st.write("Syncing data...")
