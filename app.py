import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Barcelonai utazás", layout="wide")

# ✅ Háttérkép a GitHub repóból (cseréld ki a URL-t a sajátodra, ha más a neved!)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/stagmiki/visszaszamlalo/main/barcelona.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
    }}
    h1, h2 {{
        color: white;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# 📍 Cím
st.markdown("<h1>Barcelonai utazás</h1>", unsafe_allow_html=True)

# 🎯 Cél dátum
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
                f"<div class='block-container'><h2>Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</h2></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div class='block-container'><h2>Ez az utazás dátuma már elmúlt.</h2></div>", unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()
