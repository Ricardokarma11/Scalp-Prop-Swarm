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
st.title("🎯 SCALP PROP • INSTITUTIONAL TERMINAL")

def get_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker.upper()}-USD/spot"
        res = requests.get(url, timeout=2).json()
        return float(res['data']['amount'])
    except:
        return None

tab1, tab2, tab3 = st.tabs(["🛡️ RISK & SNIPER", "🔥 SWARM FLOW", "🌍 MACRO"])

with tab1:
    st.subheader("⚙️ Account & Sniper Parameters")
    selected_token = st.selectbox("SELECT TOKEN", BITFUNDED_ASSETS)
    current_price = get_price(selected_token)
    
    acc_bal = st.number_input("ACCOUNT BALANCE ($)", value=5000, step=1000)
    risk_pct = st.number_input("MAX RISK (%)", value=1.00, step=0.10)
    entry_price = st.number_input("ENTRY PRICE", value=current_price or 0.0, format="%.4f")
    leverage = st.number_input("LEVERAGE (MAX 5X)", min_value=1, max_value=5, value=5, step=1)
    
    if st.button("EXECUTE SNIPER ORDER"):
        pos_size = (acc_bal * (risk_pct / 100)) * leverage
        st.table(pd.DataFrame({
            "Metric": ["Position Size (at 5x)", "Stop Loss (2%)", "Take Profit (6%)"],
            "Value": [f"${pos_size:,.2f}", f"${entry_price*0.98:.4f}", f"${entry_price*1.06:.4f}"]
        }))

with tab2:
    st.write("### 📈 Top 10 Swarm Probability Setups")
    # 1. Gerar dados com probabilidade
    swarm_data = []
    for t in BITFUNDED_ASSETS:
        p = get_price(t)
        if p:
            prob = random.randint(70, 99) # Simulação de probabilidade
            swarm_data.append({"token": t, "price": p, "prob": prob})
    
    # 2. Ordenar por probabilidade (maior para menor)
    swarm_data = sorted(swarm_data, key=lambda x: x['prob'], reverse=True)[:10]
    
    # 3. Exibir Top 10
    for item in swarm_data:
        with st.expander(f"🟢 {item['token']} - **{item['prob']}% Success Probability**"):
            st.write(f"**Price:** ${item['price']:.4f} | **SL:** ${item['price']*0.98:.4f} | **TP:** ${item['price']*1.06:.4f}")

with tab3:
    st.write("### 🌍 Macro & Study")
    st.write("Terminal otimizado para os pares USDT da Bitfunded.")
