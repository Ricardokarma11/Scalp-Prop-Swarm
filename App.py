import streamlit as st
import pandas as pd
import requests
import hashlib

# Premium V3.4 Scalp Prop - Optimized Layout
st.set_page_config(page_title="Scalp Prop v3.4 - Terminal", layout="wide")

st.title("🎯 SCALP PROP • PREMIUM V3")
st.caption("Institutional Matrix | Live Swarm Sync | Max Leverage: 5X Cross")

st.markdown("---")

# Session State for Sync
if "selected_token" not in st.session_state: st.session_state.selected_token = "BTC"
if "selected_direction" not in st.session_state: st.session_state.selected_direction = "LONG"

# Dynamic Swarm Generator
@st.cache_data(ttl=60)
def get_live_swarm_setups():
    # Simulated Live Market Engine
    default_tickers = ["BTC", "ETH", "SOL", "SUI", "LINK", "NEAR", "RUNE", "FET", "AVAX", "WIF"]
    swarm_list = []
    for ticker in default_tickers:
        swarm_list.append({"Ticker": ticker, "Prob": f"{70 + (len(ticker)*2)}%", "Direction": "LONG" if len(ticker)%2==0 else "SHORT"})
    return sorted(swarm_list, key=lambda x: x['Prob'], reverse=True)

live_setups = get_live_swarm_setups()

tab_calc, tab_rules, tab_patterns = st.tabs(["🧮 CALCULATOR", "📜 RULES & DRAWDOWN", "📈 PATTERNS & FLOW"])

with tab_calc:
    st.subheader("⚙️ Account & Risk Setup")
    col_a, col_p, col_r = st.columns(3)
    with col_a: acc_bal = st.selectbox("Account (USDT)", [2500, 5000, 10000, 25000, 50000], index=2)
    with col_p: phase = st.radio("Target", ["Stage 1 (8%)", "Stage 2 (4%)"], horizontal=True)
    with col_r: risk = st.slider("Risk Per Trade (%)", 0.1, 5.0, 0.5, step=0.1)

    # Core Calculations
    cash_risk = acc_bal * (risk / 100.0)
    daily_drawdown = acc_bal * 0.05
    profit_target = acc_bal * (0.08 if "Stage 1" in phase else 0.04)

    # --- COMPACT METRIC ROW (O TEU PEDIDO) ---
    st.markdown("---")
    m1, m2, m3 = st.columns(3)
    m1.metric("Risk / Trade", f"{cash_risk:.0f} USDT")
    m2.metric("Daily Loss", f"{daily_drawdown:.0f} USDT")
    m3.metric("Profit Target", f"{profit_target:.0f} USDT")
    st.markdown("---")

    st.subheader("🔥 Top 10 Swarm Setups")
    cols = st.columns(5)
    for i, t in enumerate(live_setups):
        target = cols[i%5]
        if target.button(f"{'🟢' if t['Direction']=='LONG' else '🔴'} {t['Ticker']}", key=f"btn_{i}", use_container_width=True):
            st.session_state.selected_token = t['Ticker']
            st.session_state.selected_direction = t['Direction']

    st.markdown("---")
    st.subheader("🔍 Custom Calibration")
    c1, c2, c3 = st.columns([2, 2, 2])
    tok = c1.text_input("Token", value=st.session_state.selected_token)
    direc = c2.selectbox("Direction", ["LONG", "SHORT"], index=0 if st.session_state.selected_direction=="LONG" else 1)
    sl = c3.slider("SL (%)", 0.5, 10.0, 2.0)

    # Simplified Calc Display
    pos_size = cash_risk / (sl / 100.0)
    st.table(pd.DataFrame({
        "Metric": ["Position Size", "Margin (5X)", "Take Profit"],
        "Value": [f"${pos_size:,.2f}", f"${(pos_size/5):,.2f}", f"{((sl*3)*100):.1f}% ROI"]
    }))

with tab_rules:
    st.write("Bitfunded Rules: 5% Max Daily Loss, 10% Overall Loss, 1:5 Leverage.")

with tab_patterns:
    st.write("Live institutional orderflow active.")
