import streamlit as st
import requests
import pandas as pd

# 1. DEFINIÇÃO DA LISTA MESTRA (Onde tudo se conecta)
BITFUNDED_ASSETS = [
    "BTC", "ETH", "SOL", "BNB", "XRP", "DOT", "ARB", "MATIC", "OP",
    "SNX", "ETHFI", "RUNE", "BAKE", "LDO", "CRV", "COMP", "ONDO", "DYDX", "UNI", "MKR", "HYPE",
    "AI", "JASMY", "GRT", "MINA", "FET", "ICP",
    "MELANIA", "TRUMP", "WIF", "BONK", "PEPE", "MYRO", "FLOKI", "BOME", "SHIB", "DOGE", "BRETT",
    "PIXEL", "GALA", "ILV", "IMX", "THETA", "APE", "VIRTUAL", "WLFI",
    "VET", "PYTH", "JTO", "ROSE", "LINK", "COTI"
]

st.set_page_config(page_title="Scalp Prop - Institutional", layout="wide")
st.title("🎯 SCALP PROP • INSTITUTIONAL TERMINAL")

def get_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker.upper()}-USD/spot"
        res = requests.get(url, timeout=3).json()
        return float(res['data']['amount'])
    except:
        return None

tab1, tab2, tab3 = st.tabs(["🛡️ RISK & SNIPER", "🔥 SWARM FLOW", "🌍 MACRO"])

with tab1:
    st.subheader("⚙️ Account & Sniper Parameters")
    # A LISTA AQUI NO SELECTBOX
    token_input = st.selectbox("SELECT TOKEN (Whitelisted)", BITFUNDED_ASSETS)
    
    acc_bal = st.number_input("ACCOUNT BALANCE ($)", value=5000, step=1000)
    risk_pct = st.number_input("MAX RISK PER TRADE (%)", value=1.00, step=0.10)
    entry_price = st.number_input("ENTRY PRICE", value=0.0000, format="%.4f")
    leverage = st.number_input("LEVERAGE (MAX 5X)", min_value=1, max_value=5, value=5, step=1)
    
    if st.button("EXECUTE SNIPER ORDER"):
        pos_size = (acc_bal * (risk_pct / 100)) * leverage
        sl = entry_price * 0.98
        tp = entry_price * 1.06
        st.table(pd.DataFrame({
            "Metric": ["Position Size (at 5x)", "Stop Loss (2%)", "Take Profit (6%)"],
            "Value": [f"${pos_size:,.2f}", f"${sl:.4f}", f"${tp:.4f}"]
        }))

with tab2:
    st.write("### 📈 Institutional Orderflow (Swarm Data)")
    # A LISTA AQUI NO SCANNER (Swarm)
    for t in BITFUNDED_ASSETS:
        p = get_price(t)
        if p:
            with st.expander(f"🟢 {t} - Live Flow"):
                st.write(f"**Price:** ${p:.4f} | **SL:** ${p*0.98:.4f} | **TP:** ${p*1.06:.4f}")
        else:
            continue

with tab3:
    st.write("### 🌍 Macro & Study")
    st.write(f"Monitorização ativa de {len(BITFUNDED_ASSETS)} ativos da Bitfunded.")
