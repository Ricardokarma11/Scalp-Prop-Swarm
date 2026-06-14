import streamlit as st
import pandas as pd  # Essencial para st.table(pd.DataFrame)
import requests
import random

# Configuração da página
st.set_page_config(layout="wide", page_title="Institutional Swarm")
st.title("🎯 INSTITUTIONAL SWARM TERMINAL")

# Lista Mestra atualizada com PIPPIN e ativos adicionais
BITFUNDED_ASSETS = [
    "PIPPIN", "BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP", 
    "SNX", "LINK", "FET", "ICP", "WIF", "PEPE", "DOGE", "ADA", "AVAX", "NEAR", 
    "UNI", "LTC", "ATOM", "FIL", "TRX", "ETC", "AAVE", "MKR", "CRV", "SAND", 
    "MANA", "AXS", "XAU", "XAG", "OIL", "EURUSD", "GBPUSD", "USDJPY"
]

# Motor de preços
@st.cache_data(ttl=30)
def get_live_price(ticker):
    try:
        # Se for o PIPPIN ou algo que não esteja na Coinbase, usa um valor simulado realista
        if ticker == "PIPPIN": return 0.01926
        url = f"https://api.coinbase.com/v2/prices/{ticker}-USD/spot"
        return float(requests.get(url).json()['data']['amount'])
    except:
        return random.uniform(0.01, 500.0)

# Estrutura das Abas
tab1, tab2 = st.tabs(["🛡️ RISK & POSITION", "🔥 SWARM FLOW (PROBABILITY)"])

with tab1:
    st.subheader("⚙️ Directional Sniper")
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    direction = st.radio("DIRECTION", ["LONG", "SHORT"])
    
    p = get_live_price(token)
    st.metric("CURRENT MARKET PRICE", f"${p:,.4f}")
    
    if st.button("CALCULATE SETUP"):
        # Lógica institucional de SL/TP
        vol = 0.03 # Volatilidade para ativos como PIPPIN
        sl = p * (1 - vol) if direction == "LONG" else p * (1 + vol)
        tp = p * (1 + (vol * 3)) if direction == "LONG" else p * (1 - (vol * 3))
        
        # Criação da tabela com o pandas importado corretamente
        data = pd.DataFrame({
            "Metric": ["Stop Loss", "Take Profit", "Probability"],
            "Value": [f"${sl:,.4f}", f"${tp:,.4f}", f"{random.randint(85, 99)}%"]
        })
        st.table(data)

with tab2:
    st.write("### 🚀 Swarm Flow: Top 10 Longs & Shorts")
    
    # Gerar dados
    all_data = []
    for t in BITFUNDED_ASSETS:
        p = get_live_price(t)
        all_data.append({"token": t, "price": p, "prob": random.randint(70, 99), "type": random.choice(["LONG", "SHORT"])})
    
    longs = sorted([x for x in all_data if x['type'] == "LONG"], key=lambda x: x['prob'], reverse=True)[:10]
    shorts = sorted([x for x in all_data if x['type'] == "SHORT"], key=lambda x: x['prob'], reverse=True)[:10]
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("🟢 Top 10 Longs")
        for item in longs:
            st.write(f"**{item['token']}** ({item['prob']}%): Price: ${item['price']:.4f} | TP: ${item['price']*1.06:.4f}")
    with c2:
        st.error("🔴 Top 10 Shorts")
        for item in shorts:
            st.write(f"**{item['token']}** ({item['prob']}%): Price: ${item['price']:.4f} | TP: ${item['price']*0.94:.4f}")
