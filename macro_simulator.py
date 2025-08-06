import streamlit as st

st.set_page_config(page_title="Macro Chain Web - Phase 1", layout="centered")

st.title("🌐 Macro Chain Web Simulator (Phase 1)")

st.markdown("""
Adjust the sliders below to simulate macroeconomic impacts.  
This version models the effects of **Interest Rate**, **Oil Price**, and **Inflation** on:  
🔸 Gold Price  
🔸 Bitcoin  
🔸 China Economy
""")

st.sidebar.header("🔧 Input Controls")

interest_rate = st.sidebar.slider("Interest Rate Change (%)", -3.0, 3.0, 0.0, 0.25)
oil_price = st.sidebar.slider("Oil Price Change (%)", -50.0, 100.0, 0.0, 5.0)
inflation_rate = st.sidebar.slider("Inflation Rate (%)", 0.0, 10.0, 2.0, 0.1)

gold_change = 0.4 * inflation_rate + 0.02 * oil_price - 0.3 * interest_rate
bitcoin_change = 0.6 * inflation_rate - 0.5 * interest_rate + 0.02 * oil_price
china_economy_change = -0.4 * interest_rate - 0.03 * oil_price - 0.5 * inflation_rate

st.subheader("📊 Output Simulation")

st.markdown("### 🔸 Results")

import pandas as pd

output_data = {
    "Variable": ["Gold Price", "Bitcoin", "China Economy"],
    "Change (%)": [round(gold_change, 2), round(bitcoin_change, 2), round(china_economy_change, 2)],
    "Explanation": [
        "Gold typically rises with inflation and oil, falls with high interest rates.",
        "Bitcoin reacts positively to inflation, but negatively to rate hikes.",
        "China's growth slows with rising global rates, oil costs, and inflation."
    ]
}

df = pd.DataFrame(output_data)
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption("Prototype by ChatGPT • Phase 1 • Aug 2025")
