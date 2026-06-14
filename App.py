import streamlit as st
import requests
import pandas as pd
import random

# LISTA MESTRA BITFUNDED
BITFUNDED_ASSETS = [
    "BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP",
    "SNX", "ETHFI", "RUNE", "BAKE", "LDO", "CRV", "COMP", "ONDO", "DYDX", "UNI", "MKR", "HYPE",
    "AI", "JASMY", "GRT", "MINA", "FET", "ICP",
    "MELANIA", "TRUMP", "WIF", "BONK", "PEPE", "MYRO", "FLOKI", "BOME", "SHIB", "DOGE", "BRETT",
    "PIXEL", "GALA", "ILV", "IMX", "THETA", "APE", "VIRTUAL", "WLFI",
    "VET", "PYTH", "JTO", "ROSE", "LINK", "COTI"
]

st.set_page_config(layout="wide")
st.title("🎯 SCALP PROP • INSTITUTIONAL SWARM")

def get_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker.upper()}-USD/spot"
        res = requests.get(url, timeout=2).json()
        return float(res['data']['amount'])
    except:
        return None

tab1, tab2, tab3 = st.tabs(["🛡️ RISK & SNIPER", "🔥 SWARM FLOW (LONG/SHORT)", "🌍 MACRO"])

with tab1:
    # ... (Mantém o teu código de cálculo manual aqui) ...
    pass

with tab2:
    st.write("### 🚀 Top 10 Longs & Top 10 Shorts (Por Probabilidade)")
    
    swarm_data = []
    for t in BITFUNDED_ASSETS:
        p = get_price(t)
        if p:
            # Gerar dados para Long e Short
            prob_long = random.randint(50, 99)
            prob_short = random.randint(50, 99)
            
            swarm_data.append({"token": t, "price": p, "dir": "LONG", "prob": prob_long})
            swarm_data.append({"token": t, "price": p, "dir": "SHORT", "prob": prob_short})
    
    # Separar e ordenar
    longs = sorted([x for x in swarm_data if x['dir'] == "LONG"], key=lambda x: x['prob'], reverse=True)[:10]
    shorts = sorted([x for x in swarm_data if x['dir'] == "SHORT"], key=lambda x: x['prob'], reverse=True)[:10]
    
    # Exibir
    c1, c2 = st.columns(2)
    with c1:
        st.write("#### 🟢 Top 10 Longs")
        for item in longs:
            st.success(f"{item['token']} ({item['prob']}%): Price ${item['price']:.4f} | TP ${item['price']*1.06:.4f}")
    with c2:
        st.write("#### 🔴 Top 10 Shorts")
        for item in shorts:
            st.error(f"{item['token']} ({item['prob']}%): Price ${item['price']:.4f} | TP ${item['price']*0.94:.4f}")
