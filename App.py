import streamlit as st
import requests
import pandas as pd

# 1. Configuração do Ambiente
st.set_page_config(page_title="Scalp Prop - Sniper V6", layout="wide")

# 2. Engine de Preços (CoinGecko p/ Mercado Dinâmico)
@st.cache_data(ttl=300)
def get_market_movers():
    try:
        # Busca os 10 ativos com maior volume para o scanner dinâmico
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=volume_desc&per_page=10&page=1&sparkline=false"
        return requests.get(url, timeout=10).json()
    except:
        return None

# 3. Interface e Abas (Fusão das ref: 1000035734.jpg e 1000035737.jpg)
st.title("🎯 SCALP PROP • SNIPER ENGINE V6")
tab1, tab2, tab3 = st.tabs(["RULES & DRAWDOWN", "PATTERNS & FLOW", "MACRO & STUDY"])

with tab1:
    st.subheader("⚙️ Account & Sniper Parameters")
    c1, c2 = st.columns(2)
    acc_bal = c1.number_input("ACCOUNT BALANCE ($)", value=5000, step=1000)
    risk = c2.number_input("MAX RISK PER TRADE (%)", value=1.0, step=0.1)
    
    c3, c4 = st.columns(2)
    entry = c3.number_input("ENTRY PRICE", value=0.7300, format="%.4f")
    lev = c4.number_input("LEVERAGE", value=10, step=1)
    
    if st.button("EXECUTE SNIPER ORDER"):
        pos_size = (acc_bal * (risk / 100)) * lev
        sl = entry * 0.98
        tp = entry * 1.06
        data = {
            "Metric": ["Absolute Position Size", "Stop Loss (Invalidation)", "Take Profit (Strict 1:3 RR)"],
            "Value": [f"${pos_size:,.2f}", f"${sl:.4f}", f"${tp:.4f}"]
        }
        st.table(pd.DataFrame(data))

with tab2:
    st.subheader("📈 Institutional Orderflow (Swarm Data)")
    movers = get_market_movers()
    if movers:
        # Tabela consolidada como na ref: 1000035731.jpg
        for coin in movers:
            symbol = coin['symbol'].upper()
            price = coin['current_price']
            with st.expander(f"🟢 {symbol} - Live Agent Analysis"):
                st.write(f"**Live Price:** ${price:.4f}")
                st.write(f"**SL:** ${price*0.98:.4f} | **TP:** ${price*1.06:.4f}")
                st.info("Scaling Protocol: Add 20% position at TP1.")
    else:
        st.warning("Scanner synchronization in progress...")

with tab3:
    st.subheader("🌍 Macro & Study")
    st.write("Dados de mercado em tempo real carregados via API Global.")
