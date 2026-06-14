import streamlit as st
import pandas as pd
import requests

# 1. LISTA MESTRA E CONFIGURAÇÃO
BITFUNDED_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP", "SNX", "LINK", "FET", "ICP", "WIF", "PEPE", "DOGE"]

st.set_page_config(layout="wide", page_title="Institutional Terminal")
st.title("🎯 SCALP PROP • INSTITUTIONAL TERMINAL")

# 2. MOTOR DE PREÇO HÍBRIDO (Dados Reais)
@st.cache_data(ttl=30)
def get_hybrid_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker}-USD/spot"
        return float(requests.get(url).json()['data']['amount'])
    except:
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={ticker.lower()}&vs_currencies=usd"
            data = requests.get(url).json()
            return float(data[ticker.lower()]['usd'])
        except:
            return 0.0

# 3. INTERFACE DE ABAS
tab1, tab2, tab3, tab4 = st.tabs(["🛡️ RISK & SNIPER", "🔥 SWARM FLOW", "📊 LIQUIDATION HEATMAPS", "🌍 MACRO"])

# --- ABA 1: MOTOR DE BUSCA (SNIPER TÉCNICO) ---
with tab1:
    st.subheader("⚙️ Technical Sniper (Fibo & VWAP)")
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    direction = st.radio("SELECT DIRECTION", ["LONG", "SHORT"])
    
    col1, col2 = st.columns(2)
    with col1:
        swing_high = st.number_input("SWING HIGH", value=100.0)
    with col2:
        swing_low = st.number_input("SWING LOW", value=90.0)
    
    current_price = get_hybrid_price(token)
    fibo_618 = swing_low + (swing_high - swing_low) * 0.618
    distancia_fibo = abs(current_price - fibo_618)
    
    # Cálculos Dinâmicos
    sl = (current_price - distancia_fibo) if direction == "LONG" else (current_price + distancia_fibo)
    tp = (current_price + (distancia_fibo * 3)) if direction == "LONG" else (current_price - (distancia_fibo * 3))
    
    st.write(f"### Preço Atual: ${current_price:.4f} | Golden Pocket: ${fibo_618:.4f}")
    
    if st.button("CALCULATE INSTITUTIONAL LEVELS"):
        st.table(pd.DataFrame({
            "Metric": ["Stop Loss (Fibo-Based)", "Take Profit (1:3 RR)"],
            "Value": [f"${sl:.4f}", f"${tp:.4f}"]
        }))

# --- ABA 2: SWARM FLOW (EXECUÇÃO IMEDIATA) ---
with tab2:
    st.write("### 🚀 Swarm Flow: Execução Imediata")
    # Loop de processamento de tokens
    for t in BITFUNDED_ASSETS:
        p = get_hybrid_price(t)
        if p > 0:
            # SL e TP calculados automaticamente para velocidade
            sl_swarm = p * 0.985 if p > 0 else 0
            tp_swarm = p * 1.045 if p > 0 else 0
            st.success(f"**{t}** | Price: ${p:.4f} | TP: ${tp_swarm:.4f} | SL: ${sl_swarm:.4f}")

with tab3:
    st.write("### 📊 Liquidation Heatmaps")
    st.info("Monitorização de liquidez ativa.")
    

with tab4:
    st.write("### 🌍 Análise Macro & Fibo")
    st.write("Visualização de confluência técnica de mercado.")
    [attachment_0](attachment)
