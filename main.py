# Streamlit template

# SETUP:
# pip install streamlit
# run: streamlit run main.py

import streamlit as st

header = st.container()

dataframes = st.container()

section1 = st.container()

with header:
    st.title("GDA Team Swordfish Data Normalization Project")
    st.text("Normalizing Bybit Websocket data")

with dataframes: 
    # PLACE ANYTHING IN HERE datasets, dataframes, etc. websocket data

with section1: 
    # another section, place anything, maybe display normalized data
    # Can read csvs and display in here like regular python