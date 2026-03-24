# Thermal Noise Visual Analyzer

An interactive simulation tool to study thermal (Johnson) noise and its impact on signal integrity and system performance.

## Features

- Real-time signal + noise simulation  
- Frequency spectrum visualization  
- Signal-to-noise ratio (SNR) analysis  
- System failure indication  
- Interactive UI with adjustable parameters  

## Concept

Thermal noise is caused by random motion of electrons in conductors and is given by:

P = kTB

Where:
- k = Boltzmann constant  
- T = Temperature  
- B = Bandwidth  

## Tech Stack

- Python  
- Streamlit  
- NumPy  
- Matplotlib  
- Plotly  

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py