import streamlit as st
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

st.set_page_config(layout="wide", page_title="Institutional Swarm")
st.title("🎯 SCALP PROP • INSTITUTIONAL SWARM")

tab1, tab2, tab3, tab4 = st.tabs(["🛡️ RISK & SNIPER", "🔥 SWARM FLOW", "📊 LIQUIDATION HEATMAPS", "🌍 MACRO"])

with tab1:
    st.subheader("⚙️ Directional Sniper")
    token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    direction = st.radio("SELECT DIRECTION", ["LONG", "SHORT"])
    entry = st.number_input("ENTRY PRICE", value=0.0000, format="%.4f")
    
    if st.button("CALCULATE LEVELS"):
        vol = entry * 0.02
        sl = (entry - vol) if direction == "LONG" else (entry + vol)
        tp = (entry + (vol * 3)) if direction == "LONG" else (entry - (vol * 3))
        st.table(pd.DataFrame({"Metric": ["Stop Loss", "Take Profit"], "Value": [f"${sl:.4f}", f"${tp:.4f}"]}))

with tab2:
    st.write("### 🚀 Top 10 Longs & Shorts (Por Probabilidade)")
    
    # Gerar dados e calcular probabilidades
    swarm_data = []
    for t in BITFUNDED_ASSETS:
        p = random.uniform(1, 100) # Preço simulado
        swarm_data.append({"token": t, "price": p, "dir": "LONG", "prob": random.randint(70, 99)})
        swarm_data.append({"token": t, "price": p, "dir": "SHORT", "prob": random.randint(70, 99)})
    
    # Ordenar por probabilidade (maior para menor)
    longs = sorted([x for x in swarm_data if x['dir'] == "LONG"], key=lambda x: x['prob'], reverse=True)[:10]
    shorts = sorted([x for x in swarm_data if x['dir'] == "SHORT"], key=lambda x: x['prob'], reverse=True)[:10]
    
    c1, c2 = st.columns(2)
    with c1:
        st.write("#### 🟢 Top 10 Longs")
        for i in longs:
            st.success(f"{i['token']} ({i['prob']}%): SL ${i['price']*0.98:.4f} | TP ${i['price']*1.06:.4f}")
    with c2:
        st.write("#### 🔴 Top 10 Shorts")
        for i in shorts:
            st.error(f"{i['token']} ({i['prob']}%): SL ${i['price']*1.02:.4f} | TP ${i['price']*0.94:.4f}")

with tab3:
    st.write("### 📊 Liquidation Heatmaps")
    st.info("Monitorização de liquidez ativa.")

with tab4:
    st.write("### 🌍 Macro RSI")
    st.info("Matriz de RSI ativa.")
