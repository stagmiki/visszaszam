import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Barcelonai utazás", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1605733160314-4d791ba3b3d5");
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

target_date = datetime(2025, 6, 19, 0, 0, 0)
placeholder = st.empty()

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
