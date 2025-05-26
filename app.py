import streamlit as st
from datetime import datetime
import time

# Oldal beállítása
st.set_page_config(page_title="Barcelonai utazás122", layout="centered")

# 🔄 Automatikus újratöltés – fallback, ha nincs
st.experimental_rerun = st.experimental_rerun if hasattr(st, "experimental_rerun") else lambda: None
placeholder = st.empty()

# 🎨 Háttér és stílus (új, működő módszer!)
st.markdown(f"""
    <style>
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("https://i.imgur.com/hbWis1E.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.35;
        z-index: -1;
    }}
    .box {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1rem;
        margin-top: 1rem;
        font-size: 1.5rem;
        color: white;
    }}
    h1 {{
        color: white;
    }}
    </style>
""", unsafe_allow_html=True)

# Cím
st.title("Barcelonai utazás")

# 📅 Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)

# 🔁 Visszaszámláló frissítéssel
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
