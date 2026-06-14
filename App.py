import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Scalp Prop Terminal", layout="wide")

st.title("🎯 SCALP PROP • PREMIUM V4")
st.caption("Institutional Matrix | Live Coinbase Sync | Bitfunded Protocol")

# --- ENGINE DE PREÇO (Coinbase - Estável) ---
@st.cache_data(ttl=30)
def get_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker.upper()}-USD/spot"
        res = requests.get(url, timeout=5).json()
        return float(res['data']['amount'])
    except:
        return None

# --- ABAS DE NAVEGAÇÃO ---
tab1, tab2 = st.tabs(["🧮 TERMINAL", "🛡️ RISK MANAGEMENT"])

with tab1:
    # 1. MÉTRICAS EM LINHA
    m1, m2, m3 = st.columns(3)
    m1.metric("Risk / Trade", "50 USDT")
    m2.metric("Daily Loss", "500 USDT")
    m3.metric("Profit Target", "800 USDT")
    st.markdown("---")

    # 2. CUSTOM SCANNER
    st.subheader("🔍 Custom Token Scan")
    col_in, col_btn = st.columns([3, 1])
    custom_tok = col_in.text_input("Enter Token:", value="LTC")
    
    if col_btn.button("SCAN SETUP"):
        price = get_price(custom_tok)
        if price:
            sl = price * 0.98
            tp1 = price * 1.02
            tp2 = price * 1.04
            st.success(f"✅ {custom_tok.upper()} Ready | Entry: ${price:.4f}")
            c1, c2, c3 = st.columns(3)
            c1.metric("Stop Loss", f"${sl:.4f}")
            c2.metric("TP 1 (2%)", f"${tp1:.4f}")
            c3.metric("TP 2 (4%)", f"${tp2:.4f}")
            st.info("🚀 Scaling Protocol: If price hits TP1, add 20% to margin and move SL to Entry.")
        else:
            st.error("Error: Check ticker name (e.g., BTC, ETH, LTC).")

    st.markdown("---")

    # 3. TOP 10 SWARM SETUPS (Automático)
    st.subheader("🔥 Top 10 Pre-Approved Swarm Setups")
    tokens = ["BTC", "SOL", "SUI", "LINK", "NEAR", "FET", "ETH", "AVAX", "WIF", "LTC"]
    
    # Exibir todos os setups automaticamente
    for t in tokens:
        p = get_price(t)
        if p:
            with st.expander(f"🟢 {t} | Entry: ${p:.4f}"):
                c1, c2, c3, c4 = st.columns(4)
                c1.write(f"**SL:** ${p*0.98:.4f}")
                c2.write(f"**TP1:** ${p*1.02:.4f}")
                c3.write(f"**TP2:** ${p*1.04:.4f}")
                c4.write("**Scale:** +20% @ TP1")
        else:
            st.write(f"🟢 {t} - Syncing data...")

with tab2:
    st.subheader("🛡️ Risk Management Rules")
    st.write("- Max Daily Drawdown: 5%")
    st.write("- Max Total Drawdown: 10%")
    st.write("- Leverage Limit: 1:5 Cross")
    st.write("- Trading Phase: Stage 1 (8% Target)")
