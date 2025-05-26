import streamlit as st
from datetime import datetime
import time

# Oldal beállítása
st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# 🔄 Automatikus újratöltés
st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: None
placeholder = st.empty()

# 🎨 Háttér és stílus
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-aX5NLrKgRBc?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    .stMarkdown h1 {
        color: white;
    }

    .box {
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1rem;
        margin-top: 1rem;
        font-size: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Barcelonai utazás")

# 📅 Fix cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)

# 🔁 Folyamatos frissítés másodpercenként
while True:
    now = datetime.now()
    delta = target_date - now

    with placeholder.container():
        if delta.total_seconds() > 0:
            days = delta.days
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            seconds = delta.seconds % 60

            st.markdown(
                f"<div class='box'>Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='box'>Ez az utazás dátuma már elmúlt.</div>",
                unsafe_allow_html=True
            )
        time.sleep(1)
        st.experimental_rerun()
