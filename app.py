import streamlit as st
from datetime import datetime

# ---- Egyéni háttér CSS (Barcelonai kép) ----
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/3c/Barcelona_Skyline_Panorama.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }
        .stMarkdown h1 {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Cím ----
st.title("Barcelonai utazás")

# ---- Fix dátum ----
target_date = datetime(2025, 6, 9, 0, 0, 0)  # 2025.06.09 00:00:00
now = datetime.now()
delta = target_date - now

if delta.total_seconds() > 0:
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    st.success(f"Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc")
else:
    st.warning("Ez az utazás dátuma már elmúlt.")
