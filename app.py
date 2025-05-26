import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# ✅ VALÓDI háttér beállítása a .stApp osztályon keresztül
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1605733160314-4d791ba3b3d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
    }
    h1, h2, h3, p {
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Cím
st.title("Barcelonai utazás")

# 🎯 Célidőpont
target_date = datetime(2025, 6, 19, 0, 0, 0)
placeholder = st.empty()

# 🔁 Élő visszaszámlálás másodpercenként
while True:
    now = datetime.now()
    delta = target_date - now

    with placeholder.container():
        if delta.total_seconds() > 0:
            days = delta.days
