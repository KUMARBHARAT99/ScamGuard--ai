"""
ScamGuard AI
Hybrid AI Agent (Rule-Based + Gemini LLM)
"""

import streamlit as st
from agent.analyzer import analyze_message
from agent.risk_score import calculate_risk
from agent.explanation import generate_explanation
from agent.llm_engine import llm_analyze

st.set_page_config(
    page_title="ScamGuard AI",
    page_icon="🛡",
    layout="centered"
)

st.title("🛡 ScamGuard AI")
st.caption("Hybrid AI Agent for Scam Detection & Explanation")

message = st.text_area(
    "Paste SMS / Email / WhatsApp message",
    height=150
)

use_llm = st.checkbox("Use AI (LLM) Deep Analysis", value=True)

if st.button("Analyze Message"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        # ---------- Rule-based analysis ----------
        analysis = analyze_message(message)
        risk = calculate_risk(analysis["count"])
        explanation = generate_explanation(
            analysis["indicators"], risk
        )

        st.markdown("## ⚙ Rule-Based Analysis")
        st.info(explanation)

        # ---------- LLM analysis ----------
        if use_llm:
            st.markdown("## 🤖 AI (LLM) Deep Reasoning")
            with st.spinner("AI is analyzing..."):
                llm_output = llm_analyze(message)
                st.success(llm_output)
