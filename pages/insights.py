import streamlit as st

st.set_page_config(layout="wide")

# TITLE
st.title("Thermal Noise: Theory and Analysis")

st.markdown("---")

# INTRO
st.header("Overview")

st.markdown("""
Thermal noise, also known as Johnson–Nyquist noise, is a fundamental phenomenon in electronic systems. 
It arises due to the random motion of charge carriers (electrons) inside conductors as a result of thermal energy.

This type of noise is present in all resistive components and cannot be eliminated. It sets a fundamental limit 
on the performance of electronic and communication systems.
""")

st.markdown("---")

# PHYSICAL MODEL
st.header("Physical Origin of Thermal Noise")

st.markdown("""
The origin of thermal noise can be understood by modeling a resistor as a noise-generating element. 
Random thermal motion of electrons produces a fluctuating voltage across the resistor, which can be 
represented as a noise voltage source.
""")

st.image("images/Image1.png", use_container_width=True)

st.markdown("""
In this model:

- The resistor (R) generates thermal noise  
- The noise is represented as a voltage source (V₍johnson₎)  
- The capacitor (C) limits bandwidth  
- The amplifier and voltmeter measure the noise  

This demonstrates that thermal noise is an inherent physical property of electronic components.
""")

st.markdown("---")

# TIME DOMAIN
st.header("Noise in the Time Domain")

st.markdown("""
In the time domain, thermal noise appears as a completely random signal with no predictable pattern. 
It is often modeled as a Gaussian (normal) distribution with zero mean.
""")

st.image("images/Image2.png", use_container_width=True)

st.markdown("""
The waveform fluctuates continuously and does not repeat. This randomness is what makes noise difficult 
to remove without affecting the original signal.
""")

st.markdown("---")

# FREQUENCY DOMAIN
st.header("Noise in the Frequency Domain")

st.markdown("""
Thermal noise is classified as white noise, meaning that its power is distributed uniformly across 
frequencies within a given bandwidth.
""")

st.image("images/image3.jpg", use_container_width=True)

st.markdown("""
The flat spectrum indicates that all frequencies contribute equally to the total noise power. 
This is why increasing system bandwidth results in increased noise.
""")

st.markdown("---")

# FORMULA
st.header("Mathematical Model")

st.latex(r"P = k T B")

st.markdown("""
Where:

- P is the noise power  
- k is the Boltzmann constant  
- T is the absolute temperature (Kelvin)  
- B is the bandwidth  

This relationship shows that noise power increases linearly with both temperature and bandwidth.
""")

st.markdown("---")

# SNR
st.header("Signal-to-Noise Ratio (SNR)")

st.markdown("""
Signal-to-noise ratio (SNR) is a key parameter used to evaluate system performance. 
It measures the relative strength of a signal compared to background noise.
""")

st.image("images/image4.png", use_container_width=True)

st.markdown("""
As noise increases, the signal becomes less distinguishable. A low SNR results in poor system performance, 
data loss, and potential system failure.

The simulation developed in this project demonstrates how increasing temperature reduces SNR and degrades signal quality.
""")

st.markdown("---")

# APPLICATIONS
st.header("Practical Implications")

st.markdown("""
Thermal noise has significant implications in real-world systems:

- Communication systems: Limits data transmission quality  
- RF systems: Affects receiver sensitivity  
- Sensors: Reduces measurement accuracy  
- Audio systems: Produces background noise  

In many applications, thermal noise defines the minimum detectable signal level.
""")

st.markdown("---")

# CONCLUSION
st.header("Conclusion")

st.markdown("""
Thermal noise is an unavoidable physical phenomenon that directly impacts system performance. 
Understanding its behavior is essential for designing reliable electronic and communication systems.

This project demonstrates both the theoretical and practical aspects of thermal noise, including its 
effect on signal degradation and system reliability.
""")

st.markdown("---")

# REFERENCES
st.header("References")

st.markdown("""
1. Johnson, J. B. (1928). Thermal Agitation of Electricity in Conductors  
2. Nyquist, H. (1928). Thermal Noise in Electrical Circuits  
3. Electronics Notes – Thermal Noise  
4. Standard communication systems textbooks  
""")
