import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# 🔥 THERMAL STYLE
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

section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.4);
}

.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #FFB703, #FF5A1F);
}

</style>
""", unsafe_allow_html=True)

st.title("Signal Analyzer")

# SIDEBAR
st.sidebar.markdown("Control Panel")

T = st.sidebar.slider("Temperature (K)", 100, 1200, 300)
signal_amp = st.sidebar.slider("Signal Strength", 0.1, 1.0, 0.3)
noise_scale = st.sidebar.slider("Noise Sensitivity", 0.1, 1.0, 0.25)

show_clean = st.sidebar.toggle("Show Clean Signal")

# SIGNAL
fs = 10000
t = np.linspace(0, 1, fs)

signal = signal_amp * np.sin(2 * np.pi * 50 * t)
noise = np.random.normal(0, (T/300) * noise_scale, size=fs)
noisy_signal = signal + noise

fft_vals = np.fft.fft(noisy_signal)
freqs = np.fft.fftfreq(len(fft_vals), 1/fs)
spectrum = np.abs(fft_vals)

signal_power = np.mean(signal**2)
noise_power = np.mean(noise**2)
snr = signal_power / noise_power

# PLOTS
col1, col2 = st.columns(2)

with col1:
    st.subheader("Time Domain")

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#05070D")
    ax.set_facecolor("#0B0F1A")
    ax.plot(t[:500], noisy_signal[:500], color="#FF5A1F", linewidth=2)
    if show_clean:
        ax.plot(t[:500], signal[:500], color="#E3DFDE", alpha=0.4)
    st.pyplot(fig)

with col2:
    st.subheader("Frequency Spectrum")

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#05070D")
    ax.set_facecolor("#0B0F1A")

    ax.plot(freqs[:5000], spectrum[:5000], color="#FFB703", linewidth=2)

    noise_floor = np.mean(spectrum[:5000])
    ax.axhline(noise_floor, linestyle="--", color="#FB7185")

    st.pyplot(fig)

# SYSTEM HEALTH
st.markdown("---")
st.subheader("System Health")

c1, c2, c3 = st.columns(3)

c1.metric("Temperature", f"{T} K")
c2.metric("SNR", f"{snr:.2f}")
c3.metric("Signal Strength", f"{signal_amp:.2f}")

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=min(snr, 10),
    title={'text': "SNR"},
    gauge={'axis': {'range': [0, 10]}, 'bar': {'color': "#FF5A1F"}}
))

fig_gauge.update_layout(
    paper_bgcolor="#05070D",
    font={'color': "#E5E7EB"}
)

st.plotly_chart(fig_gauge, use_container_width=True)

if snr > 5:
    st.success("System Stable")
elif snr > 2:
    st.warning("Signal Degrading")
else:
    st.error("SYSTEM FAILURE")
