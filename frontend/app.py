import streamlit as st
import requests
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Enterprise Incident Intelligence System",
    page_icon="",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: #e5e7eb;
}

.main-card {
    background-color: #1e293b;
    padding: 32px;
    border-radius: 10px;
    border: 1px solid #334155;
    margin-bottom: 32px;
}

.report-card {
    background-color: #020617;
    padding: 24px;
    border-radius: 8px;
    border: 1px solid #334155;
    font-family: Consolas, Monaco, monospace;
    font-size: 13px;
    white-space: pre-wrap;
    line-height: 1.7;
}

.title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 6px;
}

.subtitle {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 32px;
}

label {
    font-weight: 600;
    color: #e5e7eb;
}

textarea {
    background-color: #020617 !important;
    color: #e5e7eb !important;
}

.stButton>button {
    width: 100%;
    padding: 14px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 6px;
    background: linear-gradient(135deg, #1d4ed8, #1e3a8a);
    color: white;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
}


</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">Enterprise Incident Intelligence System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered decision support for faster incident resolution</div>',
    unsafe_allow_html=True
)

# ---------------- INCIDENT INPUT ----------------
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown("### Incident Description")

incident_text = st.text_area(
    "Describe the current production issue",
    height=160,
    placeholder="Payments are failing and latency increases during peak traffic hours.",
    label_visibility="collapsed"
)

st.markdown(
    f'<div class="footer-text">{len(incident_text)} characters</div>',
    unsafe_allow_html=True
)

analyze_clicked = st.button("Analyze Incident")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ANALYSIS RESULT ----------------
if analyze_clicked:
    if not incident_text.strip():
        st.warning("Please enter a valid incident description.")
    else:
        with st.spinner("Analyzing incident using historical intelligence..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze-incident",
                json={"description": incident_text}
            )

        if response.status_code == 200:
            report = response.json()["analysis"]

            st.markdown('<div class="main-card">', unsafe_allow_html=True)
            st.markdown("### Incident Analysis Report")
            st.markdown(
                f'<div class="report-card">{report}</div>',
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Backend service not reachable. Ensure FastAPI is running.")
