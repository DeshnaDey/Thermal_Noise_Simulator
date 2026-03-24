import streamlit as st

st.set_page_config(page_title="Thermal Noise Lab", layout="wide")

# 🔥 GLOBAL THERMAL STYLE
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at 80% 20%, rgba(255,120,0,0.25), transparent 40%),
        radial-gradient(circle at 60% 70%, rgba(255,0,80,0.20), transparent 45%),
        radial-gradient(circle at 20% 30%, rgba(255,200,0,0.18), transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(255,80,0,0.15), transparent 50%),
        linear-gradient(180deg, #05070D 0%, #0B0F1A 100%);
}

/* TEXT */
h1, h2, h3 {
    color: #E5E7EB;
}

/* MAIN BLOCK */
.block-container {
    background: rgba(255,255,255,0.02);
    padding: 2rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.4);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* 🔥 CUSTOM INFO BOX */
.thermal-info {
    background: #05070D;
    border: 1px solid rgba(255,120,0,0.4);
    box-shadow: 0 0 25px rgba(255,120,0,0.25);
    padding: 16px;
    border-radius: 12px;
    color: #E5E7EB;
    margin-top: 20px;
}

/* REMOVE DEFAULT ALERT STYLE */
[data-testid="stAlert"] {
    background: transparent !important;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

# CONTENT
st.title("Thermal Noise Lab")

st.markdown("""
An interactive system to explore noise behavior, signal degradation, and system reliability under varying temperature conditions.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Features")
    st.markdown("""
- Real-time signal simulation  
- Frequency spectrum visualization  
- Signal-to-noise ratio (SNR) analysis  
- Thermal noise modeling  
""")

with col2:
    st.subheader("Objective")
    st.markdown("""
To demonstrate how thermal noise affects signal integrity and leads to system degradation in electronic systems.
""")

st.markdown("---")

st.markdown("""
<div class="thermal-info">
Use the sidebar to navigate between the Analyzer and Insights pages.
</div>
""", unsafe_allow_html=True)
