import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Scalp Prop Terminal", layout="wide")
st.title("SCALP PROP • LIVE ENGINE")

# --- DATA ENGINE (CoinGecko) ---
def get_coingecko_price(ticker_name):
    """Fetches price from CoinGecko based on common symbol naming."""
    try:
        # Mapping common symbols to CoinGecko IDs
        mapping = {
            "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", 
            "SUI": "sui", "LINK": "chainlink", "NEAR": "near", 
            "RUNE": "thorchain", "FET": "artificial-superintelligence-alliance", 
            "AVAX": "avalanche-2", "WIF": "dogwifhat", "LTC": "litecoin"
        }
        token_id = mapping.get(ticker_name.upper(), ticker_name.lower())
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd"
        response = requests.get(url, timeout=5).json()
        return response[token_id]['usd']
    except:
        return None

# --- UI: METRIC ROW ---
col1, col2, col3 = st.columns(3)
col1.metric("Risk / Trade", "50 USDT")
col2.metric("Daily Loss", "500 USDT")
col3.metric("Profit Target", "800 USDT")
st.markdown("---")

# --- CUSTOM SETUP (Live) ---
st.subheader("🔍 Live Operational Setup")
col_in, col_btn = st.columns([3, 1])
token_input = col_in.text_input("Enter Token:", value="LTC")

if col_btn.button("SCAN"):
    price = get_coingecko_price(token_input)
    if price:
        sl = price * 0.98
        tp1 = price * 1.02
        tp2 = price * 1.04
        
        st.success(f"✅ Real-Time Data: {token_input.upper()} | ${price:.4f}")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Stop Loss", f"${sl:.4f}")
        m2.metric("TP 1 (2%)", f"${tp1:.4f}")
        m3.metric("TP 2 (4%)", f"${tp2:.4f}")
        st.info("💡 Scaling: Add 20% margin at TP1; Move SL to Break Even.")
    else:
        st.error("Ticker not found in CoinGecko. Check name.")

st.markdown("---")

# --- TOP 10 SWARM SETUPS (Live Data) ---
st.subheader("🔥 Top 10 Swarm Setups")
top_tickers = ["BTC", "SOL", "SUI", "LINK", "NEAR", "FET", "ETH", "AVAX", "WIF", "LTC"]

for t in top_tickers:
    with st.expander(f"🟢 {t} - Live Analysis"):
        p = get_coingecko_price(t)
        if p:
            st.write(f"**Live Entry:** ${p:.4f}")
            st.write(f"**Stop Loss:** ${p*0.98:.4f}")
            st.write(f"**TP 1:** ${p*1.02:.4f} | **TP 2:** ${p*1.04:.4f}")
        else:
            st.write("Loading price...")
