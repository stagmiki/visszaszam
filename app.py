import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Oldal beállítása
st.set_page_config(page_title="BARCELONA", layout="centered")

# Automatikus frissítés 1 másodpercenként
st_autorefresh(interval=1000, key="refresh")

# Stílus: egyszerű sötét doboz szöveggel
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
        border-radius: 1rem;
        padding: 1.5rem;
        margin-top: 2rem;
        font-size: 1.5rem;
        color: white;
        text-align: center;
        animation: fadeIn 2s ease-in;
        box-shadow: 0 0 25px rgba(0,0,0,0.4);
        backdrop-filter: blur(3px);
    }

    h1 {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        animation: slideDown 1s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

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
