import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# 🎨 Háttérkép beállítása .stApp osztályon keresztül
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1605733160314-4d791ba3b3d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .css-18e3th9 {
        background-color: rgba(0, 0, 0, 0.6) !important;
        padding: 2rem;
        border-radius: 1rem;
    }

    h1, h2, p {
        color: white !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Cím
st.title("Barcelonai utazás")

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
                f"<h2>Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</h2>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<h2>Ez az utazás dátuma már elmúlt.</h2>", unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()
