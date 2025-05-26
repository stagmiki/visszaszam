import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Oldal beállítása
st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# Automatikus frissítés 1 másodpercenként
st_autorefresh(interval=1000, key="refresh")

# Stílus: egyszerű sötét doboz szöveggel
st.markdown("""
    <style>
    .box {
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-top: 2rem;
        font-size: 1.5rem;
        color: white;
        text-align: center;
    }

    h1 {
        text-align: center;
        color: white;
    }

    body {
        background-color: #1c1c1c;
    }
    </style>
""", unsafe_allow_html=True)

# Cím
st.title("Barcelonai utazás")

# Cél dátum beállítása
target_date = datetime(2025, 6, 19, 0, 0, 0)
now = datetime.now()
delta = target_date - now

# Visszaszámlálás megjelenítése
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
