import streamlit as st
import pandas as pd
import requests

# Lista de Ativos
BITFUNDED_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP", "SNX", "LINK", "FET", "ICP", "WIF", "PEPE", "DOGE"]

st.set_page_config(layout="wide", page_title="Institutional Terminal")
st.title("🎯 SCALP PROP • TRADING TERMINAL")

# Motor de Preço Real
@st.cache_data(ttl=30)
def get_live_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker}-USD/spot"
        return float(requests.get(url).json()['data']['amount'])
    except:
        return 0.0

tab1, tab2 = st.tabs(["🛡️ RISK & ENTRY", "🔥 SWARM FLOW"])

with tab1:
    st.subheader("⚙️ Position Sizing & Risk")
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    
    # Inputs de Gestão de Risco
    col1, col2, col3 = st.columns(3)
    with col1:
        account_size = st.number_input("ACCOUNT SIZE ($)", value=10000.0)
    with col2:
        risk_percent = st.number_input("RISK PER TRADE (%)", value=1.0)
    with col3:
        stop_loss_pct = st.number_input("STOP LOSS DISTANCE (%)", value=2.0)
        
    current_price = get_live_price(token)
    st.metric(label=f"Current Price ({token})", value=f"${current_price:,.4f}")
    
    if st.button("CALCULATE POSITION"):
        risk_amount = account_size * (risk_percent / 100)
        position_size = risk_amount / (stop_loss_pct / 100)
        
        st.table(pd.DataFrame({
            "Metric": ["Risk Amount ($)", "Position Size ($)", "Entry Price"],
            "Value": [f"${risk_amount:,.2f}", f"${position_size:,.2f}", f"${current_price:,.4f}"]
        }))

with tab2:
    st.write("### 🚀 Swarm Flow: Live Entries")
    for t in BITFUNDED_ASSETS:
        p = get_live_price(t)
        if p > 0:
            # Setup Simples: TP 3% / SL 2%
            st.success(f"**{t}** | Price: ${p:.4f} | TP: ${p*1.03:.4f} | SL: ${p*0.98:.4f}")
