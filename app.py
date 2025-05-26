import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Barcelonai utazás", layout="wide")

# 💡 HTML-es teljes képernyős háttérkép
st.markdown("""
    <style>
    .background-container {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        z-index: -1;
        background-image: url("https://images.unsplash.com/photo-1605733160314-4d791ba3b3d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        filter: brightness(0.5);
    }

    .content-box {
        background-color: rgba(0, 0, 0, 0.5);
        padding: 2rem;
        border-radius: 1rem;
        color: white;
        text-align: center;
    }

    h1, h2 {
        color: white;
        text-align: center;
    }
    </style>
    <div class="background-container"></div>
""", unsafe_allow_html=True)

# 🏷️ Cím
st.markdown("<h1>Barcelonai utazás</h1>", unsafe_allow_html=True)

# 🎯 Célidőpont
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

            st.markdown(
                f"<div class='content-box'><h2>Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</h2></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div class='content-box'><h2>Ez az utazás dátuma már elmúlt.</h2></div>", unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()
