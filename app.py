import streamlit as st

st.set_page_config(page_title="Thermal Noise Lab", layout="wide")

st.title("🌡️ Thermal Noise Lab")

st.markdown("""
### A simulation environment for understanding signal degradation under thermal noise
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚀 Features")
    st.markdown("""
- Real-time signal simulation  
- Frequency spectrum analysis  
- SNR-based system health  
- Interactive controls  
""")

with col2:
    st.markdown("### 🎯 Goal")
    st.markdown("""
To demonstrate how thermal noise impacts system reliability and causes failure in real-world electronic systems.
""")

st.markdown("---")
st.info("👈 Use the sidebar to explore the Analyzer and Insights pages")