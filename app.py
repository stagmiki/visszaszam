import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# ⚠️ Ez legyen az első Streamlit parancs
st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# 🔁 Automatikus frissítés 1 másodpercenként
st_autorefresh(interval=1000, key="refresh")

# 🔤 Base64 háttérkép (példaképként egy kis kép van itt)
base64_image = """
iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAHElEQVQYV2NkYGD4z0ABYBxVSFUBATGAAGCcBQC9cB2IU6kBnwAAAABJRU5ErkJggg==
"""  # Ez egy kis szürke PNG

# 🎨 Háttér beállítása Base64 képből
st.markdown(f"""
    <style>
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: url("data:image/png;base64,{base64_image.strip()}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        opacity: 0.3;
        z-index: -1;
    }}
    .box {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-top: 2rem;
        font-size: 1.5rem;
        color: white;
        text-align: center;
    }}
    h1 {{
        color: white;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Cím
st.title("Barcelonai utazás")

# 🎯 Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)
now = datetime.now()
delta = target_date - now

# ⏳ Visszaszámlálás megjelenítése
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
