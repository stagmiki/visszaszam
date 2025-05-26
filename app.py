import streamlit as st
from datetime import datetime
import time

# Streamlit oldal beállítása
st.set_page_config(page_title="BARCELONA", layout="centered")

# Háttér + animáció
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.imgur.com/hbWis1E.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .box {
        background-color: rgba(0, 0, 0, 0.6);
        bor
