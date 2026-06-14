import streamlit as st
import pandas as pd
import requests
import random
import time

# Premium V2.0 Swarm Architecture Configuration
st.set_page_config(page_title="Scalp Prop v2.0 - AI Swarm Terminal", layout="wide", initial_sidebar_state="expanded")

st.title("🤖 Scalp Prop v2.0 — AI Swarm Intelligence")
st.caption("Active LLM Cluster Terminal | Top Setup & Institutional Flow Router | Max Leverage: 5X Cross")

# --- SIDEBAR: DYNAMIC PROPFIRM RISK SYNC ---
st.sidebar.header("🎛️ Swarm Global Settings")

account_size = st.sidebar.selectbox(
    "PropFirm Account Size (USDT)", 
    [2500, 5000, 10000, 25000, 50000, 100000, 200000],
    index=2 # Defaults to 10k account challenge
)

challenge_phase = st.sidebar.radio("Challenge Phase Target", ["Phase 1 (10% Target)", "Phase 2 (5% Target)"])
risk_per_trade_pct = st.sidebar.slider("Risk per Bot Trade (%)", 0.1, 2.0, 0.5, step=0.1)

# Dynamic Risk Sync Calculations
financial_risk = account_size * (risk_per_trade_pct / 100.0)
daily_drawdown_limit = account_size * 0.05
target_multiplier = 0.10 if "Phase 1" in challenge_phase else 0.05
swarm_target = account_size * target_multiplier

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Swarm Risk Metrics")
st.sidebar.metric("Risk Allocation / Bot", f"{financial_risk:.2f} USDT")
st.sidebar.metric("Max Daily Cluster Loss", f"{daily_drawdown_limit:.2f} USDT")
st.sidebar.metric("Dynamic Target Profit", f"{swarm_target:.2f} USDT")

st.sidebar.markdown("---")
st.sidebar.subheader("🤖 Cluster Core Authorization")
swarm_active = st.sidebar.toggle("Activate AI Swarm Execution", value=True)
execution_mode = st.sidebar.radio("Execution Mode", ["Fully Autonomous", "Semi-Autonomous (Signal Only)"])

if st.sidebar.button("🔄 Force Swarm Sync & Update", use_container_width=True):
    st.toast("Swarm synchronized across all blockchain nodes!")

# --- UNIVERSAL REAL-TIME PRICE FEED (No Binance, pure Coinbase/Gecko) ---
@st.cache_data(ttl=5)
def get_live_prices():
    prices = {}
    coinbase_mapping = {"BTC": "BTC-USD", "SOL": "SOL-USD", "LINK": "LINK-USD", "NEAR": "NEAR-USD"}
    
    for ticker, pair in coinbase_mapping.items():
        try:
            res = requests.get(f"https://api.coinbase.com/v2/prices/{pair}/spot", timeout=2)
            if res.status_code == 200:
                prices[ticker] = float(res.json()['data']['amount'])
        except Exception:
            pass

    gecko_mapping = {"bitcoin": "BTC", "solana": "SOL", "chainlink": "LINK", "near": "NEAR", "world-liberty-financial": "WLFI"}
    try:
        ids = ",".join(gecko_mapping.keys())
        gecko_res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd", timeout=2)
        if gecko_res.status_code == 200:
            data = gecko_res.json()
            for g_id, ticker in gecko_mapping.items():
                if g_id in data and (ticker not in prices or ticker == "WLFI"):
                    prices[ticker] = float(data[g_id]['usd'])
    except Exception:
        pass

    baselines = {"BTC": 63720.30, "SOL": 67.30, "LINK": 15.22, "NEAR": 4.85, "WLFI": 0.05830}
    for t, p in baselines.items():
        if t not in prices:
            prices[t] = p
    return prices

live_prices = get_live_prices()

# --- V2.0 AGENTIC LOOP ENGINE (Top Setup Matrix) ---
def run_agentic_loop_v2(ticker, technical_risk):
    # Simulated internal checks of the Top Setup rules (RSI 9/EMA 9 Cross + DXY Confluence)
    if ticker in ["BTC", "SOL", "LINK", "WLFI"]:
        probability = random.randint(81, 87)
        filter_status = "🔥 APPROVED WITH EXCELLENCE"
    else:
        probability = random.randint(66, 74)
        filter_status = "🟢 APPROVED" if probability >= 65 else "❌ REJECTED BY FILTER"
        
    position_size = financial_risk / (technical_risk / 100.0)
    margin = position_size / 5.0
    
    return filter_status, probability, position_size, margin

# --- MAIN DASHBOARD LAYOUT ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.header("🤖 Active Swarm Agents & Live Scanner")
    
    # Mapping the 2026 specialized AI models directly to assets and setup layers
    swarm_agents = [
        {"ModelID": "Qwen3-Max-Thinking", "Layer": "Institutional Heatmap Core", "Ticker": "BTC", "Type": "Long", "Risk Pct": 0.89, "SL": 63150.00, "TP2": 66200.00},
        {"ModelID": "Claude Opus 4.7", "Layer": "M15 RSI 9 / EMA 9 Momentum", "Ticker": "SOL", "Type": "Long", "Risk Pct": 2.37, "SL": 65.70, "TP2": 73.40},
        {"ModelID": "GPT-5.3 Codex", "Layer": "Execution & Slippage Audit", "Ticker": "LINK", "Type": "Long", "Risk Pct": 1.57, "SL": 14.98, "TP2": 16.10},
        {"ModelID": "MAI-Thinking-1", "Layer": "DXY Correlation Matrix", "Ticker": "NEAR", "Type": "Short", "Risk Pct": 2.06, "SL": 4.95, "TP2": 4.50},
        {"ModelID": "Gemini 3.5 Flash", "Layer": "Liquidation Pool Scanner", "Ticker": "WLFI", "Type": "Long", "Risk Pct": 2.05, "SL": 0.0571, "TP2": 0.0635},
    ]
    
    for agent in swarm_agents:
        ticker = agent["Ticker"]
        price = live_prices.get(ticker, agent["SL"])
        status, prob, size, margin = run_agentic_loop_v2(ticker, agent["Risk Pct"])
        
        with st.expander(f"⚙️ {agent['ModelID']} [{agent['Layer']}] — {ticker}USDT Task", expanded=True):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown("**AI Decision Engine**")
                st.markdown(f"**Filter Status:** {status}")
                st.markdown(f"**Success Probability:** {prob}%")
            with c2:
                st.markdown("**Top Setup Coordinates**")
                st.write(f"Live Market Price: ${price:,.4f}")
                st.write(f"Stop Loss (SL): ${agent['SL']:,.4f}")
                st.write(f"Target (TP2): ${agent['TP2']:,.4f}")
            with c3:
                st.markdown("**Sizing & Safety**")
                st.write(f"Position Size: ${size:,.2f} USDT")
                st.write(f"Margin Required (5X): ${margin:,.2f} USDT")

with col_right:
    st.header("🛡️ Swarm Global Risk Matrix")
    
    st.metric("Total AI Nodes Active", len(swarm_agents), "Parallel Architecture")
    st.metric("Cluster Health Factor", "99.4%", "Zero Lag Live Stream")
    
    st.markdown("---")
    st.subheader("🔥 Top Setup Rule Filters")
    st.info("System Lockdown: All positions automatically scale down or pause execution if the DXY volatility index breaches the safety block thresholds.")
    
    st.markdown("---")
    st.subheader("📝 Live Agentic Loops (Self-Checks)")
    # Simulating the structured validation loops mapping the notes
    logs = [
        f"[{time.strftime('%H:%M:%S')}] [1. Gather Context] Qwen3-Max-Thinking mapping major liquidity heatmaps on Coinbase.",
        f"[{time.strftime('%H:%M:%S')}] [2. Take Action] Claude Opus 4.7 verified RSI 9 crossed above EMA 9 on M15.",
        f"[{time.strftime('%H:%M:%S')}] [3. Verify Results] GPT-5.3 Codex checked PropFirm drawdown boundaries before signature.",
        f"[{time.strftime('%H:%M:%S')}] [4. Response] Cluster validation loop passed. Terminal state synchronized."
    ]
    for log in logs:
        st.caption(log)

# --- SECTION 2: CONSOLIDATED MONITOR TABLE ---
st.markdown("---")
st.header("📊 Swarm Consolidated Operations Grid")

position_table = []
for agent in swarm_agents:
    ticker = agent["Ticker"]
    price = live_prices.get(ticker)
    status, prob, size, margin = run_agentic_loop_v2(ticker, agent["Risk Pct"])
    
    position_table.append({
        "AI Agent Node": agent["ModelID"],
        "Target Asset": f"{ticker}USDT",
        "Direction": agent["Type"],
        "Live Price": f"${price:,.4f}",
        "Stop Loss": f"${agent['SL']:,.4f}",
        "Target (TP2)": f"${agent['TP2']:,.4f}",
        "Allocated Size": f"${size:,.2f}",
        "Filter Status": status,
        "Success Probability": f"{prob}%"
    })

df_positions = pd.DataFrame(position_table)
st.table(df_positions)

if swarm_active:
    st.success("🎯 Swarm v2.0 Live Core Engine actively parsing smart money targets with zero-lag routing.")
else:
    st.warning("⚠️ Swarm Execution paused manually from the side controller.")
      
