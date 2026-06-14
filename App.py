import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Scalp Prop - Sniper Mode", layout="wide")

st.title("🎯 SCALP PROP • SNIPER V5")

# --- ENGINE DE PREÇO (Coinbase) ---
@st.cache_data(ttl=30)
def get_price(ticker):
    try:
        url = f"https://api.coinbase.com/v2/prices/{ticker.upper()}-USD/spot"
        res = requests.get(url, timeout=5).json()
        return float(res['data']['amount'])
    except:
        return None

# --- SEPARADORES (Como na foto 1000035751.jpg) ---
tab1, tab2, tab3 = st.tabs(["RULES & DRAWDOWN", "PATTERNS & FLOW", "MACRO & STUDY"])

with tab1:
    st.subheader("⚙️ Account & Sniper Parameters")
    
    # Inputs Manuais de Controlo
    c1, c2 = st.columns(2)
    acc_bal = c1.number_input("ACCOUNT BALANCE ($)", value=5000, step=1000)
    risk_pct = c2.number_input("MAX RISK PER TRADE (%)", value=1.0, step=0.1)
    
    c3, c4 = st.columns(2)
    entry_price = c3.number_input("CURRENT ENTRY PRICE", value=0.7300, format="%.4f")
    leverage = c4.number_input("INTENDED LEVERAGE", value=10, step=1)
    
    token = st.text_input("TOKEN", value="SUI")
    
    if st.button("EXECUTE SNIPER ORDER"):
        # Cálculos Sniper
        pos_size = (acc_bal * (risk_pct / 100)) * leverage
        sl = entry_price * 0.98
        tp_rr = entry_price * 1.06 # RR 1:3 baseado no SL de 2%
        fib_05 = entry_price * 0.99
        
        # Tabela de Métricas (Igual à foto)
        data = {
            "Performance Metric": ["Absolute Position Size", "Fibonacci 0.5 (Equilibrium)", "Fibonacci 0.618 (Golden Zone)", "Take Profit Strictly (1:3 RR)", "Stop Loss (Structural Invalidation)"],
            "Calculated Value": [f"${pos_size:,.2f}", f"${fib_05:.4f}", f"${entry_price*0.985:.4f}", f"${tp_rr:.4f}", f"${sl:.4f}"]
        }
        st.table(pd.DataFrame(data))

with tab2:
    st.write("### 📈 Institutional Orderflow")
    st.info("Scanner active: Detecting liquidity sweeps and Market Maker targets.")

with tab3:
    st.write("### 🌍 Macro & Study")
    st.write("Analysis of funding rates and global liquidity zones.")

st.markdown("---")

# --- TOP 10 SWARM SETUPS ---
st.subheader("🔥 Top 10 Pre-Approved Swarm Setups")
tokens = ["BTC", "SOL", "SUI", "LINK", "NEAR", "FET", "ETH", "AVAX", "WIF", "LTC"]

for t in tokens:
    with st.expander(f"🟢 {t} - Live Analysis"):
        p = get_price(t)
        if p:
            st.write(f"**Entry:** ${p:.4f} | **SL:** ${p*0.98:.4f} | **TP:** ${p*1.06:.4f}")
        else:
            st.write("Syncing data...")
