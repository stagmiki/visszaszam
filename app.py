import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# 🌆 Stílus háttérképpel és átlátszó overlay
st.markdown("""
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1605733160314-4d791ba3b3d5");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    .main {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
        color: white;
    }
    h1 {
        color: white;
        text-align: center;
    }
    </style>
    <div class="main">
""", unsafe_allow_html=True)

# 🏷️ Cím
st.title("Barcelonai utazás")

# 🎯 Célidőpont: 2025. június 19.
target_date = datetime(2025, 6, 19, 0, 0, 0)
placeholder = st.empty()

# 🔁 Élő visszaszámlálás
while True:
    now = datetime.now()
    delta = target_date - now

    with placeholder.container():
        if delta.total_seconds() > 0:
            days = delta.days
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            seconds = delta.seconds % 60
            st.markdown(f"<h2>Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2>Ez az utazás dátuma már elmúlt.</h2>", unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()

# Záró div lezárás
st.markdown("</div>", unsafe_allow_html=True)
