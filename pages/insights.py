import streamlit as st

st.set_page_config(layout="wide")

# 🔥 STYLE
st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 80% 20%, rgba(255,120,0,0.25), transparent 40%),
        radial-gradient(circle at 60% 70%, rgba(255,0,80,0.20), transparent 45%),
        radial-gradient(circle at 20% 30%, rgba(255,200,0,0.18), transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(255,80,0,0.15), transparent 50%),
        linear-gradient(180deg, #05070D 0%, #0B0F1A 100%);
}

h1, h2, h3 {
    color: #E5E7EB;
}

/* IMAGE PANEL */
[data-testid="stImage"] {
    border-radius: 20px;
    padding: 14px;
    background: rgba(255,255,255,0.03);
    border: 2px solid rgba(255,255,255,0.12);

    box-shadow:
        0 0 50px rgba(255,120,0,0.2),
        inset 0 0 40px rgba(0,0,0,0.6);

    transition: all 0.4s ease;
}

[data-testid="stImage"]:hover {
    box-shadow:
        0 0 80px rgba(255,120,0,0.4),
        inset 0 0 40px rgba(0,0,0,0.7);
}

[data-testid="stImage"] img {
    border-radius: 14px;
    transition: transform 0.4s ease;
}

[data-testid="stImage"]:hover img {
    transform: scale(1.04);
}

</style>
""", unsafe_allow_html=True)

st.title("Thermal Noise: Theory and Analysis")

st.markdown("---")

st.header("Overview")
st.markdown("""
Thermal noise arises due to random electron motion and is present in all electronic systems.
""")

st.markdown("---")

st.header("Physical Model")
st.image("images/image1.png", use_container_width=True)

st.markdown("---")

st.header("Time Domain")
st.image("images/image2.png", use_container_width=True)

st.markdown("---")

st.header("Frequency Domain")
st.image("images/image3.png", use_container_width=True)

st.markdown("---")

st.header("Signal-to-Noise Ratio")
st.image("images/image4.png", use_container_width=True)

st.markdown("---")

st.header("Mathematical Model")
st.latex(r"P = kTB")
