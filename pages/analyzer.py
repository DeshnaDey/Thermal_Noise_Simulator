import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# PAGE CONFIG
st.set_page_config(layout="wide")

# 💣 APPLE-STYLE GLASS UI
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(180deg, #0A0F1C 0%, #0F172A 100%);
}

/* MAIN CONTAINER */
.block-container {
    padding: 2rem;
}

/* GLASS CARDS */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 16px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.03);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* HEADINGS */
h1, h2, h3, h4 {
    color: #E2E8F0;
}

/* SLIDER COLOR */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #3B82F6, #14B8A6);
}

/* TOGGLE / CHECKBOX */
.stCheckbox, .stToggle {
    accent-color: #3B82F6;
}

/* ALERT BOXES */
.stAlert {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
}

/* PLOTS */
canvas {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("📊 Signal Analyzer")

# HERO SECTION
st.markdown("""
<div style="
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    color: #E2E8F0;
">
    <b>Thermal Noise Simulation</b><br>
    Explore how temperature affects signal clarity and system reliability.
</div>
""", unsafe_allow_html=True)

# 🎛️ SIDEBAR CONTROLS
st.sidebar.markdown("## ⚙️ Control Panel")

T = st.sidebar.slider("Temperature (K)", 100, 1200, 300)
signal_amp = st.sidebar.slider("Signal Strength", 0.1, 1.0, 0.3)
noise_scale = st.sidebar.slider("Noise Sensitivity", 0.1, 1.0, 0.25)

show_clean = st.sidebar.toggle("Show Clean Signal")
compare = st.sidebar.toggle("Comparison Mode")

# TIME
fs = 10000
t = np.linspace(0, 1, fs)

# SIGNAL
signal = signal_amp * np.sin(2 * np.pi * 50 * t)

# NOISE
noise = np.random.normal(0, (T/300) * noise_scale, size=fs)
noisy_signal = signal + noise

# FFT
fft_vals = np.fft.fft(noisy_signal)
freqs = np.fft.fftfreq(len(fft_vals), 1/fs)
spectrum = np.abs(fft_vals)

# SNR
signal_power = np.mean(signal**2)
noise_power = np.mean(noise**2)
snr = signal_power / noise_power

# LAYOUT
col1, col2 = st.columns(2)

# 📊 TIME DOMAIN
with col1:
    st.markdown("#### ⏱️ Time Domain")

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#0A0F1C")
    ax.set_facecolor("#111827")

    ax.plot(t[:500], noisy_signal[:500], linewidth=2, color="#3B82F6", label="Noisy")
    if show_clean:
        ax.plot(t[:500], signal[:500], alpha=0.4, color="#27F5E7", label="Clean")
    ax.legend()

    st.pyplot(fig)

# 📡 FREQUENCY DOMAIN
with col2:
    st.markdown("#### 📡 Spectrum Analyzer")

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#0A0F1C")
    ax.set_facecolor("#111827")

    ax.plot(freqs[:5000], spectrum[:5000], linewidth=2, color="#14B8A6")

    noise_floor = np.mean(spectrum[:5000])
    ax.axhline(noise_floor, linestyle="--", color="#64748B", label="Noise Floor")

    ax.legend()

    st.pyplot(fig)

# 🧠 SYSTEM HEALTH
st.markdown("---")
st.markdown("### 🧠 System Health")

c1, c2, c3 = st.columns(3)

c1.metric("Temperature", f"{T} K")
c2.metric("SNR", f"{snr:.2f}")
c3.metric("Signal Strength", f"{signal_amp:.2f}")

# 🎚️ SNR GAUGE
gauge_value = min(snr, 10)

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=gauge_value,
    title={'text': "SNR Level"},
    gauge={
        'axis': {'range': [0, 10]},
        'bar': {'color': "#3B82F6"},
        'steps': [
            {'range': [0, 2], 'color': "#1f2937"},
            {'range': [2, 5], 'color': "#334155"},
            {'range': [5, 10], 'color': "#0f172a"}
        ],
    }
))

fig_gauge.update_layout(
    paper_bgcolor="#0A0F1C",
    font={'color': "#E2E8F0"}
)

st.plotly_chart(fig_gauge, use_container_width=True)

# STATUS
if snr > 5:
    st.success("System Stable")
elif snr > 2:
    st.warning("Signal Degrading")
else:
    st.error("🚨 SYSTEM FAILURE")

# 🔁 COMPARISON MODE
if compare:
    st.markdown("---")
    st.markdown("### 🔁 Comparison Mode")

    T2 = 1000
    noise2 = np.random.normal(0, (T2/300) * noise_scale, size=fs)
    noisy_signal2 = signal + noise2

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"**{T}K**")
        fig, ax = plt.subplots()
        fig.patch.set_facecolor("#0A0F1C")
        ax.set_facecolor("#111827")
        ax.plot(t[:500], noisy_signal[:500], color="#3B82F6")
        st.pyplot(fig)

    with col4:
        st.markdown(f"**{T2}K**")
        fig, ax = plt.subplots()
        fig.patch.set_facecolor("#0A0F1C")
        ax.set_facecolor("#111827")
        ax.plot(t[:500], noisy_signal2[:500], color="#14B8A6")
        st.pyplot(fig)
