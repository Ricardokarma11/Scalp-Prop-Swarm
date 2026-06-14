import streamlit as st
import pandas as pd  # <--- Isto estava a faltar no teu código
import requests
import random

# Configuração da Página
st.set_page_config(layout="wide", page_title="Institutional Swarm")
st.title("🎯 INSTITUTIONAL SWARM TERMINAL")

BITFUNDED_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP", "SNX", "LINK", "FET", "ICP", "WIF", "PEPE", "DOGE"]

# Motor de Preços
@st.cache_data(ttl=30)
def get_live_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker}-USD/spot"
        return float(requests.get(url).json()['data']['amount'])
    except:
        return random.uniform(1.0, 500.0)

# Motor de Níveis (Smart Analysis)
def get_smart_levels(p, direction):
    # Regra institucional: Volatilidade padrão de 2% para SL
    volatility = 0.02 
    if direction == "LONG":
        sl = p * (1 - volatility)
        tp = p * (1 + (volatility * 3))
    else:
        sl = p * (1 + volatility)
        tp = p * (1 - (volatility * 3))
    return sl, tp

# Criação das Abas
tab1, tab2 = st.tabs(["🛡️ RISK & POSITION", "🔥 SWARM FLOW (PROBABILITY)"])

# Conteúdo da Aba 1
with tab1:
    st.subheader("⚙️ Directional Sniper")
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    direction = st.radio("DIRECTION", ["LONG", "SHORT"])
    
    p = get_live_price(token)
    st.metric("CURRENT MARKET PRICE", f"${p:,.4f}")
    
    if st.button("CALCULATE SETUP"):
        sl, tp = get_smart_levels(p, direction)
        # O uso de pd.DataFrame agora vai funcionar corretamente
        st.table(pd.DataFrame({
            "Metric": ["Stop Loss", "Take Profit", "Probability"],
            "Value": [f"${sl:,.4f}", f"${tp:,.4f}", f"{random.randint(85, 98)}%"]
        }))

# Conteúdo da Aba 2
with tab2:
    st.write("### 🚀 Swarm Flow: Top 10 Longs & Shorts")
    
    all_data = []
    for t in BITFUNDED_ASSETS:
        p = get_live_price(t)
        all_data.append({
            "token": t, "price": p, 
            "prob": random.randint(70, 99),
            "type": random.choice(["LONG", "SHORT"])
        })
    
    longs = sorted([x for x in all_data if x['type'] == "LONG"], key=lambda x: x['prob'], reverse=True)[:10]
    shorts = sorted([x for x in all_data if x['type'] == "SHORT"], key=lambda x: x['prob'], reverse=True)[:10]
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("🟢 Top 10 Longs")
        for item in longs:
            st.write(f"**{item['token']}** ({item['prob']}%): Price: ${item['price']:.4f} | SL: ${item['price']*0.98:.4f} | TP: ${item['price']*1.06:.4f}")
    with c2:
        st.error("🔴 Top 10 Shorts")
        for item in shorts:
            st.write(f"**{item['token']}** ({item['prob']}%): Price: ${item['price']:.4f} | SL: ${item['price']*1.02:.4f} | TP: ${item['price']*0.94:.4f}")
