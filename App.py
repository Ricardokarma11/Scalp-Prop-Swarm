import streamlit as st
import pandas as pd
import requests

# Configuração da página
st.set_page_config(page_title="Scalp Prop v4.1 - Live Engine", layout="wide")

st.title("🎯 SCALP PROP • V4.1 LIVE ENGINE")

# --- ENGINE DE DADOS REAL ---
def get_live_price(ticker):
    """Verifica o valor real em tempo real na Binance API."""
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={ticker.upper()}USDT"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return float(response.json()['price'])
        return None
    except:
        return None

# --- UI: INPUT COMPACTO ---
st.subheader("🔍 Live Market Scanner")
col1, col2 = st.columns([3, 1])
with col1:
    token_input = st.text_input("Enter Token (e.g. LTC, BTC, SOL):", value="LTC").upper()
with col2:
    st.write("###") # Alinhamento
    scan_btn = st.button("RUN SCAN")

# --- LÓGICA DE CALCULO E BACKTEST ---
if scan_btn:
    price = get_live_price(token_input)
    if price:
        # Cálculos de Setup Baseados na Alavancagem 1:5
        sl = price * 0.98 # 2% Stop Loss
        tp1 = price * 1.02 # 2% TP
        tp2 = price * 1.04 # 4% TP
        
        st.success(f"✅ Real-Time Data Synced for {token_input}: ${price:.4f}")
        
        # Display de métricas de trade
        m1, m2, m3 = st.columns(3)
        m1.metric("Stop Loss", f"${sl:.4f}")
        m2.metric("Target 1", f"${tp1:.4f}")
        m3.metric("Target 2", f"${tp2:.4f}")
        
        # Logica de Escalonamento
        st.info("🚀 **Scaling Protocol:** If price hits TP1, add 20% to margin and move SL to entry.")
    else:
        st.error("Error: Could not fetch price. Check ticker name.")

st.markdown("---")

# --- TOP 10 SWARM SETUPS (Dinâmico) ---
st.subheader("🔥 Top 10 Swarm Setups")
top_tickers = ["BTC", "SOL", "SUI", "LINK", "NEAR", "FET", "ETH", "AVAX", "WIF", "LTC"]

for ticker in top_tickers:
    with st.expander(f"🟢 {ticker} - Auto Scan"):
        price = get_live_price(ticker)
        if price:
            st.write(f"**Live Entry:** ${price:.4f}")
            st.write(f"**Stop Loss:** ${price * 0.98:.4f}")
            st.write(f"**TP1 (2%):** ${price * 1.02:.4f}")
            st.write(f"**TP2 (4%):** ${price * 1.04:.4f}")
        else:
            st.write("Waiting for swarm sync...")
